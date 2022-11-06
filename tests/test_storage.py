import tempfile

from pgbackup import storage

def test_storing_file_locally():
    """
    Writes content from one file-like to another
    """
    infile = tempfile.TemporaryFile()
    infile.write(b'Testing') # the 'b' creates a bytes object
    infile.seek(0)

    outfile = tempfile.NamedTemporaryFile(delete=False) # setting the 'delete = false' boolean prevents the file to be deleted after being opened for the 1st time, because the 'loal method' will close the file as soon as it's completed
    storage.local(infile, outfile) # this command stores the content of the temporary file locally
    with open(outfile.name, 'rb') as f:
        assert f.read() == b'Testing' # this 'asserts' that the contents written in the infile match with the outfile