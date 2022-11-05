# test script
import pytest
from pgbackup   import cli 

url = "postgres://bob:password@example.com:5432/db_one"

@pytest.fixture
def parser():
    return cli.create_parser()

def test_parser_without_driver(parser):
    """
    Without a specified driver the parser will exit
    """
    with pytest.raises(SystemExit):
        parser.parse_args([url])

def test_parser_with_driver(parser):
    """
    The parser will exit if it receives a driver without a destination
    """
    with pytest.raises(SystemExit):
        parser.parse_args([url, "--driver", "local"])

def test_parser_with_unkown_driver(parser):
    """
    The parser will exit if the driver name is unknown.
    """

    with pytest.raises(SystemExit):
        parser.parse_args([url, '--driver', 'azure', 'destination'])

def test_parser_with_known_drivers(parser):
    """
    The parser will not exit if the driver name is known
    """

    # creating a list to store the 2 different driver names that we want to accept, so we can iterate through the list and make our assertions multiple times, just substituting the value for our known drivers
    for driver in ['local', 's3']:
        assert parser.parse_args([url, '--driver', driver, 'destination'])

def test_parser_with_driver_and_destination(parser):
    """
    The parser will not exit if it receives a driver and destination
    """

    args = parser.parse_args([url, '--driver', 'local', '/some/path'])

    assert args.url == url # The 'assert' key word makes sure that the attributes that are set on the 'parser' or the 'args'are going to match what we expect
    assert args.driver == 'local'
    assert args.destination == '/some/path'