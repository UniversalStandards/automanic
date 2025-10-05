```python
import os
import re
import json

# Constants for folder structure
FOLDER_STRUCTURE = {
    "web-app": ["src", "public", "docs", ".github/workflows"],
    "cli-tool": ["src", "docs", ".github/workflows"],
    "library": ["src", "tests", "docs", ".github/workflows"],
    "api": ["src", "tests", "docs", ".github/workflows"],
    "mobile-app": ["src", "assets", "docs", ".github/workflows"],
    "desktop-app": ["src", "resources", "docs", ".github/workflows"],
    "data-science": ["notebooks", "data", "models", ".github/workflows"],
    "documentation": ["docs", ".github/workflows"]
}

# Function to parse the README.md file for configuration
def parse_readme(readme_path):
    config = {}
    with open(readme_path, 'r') as file:
        content = file.read()
        # Use regex to extract configuration details
        try:
            config["project_type"] = re.search(r"PROJECT_TYPE:\s*\[([^\]]+)\]", content).group(1).split("|")
            config["language"] = re.search(r"LANGUAGE:\s*\[([^\]]+)\]", content).group(1).split("|")
            config["framework"] = re.search(r"FRAMEWORK:\s*\[([^\]]+)\]", content).group(1).split("|")
            config["build_system"] = re.search(r"BUILD_SYSTEM:\s*\[([^\]]+)\]", content).group(1).split("|")
            config["database"] = re.search(r"DATABASE:\s*\[([^\]]+)\]", content).group(1).split("|")
        except AttributeError:
            print("Error: One or more required fields are missing in the README.md.")
            exit(1)
    return config

# Function to generate folder structure based on project type
def generate_structure(project_type):
    project_folder = "automanic-project"
    os.makedirs(project_folder, exist_ok=True)

    folders = FOLDER_STRUCTURE.get(project_type.lower(), [])
    for folder in folders:
        os.makedirs(os.path.join(project_folder, folder), exist_ok=True)
        print(f"Created: {os.path.join(project_folder, folder)}")

    # Create additional files in the project root
    with open(os.path.join(project_folder, 'README.md'), 'w') as readme_file:
        readme_file.write("# Project Documentation\n\nThis is the documentation for your project.")
        print(f"Created documentation template at: {os.path.join(project_folder, 'README.md')}")

# Function to prompt user for input in CLI
def interactive_setup():
    print("Welcome to the Automanic Setup Wizard!")
    project_type = input("Enter your project type (web-app, cli-tool, library, api, mobile-app, desktop-app, data-science, documentation): ")
    language = input("Enter your programming language (python, javascript, etc.): ")
    framework = input("Enter your framework (react, vue, etc.): ")
    build_system = input("Enter your build system (npm, pip, etc.): ")
    database = input("Enter your database (postgresql, mysql, etc.): ")

    config = {
        "PROJECT_TYPE": project_type,
        "LANGUAGE": language,
        "FRAMEWORK": framework,
        "BUILD_SYSTEM": build_system,
        "DATABASE": database
    }

    # Save configuration to a JSON file for further processing
    with open('project_config.json', 'w') as json_file:
        json.dump(config, json_file, indent=4)
    
    print("Configuration saved to project_config.json.")

# Main setup function
def main():
    print("Choose your setup method:")
    print("1. Upload the provided README.md template")
    print("2. Follow the prompts in the CLI walkthrough")
    print("3. Use the Interactive Webpage GUI (not implemented in CLI)")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == "1":
        readme_path = input("Enter the path to your README.md file: ")
        if os.path.exists(readme_path):
            config = parse_readme(readme_path)
            project_type = config.get("project_type")[0]  # Use the first project type as default
        else:
            print("README.md not found! Please check the path.")
            return
    elif choice == "2":
        interactive_setup()
        return
    elif choice == "3":
        print("Please use the web interface for this option.")
        return
    else:
        print("Invalid choice! Exiting.")
        return

    print(f"Setting up project of type: {project_type}")
    
    generate_structure(project_type)
    print("Setup complete! Your project structure has been generated.")

if __name__ == "__main__":
    main()
