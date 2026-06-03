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

# Test folder structure
try:
    project_name = input("Enter the project name: ")
    Path(project_name).mkdir(exist_ok=False) # Throws FileExistsError if the directory already exists
    project_root = Path(project_name)
except FileExistsError:
    print(f"Directory '{project_name}' already exists. Please choose a different project name or remove it before running the script.")
    exit(1)

# Temporary folder structure for testing. Implement JSON config file later.
folder_structure = {
    "src": {
        "core": {},
        "utils": {},
        "models": {}
    },
    "tests": {
        "unit": {},
        "integration": {}
    },
    "docs": {},
    "config": {},
    "data": {
        "input": {},
        "output": {}
    }
}


# Create project folders
def create_folders(base_path: Path, structure: dict):
    for folder_name, subfolders in structure.items():
        folder_path = base_path / folder_name
        folder_path.mkdir(exist_ok=True)

        create_folders(folder_path, subfolders)

# Load project configuration from JSON file
def load_config():
    # get the path to config.json
    return

# Run tests
def run_tests():
    print("Running tests...")
    # Add test code here
    try:
        create_folders(project_root, folder_structure)
        print(f"Created folder structure in {project_root}")
    except Exception as e:
        print(f"Error creating folder structure: {e}")
        return False

    return True

# Run normal code
def run_normal():
    print("Running normal code...")
    # Add normal code here
    return True

# Define Main function
def main():
    if args.test:
        print("Running in test mode...")
        # Add test code 
        if run_tests():
            print("Tests passed successfully!")
        else:
            print("Tests failed.")
    else:
        print("Running in normal mode...")
        # Add normal code 
        if run_normal():
            print("Normal code executed successfully!")
        else:
            print("Normal code execution failed.")

# Run Main function
if __name__ == '__main__':
    main()