import pytest 
import subprocess

from pgbackup import pgdump

url = "postgres://bob:password@example.com:5432/db_one"

# creating a 'dump' function that will take a URL and will return a process that we can read stout and to pass to store things to s3 or the local file
def test_dump_calls_pg_dump(mocker):
    """
    Utilize pg_dump with the database URL
    """
    mocker.patch('subprocess.Popen')
    assert pgdump.dump(url)
    subprocess.Popen.assert_called_with(['pg_dump', url], stout=subprocess.PIPE)
