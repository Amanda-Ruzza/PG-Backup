Pg Backup
========
CLI for backing up remote PostgreSQL databases locally or to AWS S3.
Preparing for Development
-------------------------
1. Ensure ``pip`` and ``pipenv`` are installed
2. Clone repository: ``git clone git@github.com:example/pgbackup``
3. ``cd`` into repository
4. Fetch development dependencies ``make install``
5. Activate virtualenv: ``pipenv shell``
Usage
-----
Pass in a full database URL, the storage driver, and destination.
S3 Example w/ bucket name:
::
 $ pgbackup postgres://bob@example.com:5432/db_one --driver s3
backups
Local Example w/ local path:
$ pgbackup postgres://bob@example.com:5432/db_one --driver
local /var/local/db_one/backups
Running Tests
-------------
Run tests locally using ``make`` if virtualenv is active:
::
 $ make
If virtualenv isn’t active then use:
::
 $ pipenv run make

-----
-----
::
_____________________________________________
Project Study Notes:

This project builds a CLI utility that give a connection string to a PostgreSQL database and backs itself up to an S3 bucket.
Project implementations:
- Build a PostgreSQL server
- Have the proper version of the PostgreSQL client installed on the local machine, so we can access the PGdump tool to ‘dump the PostgreSQL Database’
- The ``setup.py`` file specifies how the project is to be installed and defines the project's metadata. The ``setup`` function defines where the ``setuptools`` will look for the project's source code, and what other packages need to be installed so that the packages can work
- While setting up the ``testing path`` on the ``Makefile``, the correct syntax should have no spaces after the ``=`` as shown: ``PYTHONPATH=./src`` 
- Using the ``Red, Green, Refactor `` TDD approach, build a CLI interpreter for testing thourgh ``pytest`` and added documentation to our test by creating a ``test file``
- Using the ``Pytest built in features`` to clean up our tests and remove duplication
- The ``Pytest fixture (@pytest.fixture)`` is a ``decorator``. A 'decorator' is a function that returns another function 
- Using a ``Mocking Library`` to test things that have side effects or to modify code that it's not our own without affecting the real code. This prevents using the standard library function and modifying real things that could jeopardize the real project 
- ``Pytest Mock`` is a wrapper around the  Mock library. Used ``Side Effect`` key word argument/attribute to give a KeyError in the mock ``test_pgdump.py`` file 
- The ``test_storage.py`` file implements the local storage strategy for the database dump 
- Used the ``tempfile``package to generate temporary files for testing purposes
- Used ``pipenv install boto3 `` to install the boto3 dependency within the Python's virtual environment as a way to implement the connection to AWS S3 to store the database backups
- Created a test function for S3 on the ``test_storage.py`` file 
- boto3 is the 'client' that knows how to write from Python into S3 
- the boto3 ``upload_fileobj`` function to upload a file-like object to S3
- Made an ``automatic script creation`` dictionary on the ``setup.py`` file
- Built a ``wheel`` for the full package 
- Created  a configuration file [``setup.cfg``] to set up the ``bdist_wheel``in order to define the Python version for this project 