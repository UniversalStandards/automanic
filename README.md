# Automanic - Advanced Automated Repository Management Template

Automanic is a comprehensive template repository system designed to streamline the setup and management of software projects. It automatically determines the required file and folder structure, repository type, and settings based on user-provided specifications in a `README.md` file or through interactive methods. This tool provides complete automation for GitHub operations including issues, pull requests, reviews, commits, and merges, allowing developers to focus on coding rather than configuration.

## 🚀 Quick Start

Follow these steps to get started with Automanic:

1. **Clone this repository**:
   - Clone the Automanic repository to your local machine.
   ```bash
   git clone https://github.com/your-username/automanic.git
   cd automanic
Install dependencies:

For Python projects:
Copy
pip install -r requirements.txt
For Node.js projects:
Copy
npm install
Choose your setup method:

Option 1: Upload the provided README.md template: Upload your project README.md with the required fields (see Template Format below).
Option 2: Follow the prompts in the CLI walkthrough: Execute the provided setup.py script to interactively configure your project.
Option 3: Use our Interactive Webpage GUI: An interactive webpage will guide you through the setup process, allowing you to upload the README.md directly to the repository or generate it for later use.
Run the setup script:

Execute the provided setup.py script to create the user project structure.
Copy
python setup.py
Customize as needed.

Modify the generated files and folders according to your project requirements.
📋 Template Format for User README.md
When uploading your README.md, include these REQUIRED fields in the specified format. This configuration will guide Automanic in generating the appropriate project structure.

Copy
<!-- AUTOMANIC-CONFIG-START -->
PROJECT_TYPE: [web-app|cli-tool|library|api|mobile-app|desktop-app|data-science|documentation]
LANGUAGE: [python|javascript|typescript|go|rust|java|cpp|c|php|ruby|swift|kotlin|scala|r]
FRAMEWORK: [react|vue|angular|express|fastapi|django|spring|gin|actix|electron|flutter|pytorch|tensorflow|none]
BUILD_SYSTEM: [npm|yarn|pip|cargo|maven|gradle|make|cmake|none]
DATABASE: [postgresql|mysql|mongodb|redis|sqlite|none]
<!-- AUTOMANIC-CONFIG-END -->
Example
Here’s an example of how your README.md might look:

Copy
<!-- AUTOMANIC-CONFIG-START -->
PROJECT_TYPE: web-app
LANGUAGE: javascript
FRAMEWORK: react
BUILD_SYSTEM: npm
DATABASE: mongodb
<!-- AUTOMANIC-CONFIG-END -->
🛠️ Features
Automated Repository Setup:

Automatically generates folder structures based on project type.
Configures repository settings such as branch protection rules.
Three Configuration Options:

Upload the provided README.md template: Users can upload a predefined template file with necessary configurations.
Follow the prompts in the CLI walkthrough: Users can interactively enter project details through the command line.
Use our Interactive Webpage GUI: Users can fill out a web form that collects project details and automatically uploads the README.md or generates it for later use.
File Upload Option:

Users can upload a README.md template with placeholders.
The system intelligently fills in defaults or requests additional information as needed.
AI Integration:

Integrates with free AI tools (e.g., GitHub Copilot, OpenAI models) to assist users in generating code snippets or completing configurations based on their input.
Offers suggestions for best practices and optimizations during setup.
Enhanced Project Setup:

Configures additional files such as .env, Dockerfile, and CI/CD pipeline configurations based on user input.
Initializes databases and sets up connection strings if applicable.
GitHub Actions Integration:

Preconfigured workflows for CI/CD pipelines.
Automated testing, linting, and deployment based on project type.
Issue and Pull Request Management:

Automatically generates issue templates and pull request templates.
Supports auto-labeling and assignment of issues based on predefined rules.
Code Review Automation:

Automatically assigns reviewers based on file ownership or expertise.
Provides automated feedback using linting tools and code quality checks.
Commit and Merge Automation:

Automatically merges approved pull requests based on defined criteria.
Enforces commit message guidelines to maintain project consistency.
📂 Folder Structure
Automanic will generate the following folder structure within a dedicated project folder named automanic-project:

Copy
automanic-project/
├── src/                # Source code directory
├── tests/              # Unit tests directory
├── docs/               # Documentation files
├── .github/            # GitHub-specific files (actions, templates)
│   ├── workflows/      # CI/CD workflows
│   ├── issue_templates/ # Issue templates
│   └── pull_request_templates/ # Pull request templates
├── requirements.txt    # Dependencies for Python projects
├── package.json        # Dependencies for Node.js projects
├── Dockerfile          # Docker configuration (if applicable)
├── .gitignore          # Git ignore file
├── .env                # Environment variables configuration
└── README.md           # Project documentation
🔧 Additional Notes
Ensure that your README.md follows the exact format specified above for successful parsing.
You can customize the FOLDER_STRUCTURE dictionary in the setup.py to add or modify folder structures for specific project types.
For advanced customization, consider integrating with GitHub APIs to automate repository settings directly.
🤝 Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

