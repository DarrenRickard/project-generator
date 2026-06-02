# June 1, 2026

from pathlib import Path
# from rich import print
# from rich.console import Console
import argparse
# import json

# Initialize argument parser
parser = argparse.ArgumentParser(
    prog='projgen', 
    usage='%(prog)s [options]',
    description='A project generator tool that creates a new project based on a template and user input.',
    epilog='Example usage: projgen --test'
    )

parser.add_argument('--test', action='store_true', help='Run in test mode')
args = parser.parse_args()

# Define Main function
def main():
    if args.test:
        print("Running in test mode...")
        # Add test code 
    else:
        print("Running in normal mode...")
        # Add normal code 

# Run Main function
if __name__ == '__main__':
    main()