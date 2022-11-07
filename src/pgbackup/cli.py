# CLI script
# Defining the 'create parser function'
from argparse import Action, ArgumentParser

known_drivers = ['local', 's3']

class DriverAction(Action): # the 'class' keyword is used to define a class. Classes should use Uppercase letters
    def __call__(self, parser, namespace, values,option_string=None):
        driver, destination = values
        if driver.lower() not in known_drivers:
            parser.error("Unknown driver. Available drivers are 'local' and 's3'") 
        namespace.driver = driver.lower()
        namespace.destination = destination
    # 'self' is what makes a 'method' a method. In this case, self will be the instance of the object in which the '__call__' method is being called on 
        

def create_parser():
    parser = ArgumentParser()
    parser.add_argument('url', help="URL of the PostgreSQL database to backup")
    parser.add_argument('--driver',
                help="how and where to store the backup",
                nargs=2, # this defines the number of arguments that we'll be parsing
                action=DriverAction,
                required=True
    )
    return parser 

# This function defines the entire script implementation
def main():
    import boto3
    from pgbackup import pgdump, storage

    args = create_parser().parse_args()
    dump = pgdump.dump(args.url)
    if args.driver == 's3':
        client = boto3.client('s3')
        storage.s3(client, dump.stdout, args.destination, 'example.sql')
    else:
        outfile = open(args.destination, 'wb')
        storage.local(dump.stdout, outfile)    
