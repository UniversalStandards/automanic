# API Reference

This document provides the API reference for Automanic's programmatic usage.

## Python API

### AutomanicConfig Class

The `AutomanicConfig` class handles parsing and validation of Automanic configuration from README.md files.

```python
from scripts.generate_structure import AutomanicConfig

config_parser = AutomanicConfig()
config = config_parser.parse_readme('README.md')
```

#### Methods

##### `parse_readme(readme_path: str) -> Dict[str, str]`

Parses configuration from a README.md file.

**Parameters:**
- `readme_path` (str): Path to the README.md file containing the configuration block.

**Returns:**
- `Dict[str, str]`: Dictionary containing the parsed configuration values.

**Raises:**
- `Exception`: If the configuration block is not found or contains invalid values.

**Example:**
```python
config = config_parser.parse_readme('path/to/README.md')
print(config['PROJECT_TYPE'])  # Output: 'web-app'
print(config['LANGUAGE'])      # Output: 'python'
```

##### `_validate_config(config: Dict[str, str]) -> None`

Validates the parsed configuration values against valid options.

**Parameters:**
- `config` (Dict[str, str]): Dictionary containing configuration key-value pairs.

**Raises:**
- `Exception`: If required fields are missing or values are invalid.

### StructureGenerator Class

The `StructureGenerator` class generates project structure based on configuration.

```python
from scripts.generate_structure import StructureGenerator

generator = StructureGenerator(config)
generator.generate_structure()
```

#### Methods

##### `generate_structure() -> None`

Generates the complete project structure based on the provided configuration.

**Example:**
```python
from scripts.generate_structure import AutomanicConfig, StructureGenerator

# Parse configuration
config_parser = AutomanicConfig()
config = config_parser.parse_readme('README.md')

# Generate structure
generator = StructureGenerator(config)
generator.generate_structure()
```

### ProjectStructureCreator Class

The `ProjectStructureCreator` class creates detailed project files and directories.

```python
from scripts.create_structure import ProjectStructureCreator

creator = ProjectStructureCreator()
creator.create_structure()
```

#### Methods

##### `create_structure() -> None`

Creates the complete project structure including source files, tests, documentation, and configuration.

### DevEnvironmentSetup Class

The `DevEnvironmentSetup` class sets up the development environment with necessary tools and configurations.

```python
from scripts.setup_dev_env import DevEnvironmentSetup

setup = DevEnvironmentSetup()
setup.setup_environment()
```

#### Methods

##### `setup_environment() -> None`

Sets up the complete development environment including:
- Pre-commit hooks
- Development dependencies
- IDE configurations
- Development scripts

### WorkflowGenerator Class

The `WorkflowGenerator` class generates GitHub Actions workflows based on project configuration.

```python
from scripts.setup_workflows import WorkflowGenerator

generator = WorkflowGenerator()
generator.generate_workflows()
```

#### Methods

##### `generate_workflows() -> None`

Generates all necessary GitHub Actions workflow files:
- CI workflow
- CD workflow
- Security workflow
- Dependabot configuration

## Command Line Interface

### Main Setup Script

```bash
./scripts/setup.sh
```

Automatically configures repository structure based on README.md configuration.

**Options:**
- Reads configuration from `README.md` in the current directory
- Generates project structure
- Sets up GitHub workflows
- Configures development environment

### Interactive Setup

```bash
./scripts/interactive-setup.sh
```

Runs the interactive setup wizard that guides you through configuration options.

**Process:**
1. Prompts for each configuration option
2. Shows summary of selected options
3. Generates README.md with configuration
4. Creates project structure

### Structure Generation

```bash
python scripts/generate-structure.py --config-file README.md
```

Generates project structure from a configuration file.

**Arguments:**
- `--config-file`: Path to the README.md file with configuration (default: `README.md`)

### Validation

```bash
python scripts/validate.py
```

Validates the Automanic installation and configuration.

**Checks:**
- Required files and directories
- Script syntax and executability
- Template configuration blocks
- Workflow YAML syntax

## Configuration File Format

The configuration block must be placed in your README.md:

```markdown
<!-- AUTOMANIC-CONFIG-START -->
PROJECT_TYPE: web-app
LANGUAGE: python
FRAMEWORK: fastapi
BUILD_SYSTEM: pip
DATABASE: postgresql
DEPLOYMENT: docker
CI_CD: github-actions
TESTING: pytest
LICENSE_TYPE: mit
VISIBILITY: public
<!-- AUTOMANIC-CONFIG-END -->
```

### Required Fields

All fields are required:

| Field | Type | Description |
|-------|------|-------------|
| `PROJECT_TYPE` | string | Type of project |
| `LANGUAGE` | string | Programming language |
| `FRAMEWORK` | string | Framework to use |
| `BUILD_SYSTEM` | string | Build system |
| `DATABASE` | string | Database system |
| `DEPLOYMENT` | string | Deployment platform |
| `CI_CD` | string | CI/CD platform |
| `TESTING` | string | Testing framework |
| `LICENSE_TYPE` | string | License type |
| `VISIBILITY` | string | Repository visibility |

## Error Handling

### Common Errors

#### Configuration Not Found
```
Exception: Automanic configuration block not found in README.md
```
Ensure your README.md contains the configuration block between `<!-- AUTOMANIC-CONFIG-START -->` and `<!-- AUTOMANIC-CONFIG-END -->`.

#### Missing Required Fields
```
Exception: Missing required fields: FIELD_NAME
```
Add the missing field to your configuration block.

#### Invalid Value
```
Exception: Invalid value 'VALUE' for field 'FIELD'. Valid values: ...
```
Use one of the valid values listed in the error message.

## Integration Examples

### CI/CD Integration

```yaml
# .github/workflows/setup.yml
name: Setup New Project

on:
  workflow_dispatch:
    inputs:
      project_type:
        description: 'Project type'
        required: true
        default: 'web-app'

jobs:
  setup:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run Automanic Setup
        run: python scripts/generate-structure.py
```

### Docker Integration

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY scripts/ ./scripts/
COPY README.md .

RUN python scripts/generate-structure.py
```

## Related Documentation

- [Setup Guide](setup.md)
- [Configuration Reference](configuration.md)
- [Automation Guide](automation.md)
- [Examples](examples/)
