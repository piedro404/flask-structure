import os
import click
import zipfile  

@click.command()
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

        click.echo(f'Flask Project Structure successfully created 🚀🧩')
    except Exception as e:
        click.echo(f'Error creating project structure 🥅: {e}')

if __name__ == '__main__':
    create()
