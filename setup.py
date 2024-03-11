from setuptools import setup, find_packages

setup(
    name='flask-structure',
    version='0.1',
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
)
