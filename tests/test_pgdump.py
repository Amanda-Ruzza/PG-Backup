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

def test_dump_handles_oserror(mocker):
    """
    pgdump.dump returns a reasonable error if pg_dump isn't installed
    """
    mocker.patch('subprocess.Popen', side_effect=OSError('no such file'))
    with pytest.raises(SystemExit):
        pgdump.dump(url)
    
def test_dump_file_name_without_timestamp():
    """
    pgdump.dump_file_name returns the name of the database
    """
    assert pgdump.dump_file_name(url) == "db_one.sql"

def test_dump_file_name_with_timestamp():
    """
    pgdump.dump_file_name returns the name of the database with timestamp
    """
    timestamp = "2022-11-07T20:30:10"
    assert pgdump.dump_file_name(url, timestamp) == f"db_one-{timestamp}.sql"