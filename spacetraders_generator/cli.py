import json
import shutil
import typer
from dataclasses import dataclass, field
from pathlib import Path
from typing import Union

from openapi_python_client import cli as oapi_cli
from openapi_python_client import utils as oapi_utils
from openapi_python_client import config as oapi_config
from openapi_python_client.parser.openapi import EndpointCollection, Endpoint
import openapi_python_client as oapi_client

from jinja2 import Environment, PackageLoader, select_autoescape


import pprint

app = typer.Typer()

PACKAGE_NAME = "spacetraders_client"
PROJECT_DIR: Path = Path.cwd()


@dataclass
class ModuleRep:
    name: str
    identifier: str
    path: list[str]
    tag: str
    endpoint: Endpoint

    def __post_init__(self):
        self.endpoint_vars = vars(self.endpoint)

    # @property
    # def template_data(self):
    #     return {
    #         "identifier": self.identifier,
    #         "path": self.path,
    #         "name": self.name,
    #         "tag": self.tag,
    #     }

    def to_dict(self):
        return {
            "name": self.name
        }

@dataclass()
class ModuleNode():
    name: str
    modules: list[ModuleRep] = field(default_factory=list)
    next: list["ModuleNode"] = field(default_factory=list)
    is_root: bool = field(default=False)

    def find_next(self, name: str) -> Union["ModuleNode", None]:
        found = [x for x in self.next if x.name == name]
        if len(found) > 1:
            raise Exception("Multiple modules found!")

        return None if not found else found[0]

    def to_dict(self):
        return {
            "name": self.name,
            "modules": [x.to_dict() for x in self.modules],
            "next": [x.to_dict() for x in self.next]
        }

    def render(self, path: Path, env: Environment):

        render_data = {
            "modules": self.modules,
            "next": self.next
        }

        if not self.next:
            module_path = path/f"{self.name}.py"
        else:
            path = path/self.name
            module_path = path/"__init__.py"
            self.setup_dir(path)

        if self.modules:
            module_template = env.get_template("module.py.jinja")
            module_path.write_text(
                module_template.render(**render_data), encoding="utf-8")

        [node.render(path, env) for node in self.next]


    def setup_dir(self, path):
        try:
            path.mkdir()
        except FileExistsError:
            pass



@app.command()
def generate(bundle_path: str):
    """Generate client from relative path"""

    setup_package_dir(PACKAGE_NAME)

    project = get_oapi_project(bundle_path)

    # models = list(project.openapi.models)
    endpoint_collections = project.openapi.endpoint_collections_by_tag

    env = Environment(
        loader=PackageLoader(__package__),
        trim_blocks=True,
        lstrip_blocks=True,
        extensions=["jinja2.ext.loopcontrols"],
        keep_trailing_newline=True,
        autoescape=select_autoescape(),
    )

    env.globals.update(
        type=type
        # utils=utils,
        # python_identifier=lambda x: utils.PythonIdentifier(x, config.field_prefix),
        # class_name=lambda x: utils.ClassName(x, config.field_prefix),
        # package_name=self.package_name,
        # package_dir=self.package_dir,
        # package_description=self.package_description,
        # package_version=self.version,
        # project_name=self.project_name,
        # project_dir=self.project_dir,
        # openapi=self.openapi,
        # endpoint_collections_by_tag=self.openapi.endpoint_collections_by_tag,
    )

    module_tree = generate_tree(endpoint_collections)

    module_tree.render(PROJECT_DIR, env)

    pprint.pp(module_tree.to_dict())


def generate_tree(endpoint_collections: dict[oapi_utils.PythonIdentifier, EndpointCollection]):
    module_tree = ModuleNode(name=PACKAGE_NAME)
    for endpoint_collection in endpoint_collections.values():
        for endpoint in endpoint_collection.endpoints:

            module = ModuleRep(
                name=endpoint.name,
                identifier=oapi_utils.PythonIdentifier(endpoint.name, ""),
                path=endpoint.path.split("/")[1:],
                tag=endpoint.tag,
                endpoint=endpoint
            )

            module_node = module_tree
            next = module_node
            for step in module.path:
                if step == '':
                    step = module.identifier

                next = module_node.find_next(step)
                if not next:
                    next = ModuleNode(step)
                    module_node.next.append(next)

                # print(next)
                module_node = next

            next.modules.append(module)

    return module_tree


def get_oapi_project(bundle_path):
    # Hack together openapi_python_client to parse OpenAPI spec
    configFile = oapi_config.ConfigFile.load_from_path(Path("openapi-client.yml"))
    config = oapi_config.Config.from_sources(
        config_file=configFile,
        meta_type=oapi_cli.MetaType.NONE,
        document_source=Path(bundle_path),
        file_encoding="utf-8",
    )
    project = oapi_client._get_project_for_url_or_path(config)
    return project


def setup_package_dir(package_name):
    package_dir: Path = PROJECT_DIR / package_name

    if package_dir.is_dir():
        print("Package already exists. Removing..")
        shutil.rmtree(package_dir)

    print(f"Generating {package_name}")
    try:
        package_dir.mkdir()
    except FileExistsError as e:
        print(e)
        raise Exception("Directory already exists.")

    return package_dir
