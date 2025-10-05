#!/usr/bin/env python3
"""
Automanic Structure Generator

Parses README.md configuration and generates appropriate project structure.
"""

import os
import re
import sys
import json
import argparse
from pathlib import Path
from typing import Dict, List, Optional

class AutomanicConfig:
    """Handles parsing and validation of Automanic configuration from README.md"""
    
    REQUIRED_FIELDS = [
        'PROJECT_TYPE', 'LANGUAGE', 'FRAMEWORK', 'BUILD_SYSTEM',
        'DATABASE', 'DEPLOYMENT', 'CI_CD', 'TESTING', 'LICENSE_TYPE', 'VISIBILITY'
    ]
    
    VALID_VALUES = {
        'PROJECT_TYPE': ['web-app', 'cli-tool', 'library', 'api', 'mobile-app', 'desktop-app', 'data-science', 'documentation'],
        'LANGUAGE': ['python', 'javascript', 'typescript', 'go', 'rust', 'java', 'cpp', 'c', 'php', 'ruby', 'swift', 'kotlin', 'scala', 'r'],
        'FRAMEWORK': ['react', 'vue', 'angular', 'express', 'fastapi', 'django', 'spring', 'gin', 'actix', 'electron', 'flutter', 'pytorch', 'tensorflow', 'none'],
        'BUILD_SYSTEM': ['npm', 'yarn', 'pip', 'cargo', 'maven', 'gradle', 'make', 'cmake', 'none'],
        'DATABASE': ['postgresql', 'mysql', 'mongodb', 'redis', 'sqlite', 'none'],
        'DEPLOYMENT': ['docker', 'kubernetes', 'aws', 'gcp', 'azure', 'vercel', 'netlify', 'heroku', 'none'],
        'CI_CD': ['github-actions', 'jenkins', 'gitlab-ci', 'circleci', 'travis-ci', 'none'],
        'TESTING': ['jest', 'pytest', 'cargo-test', 'junit', 'go-test', 'rspec', 'none'],
        'LICENSE_TYPE': ['mit', 'apache-2.0', 'gpl-v3', 'bsd-3-clause', 'unlicense', 'proprietary'],
        'VISIBILITY': ['public', 'private']
    }
    
    def __init__(self):
        self.config = {}
        
    def parse_readme(self, readme_path: str) -> Dict[str, str]:
        """Parse configuration from README.md file"""
        try:
            with open(readme_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except FileNotFoundError:
            raise Exception(f"README.md not found at {readme_path}")
            
        # Extract configuration block
        config_pattern = r'<!-- AUTOMANIC-CONFIG-START -->(.*?)<!-- AUTOMANIC-CONFIG-END -->'
        match = re.search(config_pattern, content, re.DOTALL)
        
        if not match:
            raise Exception("Automanic configuration block not found in README.md")
            
        config_block = match.group(1)
        
        # Parse key-value pairs
        config = {}
        for line in config_block.split('\n'):
            line = line.strip()
            if ':' in line and not line.startswith('<!--'):
                key, value = line.split(':', 1)
                key = key.strip()
                value = value.strip(' []')
                if key in self.REQUIRED_FIELDS:
                    config[key] = value
                    
        # Validate configuration
        self._validate_config(config)
        self.config = config
        return config
        
    def _validate_config(self, config: Dict[str, str]):
        """Validate configuration values"""
        missing_fields = [field for field in self.REQUIRED_FIELDS if field not in config]
        if missing_fields:
            raise Exception(f"Missing required fields: {', '.join(missing_fields)}")
            
        for key, value in config.items():
            if key in self.VALID_VALUES and value not in self.VALID_VALUES[key]:
                raise Exception(f"Invalid value '{value}' for field '{key}'. Valid values: {', '.join(self.VALID_VALUES[key])}")

class StructureGenerator:
    """Generates project structure based on configuration"""
    
    def __init__(self, config: Dict[str, str]):
        self.config = config
        self.base_path = Path.cwd()
        
    def generate_structure(self):
        """Generate complete project structure"""
        print(f"🏗️  Generating structure for {self.config['PROJECT_TYPE']} using {self.config['LANGUAGE']}")
        
        # Create base directories
        self._create_base_directories()
        
        # Generate language-specific files
        self._generate_language_files()
        
        # Generate framework-specific files
        self._generate_framework_files()
        
        # Generate build system files
        self._generate_build_files()
        
        # Generate testing files
        self._generate_testing_files()
        
        # Generate deployment files
        self._generate_deployment_files()
        
        # Generate documentation
        self._generate_documentation()
        
        # Generate configuration files
        self._generate_config_files()
        
        print("✅ Project structure generated successfully!")
        
    def _create_base_directories(self):
        """Create base directory structure"""
        project_type = self.config['PROJECT_TYPE']
        language = self.config['LANGUAGE']
        
        # Common directories
        dirs = ['src', 'tests', 'docs', 'scripts', '.github/workflows', '.github/ISSUE_TEMPLATE']
        
        # Project type specific directories
        if project_type == 'web-app':
            dirs.extend(['public', 'assets', 'components'])
        elif project_type == 'cli-tool':
            dirs.extend(['cmd', 'internal'])
        elif project_type == 'library':
            dirs.extend(['examples', 'benchmarks'])
        elif project_type == 'api':
            dirs.extend(['api', 'internal', 'pkg'])
        elif project_type == 'data-science':
            dirs.extend(['data', 'notebooks', 'models', 'reports'])
            
        # Language specific directories
        if language == 'python':
            dirs.extend(['requirements'])
        elif language in ['javascript', 'typescript']:
            dirs.extend(['node_modules'])
        elif language == 'go':
            dirs.extend(['cmd', 'internal', 'pkg'])
        elif language == 'rust':
            dirs.extend(['target'])
        elif language == 'java':
            dirs.extend(['src/main/java', 'src/test/java', 'src/main/resources'])
            
        for dir_path in dirs:
            os.makedirs(dir_path, exist_ok=True)
            
        print(f"📁 Created {len(dirs)} directories")
        
    def _generate_language_files(self):
        """Generate language-specific files"""
        language = self.config['LANGUAGE']
        
        if language == 'python':
            self._create_python_files()
        elif language in ['javascript', 'typescript']:
            self._create_js_files()
        elif language == 'go':
            self._create_go_files()
        elif language == 'rust':
            self._create_rust_files()
        elif language == 'java':
            self._create_java_files()
            
    def _create_python_files(self):
        """Create Python-specific files"""
        # requirements.txt
        requirements = [
            "# Production dependencies",
            "requests>=2.28.0",
            "click>=8.0.0",
            "",
            "# Development dependencies",
            "pytest>=7.0.0",
            "black>=22.0.0",
            "flake8>=5.0.0",
            "mypy>=0.991"
        ]
        
        if self.config['FRAMEWORK'] == 'fastapi':
            requirements.insert(1, "fastapi>=0.100.0")
            requirements.insert(2, "uvicorn[standard]>=0.20.0")
        elif self.config['FRAMEWORK'] == 'django':
            requirements.insert(1, "django>=4.2.0")
            
        with open('requirements.txt', 'w') as f:
            f.write('\n'.join(requirements))
            
        # setup.py
        setup_py = '''from setuptools import setup, find_packages

setup(
    name="your-project",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.28.0",
    ],
    python_requires=">=3.8",
    author="Your Name",
    author_email="your.email@example.com",
    description="A brief description of your project",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/your-project",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
'''
        with open('setup.py', 'w') as f:
            f.write(setup_py)
            
        # pyproject.toml
        pyproject = '''[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "your-project"
version = "0.1.0"
description = "A brief description of your project"
readme = "README.md"
requires-python = ">=3.8"
dependencies = [
    "requests>=2.28.0",
]

[tool.black]
line-length = 88
target-version = ['py38']

[tool.mypy]
python_version = "3.8"
warn_return_any = true
warn_unused_configs = true
'''
        with open('pyproject.toml', 'w') as f:
            f.write(pyproject)
            
    def _create_js_files(self):
        """Create JavaScript/TypeScript files"""
        package_json = {
            "name": "your-project",
            "version": "1.0.0",
            "description": "A brief description of your project",
            "main": "src/index.js",
            "scripts": {
                "start": "node src/index.js",
                "dev": "nodemon src/index.js",
                "test": "jest",
                "build": "webpack --mode=production",
                "lint": "eslint src/"
            },
            "dependencies": {},
            "devDependencies": {
                "jest": "^29.0.0",
                "eslint": "^8.0.0",
                "nodemon": "^3.0.0"
            }
        }
        
        if self.config['LANGUAGE'] == 'typescript':
            package_json["main"] = "dist/index.js"
            package_json["scripts"]["build"] = "tsc"
            package_json["scripts"]["dev"] = "ts-node src/index.ts"
            package_json["devDependencies"]["typescript"] = "^5.0.0"
            package_json["devDependencies"]["ts-node"] = "^10.0.0"
            package_json["devDependencies"]["@types/node"] = "^20.0.0"
            
        if self.config['FRAMEWORK'] == 'react':
            package_json["dependencies"]["react"] = "^18.0.0"
            package_json["dependencies"]["react-dom"] = "^18.0.0"
            
        with open('package.json', 'w') as f:
            json.dump(package_json, f, indent=2)
            
    def _create_go_files(self):
        """Create Go-specific files"""
        go_mod = f'''module your-project

go 1.21

require (
    github.com/gorilla/mux v1.8.0
    github.com/spf13/cobra v1.7.0
)
'''
        with open('go.mod', 'w') as f:
            f.write(go_mod)
            
    def _create_rust_files(self):
        """Create Rust-specific files"""
        cargo_toml = '''[package]
name = "your-project"
version = "0.1.0"
edition = "2021"

[dependencies]
clap = { version = "4.0", features = ["derive"] }
tokio = { version = "1", features = ["full"] }
serde = { version = "1.0", features = ["derive"] }
serde_json = "1.0"

[dev-dependencies]
criterion = "0.5"
'''
        with open('Cargo.toml', 'w') as f:
            f.write(cargo_toml)
            
    def _create_java_files(self):
        """Create Java-specific files"""
        if self.config['BUILD_SYSTEM'] == 'maven':
            pom_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    
    <groupId>com.example</groupId>
    <artifactId>your-project</artifactId>
    <version>1.0.0</version>
    <packaging>jar</packaging>
    
    <properties>
        <maven.compiler.source>17</maven.compiler.source>
        <maven.compiler.target>17</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>
    
    <dependencies>
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <version>4.13.2</version>
            <scope>test</scope>
        </dependency>
    </dependencies>
</project>
'''
            with open('pom.xml', 'w') as f:
                f.write(pom_xml)
                
    def _generate_framework_files(self):
        """Generate framework-specific files"""
        # Implementation for framework-specific files would go here
        pass
        
    def _generate_build_files(self):
        """Generate build system files"""
        # Implementation for build-specific files would go here
        pass
        
    def _generate_testing_files(self):
        """Generate testing configuration files"""
        # Implementation for testing files would go here
        pass
        
    def _generate_deployment_files(self):
        """Generate deployment configuration files"""
        if self.config['DEPLOYMENT'] == 'docker':
            self._create_dockerfile()
            
    def _create_dockerfile(self):
        """Create Dockerfile based on language"""
        language = self.config['LANGUAGE']
        
        dockerfiles = {
            'python': '''FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "src/main.py"]
''',
            'javascript': '''FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm ci --only=production

COPY . .

EXPOSE 3000

CMD ["npm", "start"]
''',
            'go': '''FROM golang:1.21-alpine AS builder

WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download

COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -o main .

FROM alpine:latest
RUN apk --no-cache add ca-certificates
WORKDIR /root/

COPY --from=builder /app/main .

CMD ["./main"]
'''
        }
        
        if language in dockerfiles:
            with open('Dockerfile', 'w') as f:
                f.write(dockerfiles[language])
                
    def _generate_documentation(self):
        """Generate documentation structure"""
        # Implementation for documentation files would go here
        pass
        
    def _generate_config_files(self):
        """Generate configuration files like .gitignore, .editorconfig"""
        self._create_gitignore()
        self._create_editorconfig()
        
    def _create_gitignore(self):
        """Create .gitignore based on language and framework"""
        language = self.config['LANGUAGE']
        
        gitignore_templates = {
            'python': '''# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# PyInstaller
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/
.pytest_cache/

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db
''',
            'javascript': '''# Dependencies
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Runtime data
pids
*.pid
*.seed
*.pid.lock

# Coverage directory used by tools like istanbul
coverage/

# Build outputs
dist/
build/

# Environment variables
.env
.env.local
.env.development.local
.env.test.local
.env.production.local

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db
''',
            'go': '''# Binaries for programs and plugins
*.exe
*.exe~
*.dll
*.so
*.dylib

# Test binary, built with `go test -c`
*.test

# Output of the go coverage tool
*.out

# Dependency directories
vendor/

# Go workspace file
go.work

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db
''',
            'rust': '''# Generated by Cargo
/target/

# Remove Cargo.lock from gitignore if creating an executable
Cargo.lock

# These are backup files generated by rustfmt
**/*.rs.bk

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db
'''
        }
        
        if language in gitignore_templates:
            with open('.gitignore', 'w') as f:
                f.write(gitignore_templates[language])
                
    def _create_editorconfig(self):
        """Create .editorconfig"""
        editorconfig = '''root = true

[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true
trim_trailing_whitespace = true
indent_style = space
indent_size = 2

[*.py]
indent_size = 4

[*.go]
indent_style = tab

[*.md]
trim_trailing_whitespace = false
'''
        with open('.editorconfig', 'w') as f:
            f.write(editorconfig)

def main():
    parser = argparse.ArgumentParser(description='Generate project structure from README configuration')
    parser.add_argument('--config-file', default='README.md', help='Path to README.md file with configuration')
    args = parser.parse_args()
    
    try:
        # Parse configuration
        config_parser = AutomanicConfig()
        config = config_parser.parse_readme(args.config_file)
        
        print(f"✅ Configuration parsed successfully:")
        for key, value in config.items():
            print(f"   {key}: {value}")
        print()
        
        # Generate structure
        generator = StructureGenerator(config)
        generator.generate_structure()
        
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()