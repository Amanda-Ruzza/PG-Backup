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
Pre-Project requirements:
- Build a PostgreSQL server
- Have the proper version of the PostgreSQL client installed on the local machine, so we can access the PGdump tool to ‘dump the PostgreSQL Database’
- The ``setup.py`` file specifies how the project is to be installed and defines the project's metadata. The ``setup`` function defines where the ``setuptools`` will look for the project's source code, and what other packages need to be installed so that the packages can work
- Using the ``Red, Green, Refactor `` TDD approach, build a CLI interpreter for testing thourgh ``pytest`` and added documentation to our test by creating a ``test file``
- Using the ``Pytest built in features`` to clean up our tests and remove duplication
- The ``Pytest fixture (@pytest.fixture)`` is a ``decorator``. A 'decorator' is a function that returns another function 
- Using a ``Mocking Library`` to test things that have side effects or to modify code that it's not our own without affecting the real code. This prevents using the standard library function and modifying real things that could jeopardize the real project 
- 