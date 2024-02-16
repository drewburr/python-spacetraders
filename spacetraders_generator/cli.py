import json
import typer

app = typer.Typer()

@app.command()
def generate(path: str):
    """Generate client from relative path"""

    with open(path) as f:
        bundle=json.load(f)

    print(bundle['openapi'])
