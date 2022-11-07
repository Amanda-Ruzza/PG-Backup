import tempfile
import pytest 
from pgbackup import storage

# a fixture [ex: @pytest.fixture] is a decorator that wraps the 'infile function' and register it as something that can be injected into each testing function
@pytest.fixture
def infile():
    f = tempfile.TemporaryFile()
    f.write(b'Testing') # the 'b' creates a bytes object
    f.seek(0)
    return f


# Test function for local 
def test_storing_file_locally(infile):
    """
    Writes content from one file-like to another
    """
    outfile = tempfile.NamedTemporaryFile(delete=False) # setting the 'delete = false' boolean prevents the file to be deleted after being opened for the 1st time, because the 'loal method' will close the file as soon as it's completed
    storage.local(infile, outfile) # this command stores the content of the temporary file locally
    with open(outfile.name, 'rb') as f:
        assert f.read() == b'Testing' # this 'asserts' that the contents written in the infile match with the outfile

# Test function for S3
def test_storing_file_on_s3(mocker, infile):
    """
    Writes content to one file-like to S3
    """
    client = mocker.Mock()
    storage.s3(client, infile, "bucket", "file-name")
    client.upload_fileobj.assert_called_with(client, infile, "bucket", "file-name")

