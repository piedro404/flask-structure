from setuptools import setup, find_packages

setup(
    name='flask-structure',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'flask-structure = flask-structure.__main__:create',
        ],
    },
    install_requires=[
        'Click',
    ],
)
