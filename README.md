# spacetraders python client

A client library for accessing SpaceTraders API

## Usage

First, create a client:

```python
from spacetraders import Client

client = Client(base_url="https://api.spacetraders.io/v2")
```

If the endpoints you're going to hit require authentication, use `AuthenticatedClient` instead:

```python
from spacetraders import AuthenticatedClient

client = AuthenticatedClient(base_url="https://api.spacetraders.io/v2", token="SuperSecretToken")
```

Now call your endpoint and use your models:

```python
from spacetraders.models import GetMyAgentResponse200
from spacetraders.types import Response

response: Response[GetMyAgentResponse200] = client.agents.get_my_agent()
```

Or do the same thing with an async version:

```python
from spacetraders.models import GetMyAgentResponse200
from spacetraders.types import Response

response: Response[GetMyAgentResponse200] = await client.agents.get_my_agent()
```

By default, when you're calling an HTTPS API it will attempt to verify that SSL is working correctly. Using certificate verification is highly recommended most of the time, but sometimes you may need to authenticate to a server (especially an internal server) using a custom certificate bundle.

```python
client = AuthenticatedClient(
    base_url="https://internal_api.example.com",
    token="SuperSecretToken",
    verify_ssl="/path/to/certificate_bundle.pem",
)
```

You can also disable certificate validation altogether, but beware that **this is a security risk**.

```python
client = AuthenticatedClient(
    base_url="https://internal_api.example.com",
    token="SuperSecretToken",
    verify_ssl=False
)
```

There are more settings on the generated `Client` class which let you control more runtime behavior, check out the docstring on that class for more info.

Things to know:

1. All path/query params and bodies become method arguments.
1. Tagged endpoints will use the first tag as a module name for the function
1. Any endpoint which did not have a tag will be in `client.default`

## Refreshing the API definition

This project is generated from [SpaceTradersAPI/api-docs](https://github.com/SpaceTradersAPI/api-docs/).

Ensure development dependencies are installed:

- npx (10.1.2)
- poetry (1.2.0)

Run `./generate.sh` to execute steps needed to refresh the API defintion.

## Building / publishing this Client

This project uses [Poetry](https://python-poetry.org/) to manage dependencies and packaging.  Here are the basics:

1. Update the metadata in pyproject.toml (e.g. authors, version)
1. Publish the client with `poetry publish --build -r <your-repository-name>` or, if for public PyPI, just `poetry publish --build`

If you want to install this client into another project without publishing it (e.g. for development) then:

1. If that project **is using Poetry**, you can simply do `poetry add <path-to-this-client>` from that project
1. If that project is not using Poetry:
    1. Build a wheel with `poetry build -f wheel`
    1. Install that wheel from the other project `pip install <path-to-wheel>`
