# Automanic - Automated Repository Management Template# Automanic - Automated Repository Management Template



Automanic is a comprehensive template repository system that automatically determines the required file and folder structure, repository type, and settings based on user-provided README.md specifications. It provides complete automation for GitHub operations including issues, pull requests, reviews, commits, and merges.Automanic is a comprehensive template repository system that automatically determines the required file and folder structure, repository type, and settings based on user-provided README.md specifications. It provides complete automation for GitHub operations including issues, pull requests, reviews, commits, and merges.



## 🚀 Quick Start## 🚀 Quick Start



1. **Use this template** to create a new repository1. **Use this template** to create a new repository

2. **Upload your project README.md** with the required fields (see Template Format below)2. **Upload your project README.md** with the required fields (see Template Format below)

3. **Run the setup script** to automatically generate your project structure3. **Run the setup script** to automatically generate your project structure

4. **Customize** as needed4. **Customize** as needed



## 📋 Template Format for User README.md## 📋 Template Format for User README.md



When uploading your README.md, include these **REQUIRED** fields in the specified format:When uploading your README.md, include these **REQUIRED** fields in the specified format:



```markdown```markdown

<!-- AUTOMANIC-CONFIG-START --><!-- AUTOMANIC-CONFIG-START -->

PROJECT_TYPE: [web-app|cli-tool|library|api|mobile-app|desktop-app|data-science|documentation]PROJECT_TYPE: [web-app|cli-tool|library|api|mobile-app|desktop-app|data-science|documentation]

LANGUAGE: [python|javascript|typescript|go|rust|java|cpp|c|php|ruby|swift|kotlin|scala|r]LANGUAGE: [python|javascript|typescript|go|rust|java|cpp|c|php|ruby|swift|kotlin|scala|r]

FRAMEWORK: [react|vue|angular|express|fastapi|django|spring|gin|actix|electron|flutter|pytorch|tensorflow|none]FRAMEWORK: [react|vue|angular|express|fastapi|django|spring|gin|actix|electron|flutter|pytorch|tensorflow|none]

BUILD_SYSTEM: [npm|yarn|pip|cargo|maven|gradle|make|cmake|none]BUILD_SYSTEM: [npm|yarn|pip|cargo|maven|gradle|make|cmake|none]

DATABASE: [postgresql|mysql|mongodb|redis|sqlite|none]DATABASE: [postgresql|mysql|mongodb|redis|sqlite|none]

DEPLOYMENT: [docker|kubernetes|aws|gcp|azure|vercel|netlify|heroku|none]DEPLOYMENT: [docker|kubernetes|aws|gcp|azure|vercel|netlify|heroku|none]

CI_CD: [github-actions|jenkins|gitlab-ci|circleci|travis-ci|none]CI_CD: [github-actions|jenkins|gitlab-ci|circleci|travis-ci|none]

TESTING: [jest|pytest|cargo-test|junit|go-test|rspec|none]TESTING: [jest|pytest|cargo-test|junit|go-test|rspec|none]

LICENSE_TYPE: [mit|apache-2.0|gpl-v3|bsd-3-clause|unlicense|proprietary]LICENSE_TYPE: [mit|apache-2.0|gpl-v3|bsd-3-clause|unlicense|proprietary]

VISIBILITY: [public|private]VISIBILITY: [public|private]

<!-- AUTOMANIC-CONFIG-END --><!-- AUTOMANIC-CONFIG-END -->



# Your Project Title# Your Project Title



Your project description here...Your project description here...

``````



## 🏗️ What Gets Generated## 🏗️ What Gets Generated



Based on your configuration, Automanic automatically creates:Based on your configuration, Automanic automatically creates:



### Core Structure### Core Structure

- **Appropriate `.gitignore`** for your language/framework- **Appropriate `.gitignore`** for your language/framework

- **License file** based on your LICENSE_TYPE- **License file** based on your LICENSE_TYPE

- **CI/CD workflows** for your specified platform- **CI/CD workflows** for your specified platform

- **Issue and PR templates** for your project type- **Issue and PR templates** for your project type

- **Documentation structure** with guides and API docs- **Documentation structure** with guides and API docs

- **Security configuration** (SECURITY.md, dependabot, etc.)- **Security configuration** (SECURITY.md, dependabot, etc.)



### Language-Specific Files### Language-Specific Files

- **Package configuration** (package.json, requirements.txt, Cargo.toml, etc.)- **Package configuration** (package.json, requirements.txt, Cargo.toml, etc.)

- **Build configuration** (webpack, tsconfig, Dockerfile, etc.)- **Build configuration** (webpack, tsconfig, Dockerfile, etc.)

- **Testing setup** with example tests- **Testing setup** with example tests

- **Development environment** (.env.example, dev containers, etc.)- **Development environment** (.env.example, dev containers, etc.)



### Automation Features### Automation Features

- **Automated issue labeling** and assignment- **Automated issue labeling** and assignment

- **PR validation** and testing workflows- **PR validation** and testing workflows

- **Automated code reviews** and merge strategies- **Automated code reviews** and merge strategies

- **Release automation** with semantic versioning- **Release automation** with semantic versioning

- **Dependency management** and security updates- **Dependency management** and security updates



## 🔧 Usage## 🔧 Usage



### Method 1: Automated Setup (Recommended)### Method 1: Automated Setup (Recommended)

```bash```bash

# Clone or use this template# Clone or use this template

# Upload your README.md with required fields# Upload your README.md with required fields

./scripts/setup.sh./scripts/setup.sh

``````



### Method 2: Manual Configuration### Method 2: Manual Configuration

```bash```bash

# Run interactive setup# Run interactive setup

./scripts/interactive-setup.sh./scripts/interactive-setup.sh



# Or configure specific components# Or configure specific components

./scripts/generate-structure.py --config-file your-readme.md./scripts/generate-structure.py --config-file your-readme.md

``````



## 📁 Generated Structure Example## 📁 Generated Structure Example



For a Python web application, Automanic generates:For a Python web application, Automanic generates:



``````

your-project/your-project/

├── .github/├── .github/

│   ├── workflows/│   ├── workflows/

│   │   ├── ci.yml│   │   ├── ci.yml

│   │   ├── cd.yml│   │   ├── cd.yml

│   │   └── security.yml│   │   └── security.yml

│   ├── ISSUE_TEMPLATE/│   ├── ISSUE_TEMPLATE/

│   └── PULL_REQUEST_TEMPLATE.md│   └── PULL_REQUEST_TEMPLATE.md

├── src/├── src/

├── tests/├── tests/

├── docs/├── docs/

├── scripts/├── scripts/

├── requirements.txt├── requirements.txt

├── setup.py├── setup.py

├── Dockerfile├── Dockerfile

├── docker-compose.yml├── docker-compose.yml

├── .env.example├── .env.example

└── README.md (your customized version)└── README.md (your customized version)

``````



## 🔄 Automation Capabilities## 🔄 Automation Capabilities



### Issue Management### Issue Management

- **Auto-labeling** based on content analysis- **Auto-labeling** based on content analysis

- **Template-based** issue creation- **Template-based** issue creation

- **Assignment** based on expertise areas- **Assignment** based on expertise areas

- **Progress tracking** with project boards- **Progress tracking** with project boards



### Pull Request Management### Pull Request Management

- **Automated validation** and testing- **Automated validation** and testing

- **Review assignment** based on CODEOWNERS- **Review assignment** based on CODEOWNERS

- **Merge strategies** with branch protection- **Merge strategies** with branch protection

- **Release automation** on merge to main- **Release automation** on merge to main



### Code Quality### Code Quality

- **Automated linting** and formatting- **Automated linting** and formatting

- **Security scanning** with CodeQL- **Security scanning** with CodeQL

- **Dependency updates** with Dependabot- **Dependency updates** with Dependabot

- **Performance monitoring** and alerts- **Performance monitoring** and alerts



## 🎯 Supported Project Types## 🎯 Supported Project Types



| Type | Languages | Frameworks | Features || Type | Languages | Frameworks | Features |

|------|-----------|------------|----------||------|-----------|------------|----------|

| **Web App** | JS/TS, Python, Go | React, Vue, Django, Express | Full-stack setup, deployment || **Web App** | JS/TS, Python, Go | React, Vue, Django, Express | Full-stack setup, deployment |

| **CLI Tool** | Go, Rust, Python, JS | Cobra, Clap, Click, Commander | Binary building, distribution || **CLI Tool** | Go, Rust, Python, JS | Cobra, Clap, Click, Commander | Binary building, distribution |

| **Library** | All supported | Framework-specific | Package publishing, docs || **Library** | All supported | Framework-specific | Package publishing, docs |

| **API** | Python, Go, JS, Java | FastAPI, Gin, Express, Spring | OpenAPI specs, testing || **API** | Python, Go, JS, Java | FastAPI, Gin, Express, Spring | OpenAPI specs, testing |

| **Mobile** | Dart, Swift, Kotlin | Flutter, React Native | Platform builds, stores || **Mobile** | Dart, Swift, Kotlin | Flutter, React Native | Platform builds, stores |

| **Desktop** | Electron, Go, Rust | Tauri, Electron, Iced | Cross-platform building || **Desktop** | Electron, Go, Rust | Tauri, Electron, Iced | Cross-platform building |

| **Data Science** | Python, R, Julia | Jupyter, Streamlit, Shiny | Notebook setup, viz tools || **Data Science** | Python, R, Julia | Jupyter, Streamlit, Shiny | Notebook setup, viz tools |

| **Documentation** | Markdown | GitBook, MkDocs, Sphinx | Site generation, hosting || **Documentation** | Markdown | GitBook, MkDocs, Sphinx | Site generation, hosting |



## 🛡️ Security Features## 🛡️ Security Features



- **SECURITY.md** with vulnerability reporting- **SECURITY.md** with vulnerability reporting

- **Dependabot** configuration for updates- **Dependabot** configuration for updates

- **CodeQL** analysis workflows- **CodeQL** analysis workflows

- **Secret scanning** prevention- **Secret scanning** prevention

- **Branch protection** rules- **Branch protection** rules

- **Required reviews** and status checks- **Required reviews** and status checks



## 🚢 Deployment Configurations## 🚢 Deployment Configurations



Pre-configured for major platforms:Pre-configured for major platforms:

- **Docker** with multi-stage builds- **Docker** with multi-stage builds

- **Kubernetes** with Helm charts- **Kubernetes** with Helm charts

- **AWS** with CDK/CloudFormation- **AWS** with CDK/CloudFormation

- **GCP** with Cloud Run/GKE- **GCP** with Cloud Run/GKE

- **Azure** with Container Apps- **Azure** with Container Apps

- **Vercel/Netlify** for static sites- **Vercel/Netlify** for static sites



## 📚 Documentation## 📚 Documentation



- [Setup Guide](docs/setup.md) - Detailed setup instructions- [Setup Guide](docs/setup.md) - Detailed setup instructions

- [Configuration Reference](docs/configuration.md) - All available options- [Configuration Reference](docs/configuration.md) - All available options

- [Automation Guide](docs/automation.md) - GitHub Actions workflows- [Automation Guide](docs/automation.md) - GitHub Actions workflows

- [Templates Guide](docs/templates.md) - Creating custom templates- [Templates Guide](docs/templates.md) - Creating custom templates

- [API Reference](docs/api.md) - Programmatic usage- [API Reference](docs/api.md) - Programmatic usage

- [Examples](docs/examples/) - Sample configurations- [Examples](docs/examples/) - Sample configurations



## 🤝 Contributing## 🤝 Contributing



1. Fork the repository1. Fork the repository

2. Create a feature branch2. Create a feature branch

3. Make your changes3. Make your changes

4. Add tests if applicable4. Add tests if applicable

5. Submit a pull request5. Submit a pull request



## 📄 License## 📄 License



This project is released under the [Unlicense](LICENSE) - free and unencumbered software released into the public domain.This project is released under the [Unlicense](LICENSE) - free and unencumbered software released into the public domain.



## 🔗 Links## 🔗 Links



- [Issues](https://github.com/UniversalStandards/automanic/issues)- [Issues](https://github.com/UniversalStandards/automanic/issues)

- [Discussions](https://github.com/UniversalStandards/automanic/discussions)- [Discussions](https://github.com/UniversalStandards/automanic/discussions)

- [Wiki](https://github.com/UniversalStandards/automanic/wiki)- [Wiki](https://github.com/UniversalStandards/automanic/wiki)

- [Changelog](CHANGELOG.md)- [Changelog](CHANGELOG.md)
