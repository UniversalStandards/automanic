# Automanic - Advanced Automated Repository Management Template

[![CI](https://github.com/UniversalStandards/automanic/actions/workflows/ci.yml/badge.svg)](https://github.com/UniversalStandards/automanic/actions/workflows/ci.yml)
[![Deploy to GitHub Pages](https://github.com/UniversalStandards/automanic/actions/workflows/deploy.yml/badge.svg)](https://github.com/UniversalStandards/automanic/actions/workflows/deploy.yml)
[![License: Unlicense](https://img.shields.io/badge/license-Unlicense-blue.svg)](http://unlicense.org/)

Automanic is a comprehensive template repository system designed to streamline the setup and management of software projects. It automatically determines the required file and folder structure, repository type, and settings based on user-provided specifications in a `README.md` file or through interactive methods. This tool provides complete automation for GitHub operations including issues, pull requests, reviews, commits, and merges, allowing developers to focus on coding rather than configuration.

## 🌐 Live Demo

Visit the interactive setup wizard: **[https://UniversalStandards.github.io/automanic](https://UniversalStandards.github.io/automanic)**

## 🚀 Quick Start

Follow these steps to get started with Automanic:

### Option 1: Use the Interactive Web GUI (Recommended)

1. Visit [https://UniversalStandards.github.io/automanic](https://UniversalStandards.github.io/automanic)
2. Answer the configuration questions
3. Copy the generated configuration block
4. Paste it into your project's README.md
5. Run the setup script

### Option 2: Clone and Configure Manually

1. **Clone this repository**:
   ```bash
   git clone https://github.com/UniversalStandards/automanic.git
   cd automanic
   ```

2. **Install dependencies**:

   For Python scripts:
   ```bash
   pip install pyyaml
   ```

   For the React web app (optional):
   ```bash
   npm install
   ```

3. **Run the interactive setup**:
   ```bash
   ./scripts/interactive-setup.sh
   ```
   
   Or use the automatic setup with your README.md:
   ```bash
   ./scripts/setup.sh
   ```

## 📋 Configuration Format

Add this configuration block to your README.md:

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

Your project description here...
```

### Configuration Options

| Field | Options |
|-------|---------|
| `PROJECT_TYPE` | `web-app`, `cli-tool`, `library`, `api`, `mobile-app`, `desktop-app`, `data-science`, `documentation` |
| `LANGUAGE` | `python`, `javascript`, `typescript`, `go`, `rust`, `java`, `cpp`, `c`, `php`, `ruby`, `swift`, `kotlin`, `scala`, `r` |
| `FRAMEWORK` | `react`, `vue`, `angular`, `express`, `fastapi`, `django`, `spring`, `gin`, `actix`, `electron`, `flutter`, `pytorch`, `tensorflow`, `none` |
| `BUILD_SYSTEM` | `npm`, `yarn`, `pip`, `cargo`, `maven`, `gradle`, `make`, `cmake`, `none` |
| `DATABASE` | `postgresql`, `mysql`, `mongodb`, `redis`, `sqlite`, `none` |
| `DEPLOYMENT` | `docker`, `kubernetes`, `aws`, `gcp`, `azure`, `vercel`, `netlify`, `heroku`, `none` |
| `CI_CD` | `github-actions`, `jenkins`, `gitlab-ci`, `circleci`, `travis-ci`, `none` |
| `TESTING` | `jest`, `pytest`, `cargo-test`, `junit`, `go-test`, `rspec`, `none` |
| `LICENSE_TYPE` | `mit`, `apache-2.0`, `gpl-v3`, `bsd-3-clause`, `unlicense`, `proprietary` |
| `VISIBILITY` | `public`, `private` |

## 🛠️ Features

### Automated Repository Setup
- Automatically generates folder structures based on project type
- Configures repository settings such as branch protection rules
- Creates language-specific configuration files

### Three Configuration Methods
1. **Interactive Web GUI**: User-friendly web interface for configuration
2. **CLI Walkthrough**: Interactive command-line setup wizard
3. **README.md Template**: Upload a pre-configured README.md

### AI Integration
- Integrates with GitHub Copilot for code suggestions
- Automated code reviews and quality checks
- Smart issue labeling and assignment

### GitHub Actions Automation
- Pre-configured CI/CD workflows
- Automated testing, linting, and deployment
- Security scanning with CodeQL and Bandit
- Dependabot integration for dependency updates

### Issue and PR Management
- Automatic issue labeling based on content
- Automatic reviewer assignment
- PR templates with checklists
- Auto-merge for passing dependency updates

## 📁 Generated Project Structure

```
your-project/
├── .github/
│   ├── workflows/          # CI/CD workflows
│   │   ├── ci.yml         # Continuous Integration
│   │   ├── deploy.yml     # Deployment workflow
│   │   ├── auto-management.yml  # Issue/PR automation
│   │   └── auto-release.yml     # Release automation
│   ├── ISSUE_TEMPLATE/    # Issue templates
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── dependabot.yml     # Dependency updates
├── src/                   # Source code
├── tests/                 # Unit tests
├── docs/                  # Documentation
├── scripts/              # Automation scripts
├── config/               # Configuration files
├── .gitignore           # Git ignore rules
├── .editorconfig        # Editor configuration
├── README.md            # Project documentation
├── CONTRIBUTING.md      # Contribution guidelines
├── CHANGELOG.md         # Version history
├── SECURITY.md          # Security policy
└── LICENSE              # License file
```

## 🔧 GitHub Pages Deployment

This repository is configured for automatic deployment to GitHub Pages.

### How to Enable GitHub Pages

1. Go to your repository **Settings**
2. Navigate to **Pages** in the left sidebar
3. Under **Build and deployment**:
   - **Source**: Select **"GitHub Actions"**
4. The site will automatically deploy when you push to the `main` branch

The GitHub Pages site will be available at: `https://[username].github.io/automanic`

### Manual Deployment

```bash
npm install
npm run deploy
```

## 📚 Documentation

- [Setup Guide](docs/setup.md) - Detailed setup instructions
- [Configuration Reference](docs/configuration.md) - All available options
- [Automation Guide](docs/automation.md) - GitHub Actions workflows
- [API Reference](docs/api.md) - Programmatic usage
- [Examples](docs/examples/) - Sample configurations

## 🎯 Supported Project Types

| Type | Languages | Frameworks | Features |
|------|-----------|------------|----------|
| **Web App** | JS/TS, Python, Go | React, Vue, Django, Express | Full-stack setup, deployment |
| **CLI Tool** | Go, Rust, Python, JS | Cobra, Clap, Click, Commander | Binary building, distribution |
| **Library** | All supported | Framework-specific | Package publishing, docs |
| **API** | Python, Go, JS, Java | FastAPI, Gin, Express, Spring | OpenAPI specs, testing |
| **Mobile** | Dart, Swift, Kotlin | Flutter, React Native | Platform builds, stores |
| **Desktop** | JS/TS, Go, Rust | Tauri, Electron | Cross-platform building |
| **Data Science** | Python, R | PyTorch, TensorFlow | Notebook setup, viz tools |
| **Documentation** | Markdown | MkDocs, Sphinx | Site generation, hosting |

## 🛡️ Security Features

- **SECURITY.md** with vulnerability reporting guidelines
- **Dependabot** for automated dependency updates
- **CodeQL** analysis for security vulnerabilities
- **Bandit** security scanning for Python
- **Branch protection** rules
- **Required reviews** and status checks

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is released into the public domain under the [Unlicense](LICENSE).

## 🔗 Links

- [Live Demo](https://UniversalStandards.github.io/automanic)
- [Issues](https://github.com/UniversalStandards/automanic/issues)
- [Discussions](https://github.com/UniversalStandards/automanic/discussions)
- [Changelog](CHANGELOG.md)
