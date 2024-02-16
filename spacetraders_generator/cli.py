import json
import typer
from pathlib import Path
from openapi_python_client import cli as oapi_cli
from openapi_python_client import config as oapi_config
import openapi_python_client as oapi_client

app = typer.Typer()

@app.command()
def generate(path: str):
    """Generate client from relative path"""

    # Hack together openapi_python_client to parse OpenAPI spec
    with open(path) as f:
        bundle=json.load(f)

    print(bundle['openapi'])

    configFile = oapi_config.ConfigFile.load_from_path(Path('openapi-client.yml'))

    config = oapi_config.Config.from_sources(config_file=configFile, meta_type=oapi_cli.MetaType.NONE, document_source=Path('bundle.json'), file_encoding='utf-8')

    project = oapi_client._get_project_for_url_or_path(config)

    models = list(project.openapi.models)
    endpoint_collections = project.openapi.endpoint_collections_by_tag

    print(endpoint_collections.keys())
