# Defining the dump function
import subprocess

def dump(url):
    pass subprocess.Popen(['pg_dump', url], stdout=subprocess.PIPE)