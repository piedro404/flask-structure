import os
import click
import zipfile  

@click.group()
def cli():
    pass

@cli.command()
def home():
    """
    Welcome to the flask-structure library and repository location 
    """
    click.echo('Welcome to Flask Project Structure ⚒️')
    click.echo('Visit to Repository: https://github.com/piedro404/flask-structure')

@cli.command()
def create():
    """
    Creates a Flask project structure and extracts files from a zipped archive.
    """
    base_path = os.path.abspath(os.path.dirname(__file__))
    template_path = os.path.join(base_path, 'flask-api-structure.zip')

    destination_path = os.getcwd()

    try:
        # Extract files from the compressed archive (flask_project_template.zip)
        with zipfile.ZipFile(template_path, 'r') as zip_ref:
            zip_ref.extractall(destination_path)

        click.echo('Flask Project Structure successfully created 🚀🧩')
    except Exception as e:
        click.echo(f'Error creating project structure 🥅: {e}')

if __name__ == '__main__':
    cli()
