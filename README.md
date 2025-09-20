# Automanic - Automated Repository Management Template

Automanic is a comprehensive template repository system that automatically determines the required file and folder structure, repository type, and settings based on user-provided README.md specifications. It provides complete automation for GitHub operations including issues, pull requests, reviews, commits, and merges.

## 🚀 Quick Start

1. **Use this template** to create a new repository
2. **Upload your project README.md** with the required fields (see Template Format below)
3. **Run the setup script** to automatically generate your project structure
4. **Customize** as needed

## 📋 Template Format for User README.md

When uploading your README.md, include these **REQUIRED** fields in the specified format:

```markdown
<!-- AUTOMANIC-CONFIG-START -->
PROJECT_TYPE: [web-app|cli-tool|library|api|mobile-app|desktop-app|data-science|documentation]
LANGUAGE: [python|javascript|typescript|go|rust|java|cpp|c|php|ruby|swift|kotlin|scala|r]
FRAMEWORK: [react|vue|angular|express|fastapi|django|spring|gin|actix|electron|flutter|pytorch|tensorflow|none]
BUILD_SYSTEM: [npm|yarn|pip|cargo|maven|gradle|make|cmake|none]
DATABASE: [postgresql|mysql|mongodb|redis|sqlite|none]
DEPLOYMENT: [docker|kubernetes|aws|gcp|azure|vercel|netlify|heroku|none]
CI_CD: [github-actions|jenkins|gitlab-ci|circleci|travis-ci|none]
TESTING: [jest|pytest|cargo-test|junit|go-test|rspec|none]
LICENSE_TYPE: [mit|apache-2.0|gpl-v3|bsd-3-clause|unlicense|proprietary]
VISIBILITY: [public|private]
<!-- AUTOMANIC-CONFIG-END -->

# Your Project Title

Your project description here...
```

## 🏗️ What Gets Generated

Based on your configuration, Automanic automatically creates:

### Core Structure
- **Appropriate `.gitignore`** for your language/framework
- **License file** based on your LICENSE_TYPE
- **CI/CD workflows** for your specified platform
- **Issue and PR templates** for your project type
- **Documentation structure** with guides and API docs
- **Security configuration** (SECURITY.md, dependabot, etc.)

### Language-Specific Files
- **Package configuration** (package.json, requirements.txt, Cargo.toml, etc.)
- **Build configuration** (webpack, tsconfig, Dockerfile, etc.)
- **Testing setup** with example tests
- **Development environment** (.env.example, dev containers, etc.)

### Automation Features
- **Automated issue labeling** and assignment
- **PR validation** and testing workflows
- **Automated code reviews** and merge strategies
- **Release automation** with semantic versioning
- **Dependency management** and security updates

## 🔧 Usage

### Method 1: Automated Setup (Recommended)
```bash
# Clone or use this template
# Upload your README.md with required fields
./scripts/setup.sh
```

### Method 2: Manual Configuration
```bash
# Run interactive setup
./scripts/interactive-setup.sh

# Or configure specific components
./scripts/generate-structure.py --config-file your-readme.md
```

## 📁 Generated Structure Example

For a Python web application, Automanic generates:

```
your-project/
├── .github/
│   ├── workflows/
│   │   ├── ci.yml
│   │   ├── cd.yml
│   │   └── security.yml
│   ├── ISSUE_TEMPLATE/
│   └── PULL_REQUEST_TEMPLATE.md
├── src/
├── tests/
├── docs/
├── scripts/
├── requirements.txt
├── setup.py
├── Dockerfile
├── docker-compose.yml
├── .env.example
└── README.md (your customized version)
```

## 🔄 Automation Capabilities

### Issue Management
- **Auto-labeling** based on content analysis
- **Template-based** issue creation
- **Assignment** based on expertise areas
- **Progress tracking** with project boards

### Pull Request Management
- **Automated validation** and testing
- **Review assignment** based on CODEOWNERS
- **Merge strategies** with branch protection
- **Release automation** on merge to main

### Code Quality
- **Automated linting** and formatting
- **Security scanning** with CodeQL
- **Dependency updates** with Dependabot
- **Performance monitoring** and alerts

## 🎯 Supported Project Types

| Type | Languages | Frameworks | Features |
|------|-----------|------------|----------|
| **Web App** | JS/TS, Python, Go | React, Vue, Django, Express | Full-stack setup, deployment |
| **CLI Tool** | Go, Rust, Python, JS | Cobra, Clap, Click, Commander | Binary building, distribution |
| **Library** | All supported | Framework-specific | Package publishing, docs |
| **API** | Python, Go, JS, Java | FastAPI, Gin, Express, Spring | OpenAPI specs, testing |
| **Mobile** | Dart, Swift, Kotlin | Flutter, React Native | Platform builds, stores |
| **Desktop** | Electron, Go, Rust | Tauri, Electron, Iced | Cross-platform building |
| **Data Science** | Python, R, Julia | Jupyter, Streamlit, Shiny | Notebook setup, viz tools |
| **Documentation** | Markdown | GitBook, MkDocs, Sphinx | Site generation, hosting |

## 🛡️ Security Features

- **SECURITY.md** with vulnerability reporting
- **Dependabot** configuration for updates
- **CodeQL** analysis workflows
- **Secret scanning** prevention
- **Branch protection** rules
- **Required reviews** and status checks

## 🚢 Deployment Configurations

Pre-configured for major platforms:
- **Docker** with multi-stage builds
- **Kubernetes** with Helm charts
- **AWS** with CDK/CloudFormation
- **GCP** with Cloud Run/GKE
- **Azure** with Container Apps
- **Vercel/Netlify** for static sites

## 📚 Documentation

- [Setup Guide](docs/setup.md) - Detailed setup instructions
- [Configuration Reference](docs/configuration.md) - All available options
- [Automation Guide](docs/automation.md) - GitHub Actions workflows
- [Templates Guide](docs/templates.md) - Creating custom templates
- [API Reference](docs/api.md) - Programmatic usage
- [Examples](docs/examples/) - Sample configurations

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is released under the [Unlicense](LICENSE) - free and unencumbered software released into the public domain.

## 🔗 Links

- [Issues](https://github.com/UniversalStandards/automanic/issues)
- [Discussions](https://github.com/UniversalStandards/automanic/discussions)
- [Wiki](https://github.com/UniversalStandards/automanic/wiki)
- [Changelog](CHANGELOG.md)