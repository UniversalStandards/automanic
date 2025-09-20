#!/usr/bin/env python3
"""
Development Environment Setup

Sets up the development environment with necessary tools and configurations.
"""

import os
import subprocess
import sys
from pathlib import Path

class DevEnvironmentSetup:
    """Sets up development environment"""
    
    def __init__(self):
        self.base_path = Path.cwd()
        
    def setup_environment(self):
        """Setup the complete development environment"""
        print("🔧 Setting up development environment...")
        
        # Setup pre-commit hooks
        self._setup_precommit_hooks()
        
        # Setup development dependencies
        self._setup_dev_dependencies()
        
        # Setup IDE configurations
        self._setup_ide_config()
        
        # Setup development scripts
        self._setup_dev_scripts()
        
        print("✅ Development environment setup complete!")
        
    def _setup_precommit_hooks(self):
        """Setup pre-commit hooks for code quality"""
        
        precommit_config = '''repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
      - id: check-ast
      - id: check-merge-conflict
      - id: debug-statements

  - repo: https://github.com/psf/black
    rev: 23.12.1
    hooks:
      - id: black
        language_version: python3

  - repo: https://github.com/pycqa/flake8
    rev: 7.0.0
    hooks:
      - id: flake8
        additional_dependencies: [flake8-docstrings]

  - repo: https://github.com/pycqa/isort
    rev: 5.13.2
    hooks:
      - id: isort
        args: ["--profile", "black"]

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.8.0
    hooks:
      - id: mypy
        additional_dependencies: [types-all]
        exclude: ^tests/

  - repo: https://github.com/PyCQA/bandit
    rev: 1.7.5
    hooks:
      - id: bandit
        args: ['-c', '.bandit']
        exclude: ^tests/

  - repo: https://github.com/pycqa/pydocstyle
    rev: 6.3.0
    hooks:
      - id: pydocstyle
        exclude: ^tests/
'''
        
        with open('.pre-commit-config.yaml', 'w') as f:
            f.write(precommit_config)
            
        # Create bandit configuration
        bandit_config = '''[bandit]
exclude_dirs = ["tests", "venv", ".venv"]
skips = ["B101", "B601"]
'''
        
        with open('.bandit', 'w') as f:
            f.write(bandit_config)
            
        print("🪝 Created pre-commit hooks configuration")
        
    def _setup_dev_dependencies(self):
        """Setup development dependencies"""
        
        dev_requirements = '''# Development dependencies
pre-commit>=3.6.0
black>=23.12.0
flake8>=7.0.0
isort>=5.13.0
mypy>=1.8.0
bandit>=1.7.5
pytest>=7.4.0
pytest-cov>=4.1.0
pytest-mock>=3.12.0
pytest-asyncio>=0.23.0
coverage>=7.4.0
tox>=4.11.0

# Documentation
sphinx>=7.2.0
sphinx-rtd-theme>=2.0.0
mkdocs>=1.5.0
mkdocs-material>=9.5.0

# Development tools
pip-tools>=7.3.0
twine>=4.0.0
wheel>=0.42.0
setuptools>=69.0.0

# Type stubs
types-requests>=2.31.0
types-PyYAML>=6.0.0
'''
        
        with open('requirements-dev.txt', 'w') as f:
            f.write(dev_requirements)
            
        # Create tox configuration
        tox_ini = '''[tox]
envlist = py38,py39,py310,py311,flake8,mypy,bandit,coverage
isolated_build = true

[testenv]
deps = 
    pytest
    pytest-cov
    pytest-mock
commands = pytest {posargs}

[testenv:flake8]
deps = flake8
commands = flake8 src tests

[testenv:mypy]
deps = mypy
commands = mypy src

[testenv:bandit]
deps = bandit
commands = bandit -r src

[testenv:coverage]
deps = 
    pytest
    pytest-cov
commands = 
    pytest --cov=src --cov-report=term-missing --cov-report=html --cov-fail-under=80

[testenv:docs]
deps = 
    sphinx
    sphinx-rtd-theme
commands = sphinx-build -b html docs docs/_build/html
'''
        
        with open('tox.ini', 'w') as f:
            f.write(tox_ini)
            
        print("📦 Created development dependencies configuration")
        
    def _setup_ide_config(self):
        """Setup IDE configurations"""
        
        # VS Code configuration
        vscode_dir = Path('.vscode')
        vscode_dir.mkdir(exist_ok=True)
        
        # VS Code settings
        vscode_settings = {
            "python.defaultInterpreterPath": "./venv/bin/python",
            "python.formatting.provider": "black",
            "python.linting.enabled": True,
            "python.linting.flake8Enabled": True,
            "python.linting.mypyEnabled": True,
            "python.linting.banditEnabled": True,
            "python.testing.pytestEnabled": True,
            "python.testing.unittestEnabled": False,
            "editor.formatOnSave": True,
            "editor.codeActionsOnSave": {
                "source.organizeImports": True
            },
            "files.exclude": {
                "**/__pycache__": True,
                "**/*.pyc": True,
                ".pytest_cache": True,
                ".coverage": True,
                "htmlcov": True,
                ".tox": True,
                ".mypy_cache": True,
                "*.egg-info": True
            }
        }
        
        import json
        with open(vscode_dir / 'settings.json', 'w') as f:
            json.dump(vscode_settings, f, indent=2)
            
        # VS Code extensions recommendations
        extensions = {
            "recommendations": [
                "ms-python.python",
                "ms-python.flake8",
                "ms-python.mypy-type-checker",
                "ms-python.black-formatter",
                "ms-python.isort",
                "streetsidesoftware.code-spell-checker",
                "eamodio.gitlens",
                "github.vscode-pull-request-github",
                "ms-vscode.vscode-yaml"
            ]
        }
        
        with open(vscode_dir / 'extensions.json', 'w') as f:
            json.dump(extensions, f, indent=2)
            
        # VS Code launch configuration for debugging
        launch_config = {
            "version": "0.2.0",
            "configurations": [
                {
                    "name": "Python: Current File",
                    "type": "python",
                    "request": "launch",
                    "program": "${file}",
                    "console": "integratedTerminal"
                },
                {
                    "name": "Python: Main Module",
                    "type": "python",
                    "request": "launch",
                    "program": "src/main.py",
                    "console": "integratedTerminal"
                },
                {
                    "name": "Python: Pytest",
                    "type": "python",
                    "request": "launch",
                    "module": "pytest",
                    "console": "integratedTerminal"
                }
            ]
        }
        
        with open(vscode_dir / 'launch.json', 'w') as f:
            json.dump(launch_config, f, indent=2)
            
        print("🖥️  Created IDE configurations")
        
    def _setup_dev_scripts(self):
        """Setup development scripts"""
        
        scripts_dir = Path('scripts')
        scripts_dir.mkdir(exist_ok=True)
        
        # Development script
        dev_script = '''#!/bin/bash
# Development helper script

set -e

COMMAND="$1"

case $COMMAND in
  "setup")
    echo "🔧 Setting up development environment..."
    python -m venv venv
    source venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    pip install -r requirements-dev.txt
    pre-commit install
    echo "✅ Development environment setup complete!"
    ;;
    
  "test")
    echo "🧪 Running tests..."
    pytest
    ;;
    
  "coverage")
    echo "📊 Running tests with coverage..."
    pytest --cov=src --cov-report=html --cov-report=term
    echo "Coverage report generated in htmlcov/"
    ;;
    
  "lint")
    echo "🔍 Running linters..."
    flake8 src tests
    mypy src
    bandit -r src
    ;;
    
  "format")
    echo "✨ Formatting code..."
    black .
    isort .
    ;;
    
  "clean")
    echo "🧹 Cleaning up..."
    find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
    find . -type f -name "*.pyc" -delete
    rm -rf .coverage htmlcov/ .pytest_cache/ .mypy_cache/ .tox/ *.egg-info/ build/ dist/
    ;;
    
  "docs")
    echo "📚 Building documentation..."
    cd docs
    make html
    echo "Documentation built in docs/_build/html/"
    ;;
    
  "release")
    echo "🚀 Preparing release..."
    python -m twine check dist/*
    echo "Release artifacts validated!"
    ;;
    
  *)
    echo "Usage: $0 {setup|test|coverage|lint|format|clean|docs|release}"
    echo ""
    echo "Commands:"
    echo "  setup     - Set up development environment"
    echo "  test      - Run tests"
    echo "  coverage  - Run tests with coverage report"
    echo "  lint      - Run linters (flake8, mypy, bandit)"
    echo "  format    - Format code (black, isort)"
    echo "  clean     - Clean up generated files"
    echo "  docs      - Build documentation"
    echo "  release   - Validate release artifacts"
    exit 1
    ;;
esac
'''
        
        with open(scripts_dir / 'dev.sh', 'w') as f:
            f.write(dev_script)
            
        os.chmod(scripts_dir / 'dev.sh', 0o755)
        
        # Makefile for common tasks
        makefile = '''# Makefile for development tasks

.PHONY: help setup test coverage lint format clean docs install build release

help:
	@echo "Available commands:"
	@echo "  setup     - Set up development environment"
	@echo "  test      - Run tests"
	@echo "  coverage  - Run tests with coverage"
	@echo "  lint      - Run linters"
	@echo "  format    - Format code"
	@echo "  clean     - Clean up generated files"
	@echo "  docs      - Build documentation"
	@echo "  install   - Install package in development mode"
	@echo "  build     - Build package"
	@echo "  release   - Upload to PyPI"

setup:
	python -m venv venv
	. venv/bin/activate && pip install --upgrade pip
	. venv/bin/activate && pip install -r requirements.txt
	. venv/bin/activate && pip install -r requirements-dev.txt
	. venv/bin/activate && pre-commit install

test:
	pytest

coverage:
	pytest --cov=src --cov-report=html --cov-report=term

lint:
	flake8 src tests
	mypy src
	bandit -r src

format:
	black .
	isort .

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	rm -rf .coverage htmlcov/ .pytest_cache/ .mypy_cache/ .tox/ *.egg-info/ build/ dist/

docs:
	cd docs && make html

install:
	pip install -e .

build:
	python -m build

release: build
	python -m twine upload dist/*
'''
        
        with open('Makefile', 'w') as f:
            f.write(makefile)
            
        print("📜 Created development scripts")

def main():
    setup = DevEnvironmentSetup()
    setup.setup_environment()

if __name__ == "__main__":
    main()