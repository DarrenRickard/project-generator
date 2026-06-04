# June 1, 2026

from pathlib import Path
# from rich import print
# from rich.console import Console
import argparse
import json

folder_structure_path = Path('config/structure_cfg.json')

# Initialize argument parser
parser = argparse.ArgumentParser(
    prog='projgen', 
    usage='%(prog)s [options]',
    description='A project generator tool that creates a new project based on a template and user input.',
    epilog='Example usage: projgen --test'
    )

parser.add_argument('--test', action='store_true', help='Run in test mode')
parser.add_argument('--json', action='store_true', help='Check the loaded JSON configuration file')
args = parser.parse_args()

def get_project_name():
    try:
        project_name = input("Enter the project name: ")
        Path(project_name).mkdir(exist_ok=False) # Throws FileExistsError if the directory already exists
        project_root = Path(project_name)
        return project_name, project_root
    except FileExistsError:
        print(f"Directory '{project_name}' already exists. Please choose a different project name or remove it before running the script.")
        exit(1)

# Load folder structure from JSON config file
def load_folder_structure(): 
    with open(folder_structure_path, 'r') as f:
        return json.load(f)

# Folder structures loaded from JSON config file
folder_structures = load_folder_structure()


# Create project folders
def create_folders(base_path: Path, structure: dict):
    for folder_name, subfolders in structure.items():
        folder_path = base_path / folder_name
        folder_path.mkdir(exist_ok=True)

        create_folders(folder_path, subfolders)

# Run tests
def run_tests():
    print("Running tests...")

def check_json():
    print("Checking JSON configuration...\n")
    print(folder_structures)

# Run normal code
def run_normal():
    print("Running normal code...")
    project_name, project_root = get_project_name()
    selected_structure = input(f"Select a folder structure from the following options: {list(folder_structures.keys())}: ")
    # Add test code here
    try:
        print(f"Creating folder structure for project: '{project_name}'...")
        create_folders(project_root, folder_structures[selected_structure])
        print(f"Created folder structure in {project_root}")
    except Exception as e:
        print(f"Error creating folder structure: {e}")
        return False

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
    elif args.json:
        check_json()
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