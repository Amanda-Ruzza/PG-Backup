# The setup.py file specifies how the project is to be installed and defines the project's metadata

from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()

setup(
    name='pgbackup',
    version='0.1.0',
    description='Database backups locally or to AWS S3',
    long_description=readme,
    author='ANR',
    #author_email='xxx@email.com,'
    install_requires=['boto3'],# this list defines where the necessary project dependencies will go
    packages=find_packages('src'),
    package_dir={'': 'src'}, # this is a dictionary that points from an empty string to the 'src' directory
    entry_points={
        'console_scripts':[
            'pgbackup=pgbackup.cli:main',
            ]
        } 
)

