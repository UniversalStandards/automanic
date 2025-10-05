# Setup Guide

This guide will help you set up and use the Automanic template repository system.

## Prerequisites

- Git
- Python 3.8+ 
- Node.js 14+ (if working with JavaScript/TypeScript projects)
- Docker (optional, for deployment features)

## Installation Methods

### Method 1: Use as GitHub Template

1. Click "Use this template" on the GitHub repository
2. Create your new repository
3. Clone your new repository locally
4. Follow the [Quick Start](#quick-start) section

### Method 2: Clone and Customize

```bash
git clone https://github.com/UniversalStandards/automanic.git
cd automanic
```

## Quick Start

### Option A: Automatic Setup (Recommended)

1. **Prepare your README.md**: Create or modify your README.md with the required configuration block:

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

# Your Project Title
Your project description...
```

2. **Run the setup script**:
```bash
./scripts/setup.sh
```

3. **Review generated files** and customize as needed

### Option B: Interactive Setup

If you prefer a guided setup process:

```bash
./scripts/interactive-setup.sh
```

This will walk you through each configuration option and generate the appropriate project structure.

## Configuration Options

### Required Fields

All fields in the `AUTOMANIC-CONFIG` block are required:

| Field | Description | Valid Values |
|-------|-------------|--------------|
| `PROJECT_TYPE` | Type of project | `web-app`, `cli-tool`, `library`, `api`, `mobile-app`, `desktop-app`, `data-science`, `documentation` |
| `LANGUAGE` | Programming language | `python`, `javascript`, `typescript`, `go`, `rust`, `java`, `cpp`, `c`, `php`, `ruby`, `swift`, `kotlin`, `scala`, `r` |
| `FRAMEWORK` | Framework to use | `react`, `vue`, `angular`, `express`, `fastapi`, `django`, `spring`, `gin`, `actix`, `electron`, `flutter`, `pytorch`, `tensorflow`, `none` |
| `BUILD_SYSTEM` | Build system | `npm`, `yarn`, `pip`, `cargo`, `maven`, `gradle`, `make`, `cmake`, `none` |
| `DATABASE` | Database system | `postgresql`, `mysql`, `mongodb`, `redis`, `sqlite`, `none` |
| `DEPLOYMENT` | Deployment platform | `docker`, `kubernetes`, `aws`, `gcp`, `azure`, `vercel`, `netlify`, `heroku`, `none` |
| `CI_CD` | CI/CD system | `github-actions`, `jenkins`, `gitlab-ci`, `circleci`, `travis-ci`, `none` |
| `TESTING` | Testing framework | `jest`, `pytest`, `cargo-test`, `junit`, `go-test`, `rspec`, `none` |
| `LICENSE_TYPE` | License type | `mit`, `apache-2.0`, `gpl-v3`, `bsd-3-clause`, `unlicense`, `proprietary` |
| `VISIBILITY` | Repository visibility | `public`, `private` |

## What Gets Generated

Based on your configuration, Automanic creates:

### Directory Structure
```
your-project/
├── .github/
│   ├── workflows/           # CI/CD workflows
│   ├── ISSUE_TEMPLATE/      # Issue templates
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── dependabot.yml
├── src/                     # Source code
├── tests/                   # Test files
├── docs/                    # Documentation
├── scripts/                 # Automation scripts
├── config/                  # Configuration files
├── .gitignore              # Git ignore rules
├── .editorconfig           # Editor configuration
├── README.md               # Project documentation
├── CONTRIBUTING.md         # Contribution guidelines
├── SECURITY.md             # Security policy
└── LICENSE                 # License file
```

### Generated Files by Language

**Python Projects:**
- `requirements.txt` - Dependencies
- `setup.py` - Package setup
- `pyproject.toml` - Build configuration
- `.pre-commit-config.yaml` - Pre-commit hooks
- `tox.ini` - Testing configuration

**JavaScript/TypeScript Projects:**
- `package.json` - Dependencies and scripts
- `tsconfig.json` (TypeScript only)
- `.eslintrc.js` - Linting configuration
- `jest.config.js` - Testing configuration

**Go Projects:**
- `go.mod` - Module definition
- `Dockerfile` - Container configuration
- `Makefile` - Build automation

**Rust Projects:**
- `Cargo.toml` - Package configuration
- `Dockerfile` - Container configuration

### Automation Features

**GitHub Actions Workflows:**
- `ci.yml` - Continuous Integration
- `auto-management.yml` - Issue/PR automation
- `auto-release.yml` - Release automation
- `security.yml` - Security scanning

**Development Tools:**
- Pre-commit hooks for code quality
- Automated formatting and linting
- Test automation
- Coverage reporting
- Dependency updates

## Customization

After generation, you can customize:

1. **Edit generated files** to match your specific needs
2. **Add additional dependencies** to package files
3. **Modify workflows** in `.github/workflows/`
4. **Update documentation** in `docs/` and README.md
5. **Configure IDE settings** in `.vscode/`

## Troubleshooting

### Common Issues

**Python not found:**
```bash
# Install Python 3.8+
# On macOS with Homebrew:
brew install python

# On Ubuntu/Debian:
sudo apt-get install python3 python3-pip
```

**Permission denied on scripts:**
```bash
chmod +x scripts/*.sh
```

**Configuration block not found:**
Make sure your README.md contains the exact format:
```markdown
<!-- AUTOMANIC-CONFIG-START -->
...configuration...
<!-- AUTOMANIC-CONFIG-END -->
```

**Invalid configuration values:**
Check that all values match the valid options listed in the Configuration Options table.

### Getting Help

1. Check the [API documentation](api.md)
2. Look at [example templates](../templates/)
3. Open an issue on GitHub
4. Join our discussions

## Advanced Usage

### Custom Templates

You can create custom templates for specific project patterns:

1. Create a new template in `templates/`
2. Add configuration mapping in `scripts/generate-structure.py`
3. Test with your configuration

### Extending Automation

Add custom GitHub Actions workflows:

1. Create new workflow files in `.github/workflows/`
2. Use the existing workflows as templates
3. Configure secrets in repository settings

### Integration with External Tools

Automanic integrates with:
- **GitHub Codespaces** - Pre-configured development environments
- **GitPod** - Cloud development environments  
- **Dependabot** - Automated dependency updates
- **CodeQL** - Security analysis
- **Various deployment platforms**

## Next Steps

After setup:

1. **Review all generated files**
2. **Install dependencies** for your language
3. **Set up development environment**
4. **Configure repository settings** on GitHub
5. **Start coding!**

For more detailed information, see:
- [Configuration Reference](configuration.md)
- [Automation Guide](automation.md)
- [API Documentation](api.md)
- [Examples](examples/)