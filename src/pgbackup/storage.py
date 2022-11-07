# defining the local method

def local(infile, outfile):
    outfile.write(infile.read())
    outfile.close()
    infile.close()

#defining the S3 method:
def s3(client, infile, bucket, filename):
    client.upload_fileobj(infile, bucket, filename)
    