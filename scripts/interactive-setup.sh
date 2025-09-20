#!/usr/bin/env python3
"""
Interactive Automanic Setup

Guides users through configuration and setup process.
"""

import os
import sys
from typing import Dict, List, Tuple

class InteractiveSetup:
    """Interactive setup wizard for Automanic"""
    
    def __init__(self):
        self.config = {}
        self.questions = self._define_questions()
        
    def _define_questions(self) -> List[Tuple[str, str, List[str]]]:
        """Define configuration questions"""
        return [
            (
                "PROJECT_TYPE",
                "What type of project are you creating?",
                [
                    "web-app - Web application with frontend/backend",
                    "cli-tool - Command line interface tool",
                    "library - Reusable code library/package",
                    "api - REST API service",
                    "mobile-app - Mobile application",
                    "desktop-app - Desktop application",
                    "data-science - Data science/ML project",
                    "documentation - Documentation site"
                ]
            ),
            (
                "LANGUAGE",
                "What programming language will you use?",
                [
                    "python - Python",
                    "javascript - JavaScript",
                    "typescript - TypeScript", 
                    "go - Go",
                    "rust - Rust",
                    "java - Java",
                    "cpp - C++",
                    "c - C",
                    "php - PHP",
                    "ruby - Ruby",
                    "swift - Swift",
                    "kotlin - Kotlin",
                    "scala - Scala",
                    "r - R"
                ]
            ),
            (
                "FRAMEWORK",
                "Which framework will you use (if any)?",
                [
                    "react - React (JavaScript/TypeScript)",
                    "vue - Vue.js (JavaScript/TypeScript)",
                    "angular - Angular (TypeScript)",
                    "express - Express.js (Node.js)",
                    "fastapi - FastAPI (Python)",
                    "django - Django (Python)",
                    "spring - Spring Boot (Java)",
                    "gin - Gin (Go)",
                    "actix - Actix Web (Rust)",
                    "electron - Electron (Desktop)",
                    "flutter - Flutter (Mobile)",
                    "pytorch - PyTorch (ML)",
                    "tensorflow - TensorFlow (ML)",
                    "none - No framework"
                ]
            ),
            (
                "BUILD_SYSTEM",
                "What build system will you use?",
                [
                    "npm - npm (Node.js)",
                    "yarn - Yarn (Node.js)",
                    "pip - pip (Python)",
                    "cargo - Cargo (Rust)",
                    "maven - Maven (Java)",
                    "gradle - Gradle (Java/Kotlin)",
                    "make - Make",
                    "cmake - CMake",
                    "none - No build system"
                ]
            ),
            (
                "DATABASE",
                "What database will you use?",
                [
                    "postgresql - PostgreSQL",
                    "mysql - MySQL",
                    "mongodb - MongoDB",
                    "redis - Redis",
                    "sqlite - SQLite",
                    "none - No database"
                ]
            ),
            (
                "DEPLOYMENT",
                "How will you deploy your project?",
                [
                    "docker - Docker containers",
                    "kubernetes - Kubernetes",
                    "aws - Amazon Web Services",
                    "gcp - Google Cloud Platform",
                    "azure - Microsoft Azure",
                    "vercel - Vercel",
                    "netlify - Netlify",
                    "heroku - Heroku",
                    "none - No deployment automation"
                ]
            ),
            (
                "CI_CD",
                "What CI/CD system will you use?",
                [
                    "github-actions - GitHub Actions",
                    "jenkins - Jenkins",
                    "gitlab-ci - GitLab CI",
                    "circleci - CircleCI",
                    "travis-ci - Travis CI",
                    "none - No CI/CD"
                ]
            ),
            (
                "TESTING",
                "What testing framework will you use?",
                [
                    "jest - Jest (JavaScript/TypeScript)",
                    "pytest - pytest (Python)",
                    "cargo-test - cargo test (Rust)",
                    "junit - JUnit (Java)",
                    "go-test - go test (Go)",
                    "rspec - RSpec (Ruby)",
                    "none - No testing framework"
                ]
            ),
            (
                "LICENSE_TYPE",
                "What license will you use?",
                [
                    "mit - MIT License (permissive)",
                    "apache-2.0 - Apache License 2.0",
                    "gpl-v3 - GPL v3 (copyleft)",
                    "bsd-3-clause - BSD 3-Clause",
                    "unlicense - Unlicense (public domain)",
                    "proprietary - Proprietary/Closed source"
                ]
            ),
            (
                "VISIBILITY",
                "Will this be a public or private repository?",
                [
                    "public - Public repository",
                    "private - Private repository"
                ]
            )
        ]
        
    def run_interactive_setup(self):
        """Run the interactive setup process"""
        print("🚀 Welcome to Automanic Interactive Setup!")
        print("=" * 50)
        print("This wizard will help you configure your project.")
        print("You can press Ctrl+C at any time to cancel.\n")
        
        try:
            # Collect configuration
            for key, question, options in self.questions:
                self.config[key] = self._ask_question(key, question, options)
                
            # Show summary
            self._show_summary()
            
            # Confirm and generate
            if self._confirm_generation():
                self._generate_readme()
                self._run_setup()
                
        except KeyboardInterrupt:
            print("\n\n❌ Setup cancelled by user.")
            sys.exit(1)
        except Exception as e:
            print(f"\n❌ Error during setup: {e}")
            sys.exit(1)
            
    def _ask_question(self, key: str, question: str, options: List[str]) -> str:
        """Ask a single configuration question"""
        print(f"\n📋 {question}")
        print("-" * 40)
        
        # Display options with numbers
        for i, option in enumerate(options, 1):
            print(f"{i:2d}. {option}")
            
        while True:
            try:
                choice = input(f"\nEnter your choice (1-{len(options)}): ").strip()
                
                if not choice:
                    print("Please enter a number.")
                    continue
                    
                choice_num = int(choice)
                if 1 <= choice_num <= len(options):
                    # Extract just the key part (before the dash)
                    selected = options[choice_num - 1].split(' - ')[0]
                    print(f"✅ Selected: {selected}")
                    return selected
                else:
                    print(f"Please enter a number between 1 and {len(options)}.")
                    
            except ValueError:
                print("Please enter a valid number.")
            except KeyboardInterrupt:
                raise
                
    def _show_summary(self):
        """Show configuration summary"""
        print("\n" + "=" * 50)
        print("📋 CONFIGURATION SUMMARY")
        print("=" * 50)
        
        for key, value in self.config.items():
            print(f"{key:15s}: {value}")
            
        print("=" * 50)
        
    def _confirm_generation(self) -> bool:
        """Confirm before generating project"""
        while True:
            confirm = input("\n✨ Generate project with this configuration? (y/n): ").strip().lower()
            if confirm in ['y', 'yes']:
                return True
            elif confirm in ['n', 'no']:
                print("❌ Setup cancelled.")
                return False
            else:
                print("Please enter 'y' or 'n'.")
                
    def _generate_readme(self):
        """Generate README.md with configuration"""
        readme_content = f'''# Your Project Name

<!-- AUTOMANIC-CONFIG-START -->
PROJECT_TYPE: {self.config["PROJECT_TYPE"]}
LANGUAGE: {self.config["LANGUAGE"]}
FRAMEWORK: {self.config["FRAMEWORK"]}
BUILD_SYSTEM: {self.config["BUILD_SYSTEM"]}
DATABASE: {self.config["DATABASE"]}
DEPLOYMENT: {self.config["DEPLOYMENT"]}
CI_CD: {self.config["CI_CD"]}
TESTING: {self.config["TESTING"]}
LICENSE_TYPE: {self.config["LICENSE_TYPE"]}
VISIBILITY: {self.config["VISIBILITY"]}
<!-- AUTOMANIC-CONFIG-END -->

## Description

Brief description of your project goes here.

## Features

- Feature 1
- Feature 2
- Feature 3

## Requirements

List your project requirements here.

## Installation

```bash
# Add installation instructions
```

## Usage

```bash
# Add usage examples
```

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the {self.config["LICENSE_TYPE"]} License - see the [LICENSE](LICENSE) file for details.
'''

        with open('README.md', 'w') as f:
            f.write(readme_content)
            
        print("✅ Generated README.md with your configuration")
        
    def _run_setup(self):
        """Run the main setup script"""
        print("\n🏗️  Running project setup...")
        
        try:
            # Import and run the main setup logic
            import subprocess
            
            # Run the structure generation
            result = subprocess.run([
                sys.executable, 
                'scripts/generate-structure.py', 
                '--config-file', 'README.md'
            ], capture_output=True, text=True)
            
            if result.returncode != 0:
                print(f"❌ Error running structure generation: {result.stderr}")
                return
                
            print("✅ Project structure generated successfully!")
            print("\n🎉 Setup Complete!")
            print("\nNext steps:")
            print("1. Review and customize the generated files")
            print("2. Initialize git repository if needed: git init")
            print("3. Install dependencies")
            print("4. Start developing!")
            
        except Exception as e:
            print(f"❌ Error running setup: {e}")

def main():
    setup = InteractiveSetup()
    setup.run_interactive_setup()

if __name__ == "__main__":
    main()