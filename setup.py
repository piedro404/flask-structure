from setuptools import setup, find_packages

# Lê o conteúdo do README.md
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='flask-structure',
    version='0.1.1',
    author='Piedro404',
    author_email='pedro.henrique.martins404@gmail.com',
    description='A Python library dedicated to exemplify and facilitate the start of Flask projects for APIs 💫. Download flask-structure and streamline the "start" of your projects with ease 🚀.',
    long_description=long_description,  # Utiliza o conteúdo do README como descrição longa
    long_description_content_type='text/markdown',  # Indica o tipo de conteúdo do README (markdown)
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'flask-structure = flask_structure_handler.__main__:cli',
        ],
    },
    install_requires=[
        'Click',
        # 'Flask',
        # 'Flask-Cors',
        # 'Cerberus'
    ],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    project_urls={
        'Homepage': 'https://github.com/piedro404/flask-structure',
        'Issues': 'https://github.com/piedro404/flask-structure/issues',
    },
)
