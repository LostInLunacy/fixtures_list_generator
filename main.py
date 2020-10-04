""" Generates and prints a list of fixtures, 
given the name of txt file containing the teams. """

# Imports
import argparse
from time import sleep
from random import shuffle

# Local Imports
from fixtures import FixtureListGenerator

def get_teams(file_name):
    """ Get teams from file. """
    try:
        with open(file_name) as tf:
            # Strip each line to get rid of \n
            teams = [l.strip() for l in tf.readlines()]
    except FileNotFoundError:
        print("Unable to locate file. Please try again!")
        sleep(4) # Allow user time to read above message
        quit()
    else:
        return teams

def main():
    parser = argparse.ArgumentParser(
        description="Fixtures List Generator"
    )

    # Add parameters
    parser.add_argument('file_name', help="team list")

    # Parse the args
    args = parser.parse_args()

    # Get file_name
    file_name = args.file_name

    # Ensure txt extension added
    if file_name[-4:] != '.txt': file_name += '.txt'

    teams = get_teams(file_name)
    shuffle(teams)

    fixgen = FixtureListGenerator(teams)
    fixgen()
    fixgen.print_fixtures_list()


if __name__ == "__main__":
    main()
