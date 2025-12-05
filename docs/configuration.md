# Configuration Reference

This document provides detailed information about all configuration options available in Automanic.

## Configuration Block

The Automanic configuration block must be placed in your README.md file between the following markers:

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

## Configuration Options

### PROJECT_TYPE

Defines the type of project being created.

| Value | Description |
|-------|-------------|
| `web-app` | Web application with frontend/backend components |
| `cli-tool` | Command-line interface tool |
| `library` | Reusable code library or package |
| `api` | REST API service |
| `mobile-app` | Mobile application (iOS/Android) |
| `desktop-app` | Desktop application |
| `data-science` | Data science or machine learning project |
| `documentation` | Documentation site |

### LANGUAGE

Specifies the primary programming language.

| Value | Description |
|-------|-------------|
| `python` | Python 3.8+ |
| `javascript` | JavaScript (ES6+) |
| `typescript` | TypeScript |
| `go` | Go 1.21+ |
| `rust` | Rust |
| `java` | Java 17+ |
| `cpp` | C++ |
| `c` | C |
| `php` | PHP |
| `ruby` | Ruby |
| `swift` | Swift |
| `kotlin` | Kotlin |
| `scala` | Scala |
| `r` | R |

### FRAMEWORK

Specifies the framework to use.

| Value | Description | Compatible Languages |
|-------|-------------|---------------------|
| `react` | React.js | JavaScript, TypeScript |
| `vue` | Vue.js | JavaScript, TypeScript |
| `angular` | Angular | TypeScript |
| `express` | Express.js | JavaScript, TypeScript |
| `fastapi` | FastAPI | Python |
| `django` | Django | Python |
| `spring` | Spring Boot | Java, Kotlin |
| `gin` | Gin | Go |
| `actix` | Actix Web | Rust |
| `electron` | Electron | JavaScript, TypeScript |
| `flutter` | Flutter | Dart |
| `pytorch` | PyTorch | Python |
| `tensorflow` | TensorFlow | Python |
| `none` | No framework | All |

### BUILD_SYSTEM

Specifies the build and package management system.

| Value | Description |
|-------|-------------|
| `npm` | Node Package Manager |
| `yarn` | Yarn package manager |
| `pip` | Python pip |
| `cargo` | Rust Cargo |
| `maven` | Apache Maven |
| `gradle` | Gradle |
| `make` | Make |
| `cmake` | CMake |
| `none` | No build system |

### DATABASE

Specifies the database system.

| Value | Description |
|-------|-------------|
| `postgresql` | PostgreSQL |
| `mysql` | MySQL/MariaDB |
| `mongodb` | MongoDB |
| `redis` | Redis |
| `sqlite` | SQLite |
| `none` | No database |

### DEPLOYMENT

Specifies the deployment platform.

| Value | Description |
|-------|-------------|
| `docker` | Docker containers |
| `kubernetes` | Kubernetes |
| `aws` | Amazon Web Services |
| `gcp` | Google Cloud Platform |
| `azure` | Microsoft Azure |
| `vercel` | Vercel |
| `netlify` | Netlify |
| `heroku` | Heroku |
| `none` | No deployment automation |

### CI_CD

Specifies the CI/CD platform.

| Value | Description |
|-------|-------------|
| `github-actions` | GitHub Actions |
| `jenkins` | Jenkins |
| `gitlab-ci` | GitLab CI/CD |
| `circleci` | CircleCI |
| `travis-ci` | Travis CI |
| `none` | No CI/CD |

### TESTING

Specifies the testing framework.

| Value | Description |
|-------|-------------|
| `jest` | Jest (JavaScript/TypeScript) |
| `pytest` | pytest (Python) |
| `cargo-test` | cargo test (Rust) |
| `junit` | JUnit (Java) |
| `go-test` | go test (Go) |
| `rspec` | RSpec (Ruby) |
| `none` | No testing framework |

### LICENSE_TYPE

Specifies the license type.

| Value | Description |
|-------|-------------|
| `mit` | MIT License (permissive) |
| `apache-2.0` | Apache License 2.0 |
| `gpl-v3` | GNU GPL v3 (copyleft) |
| `bsd-3-clause` | BSD 3-Clause License |
| `unlicense` | Unlicense (public domain) |
| `proprietary` | Proprietary/closed source |

### VISIBILITY

Specifies repository visibility.

| Value | Description |
|-------|-------------|
| `public` | Public repository |
| `private` | Private repository |

## Environment Variables

Automanic respects the following environment variables:

| Variable | Description | Default |
|----------|-------------|---------|
| `AUTOMANIC_CONFIG_FILE` | Path to configuration file | `README.md` |
| `AUTOMANIC_OUTPUT_DIR` | Output directory for generated files | Current directory |
| `AUTOMANIC_SKIP_GIT` | Skip git initialization | `false` |
| `AUTOMANIC_VERBOSE` | Enable verbose output | `false` |

## Generated File Structure

Based on your configuration, Automanic generates a standardized project structure:

```
project/
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
├── CHANGELOG.md            # Change log
└── LICENSE                 # License file
```

## Customization

After generation, you can customize:

1. **Edit generated files** to match your specific requirements
2. **Add additional dependencies** to package configuration files
3. **Modify workflows** in `.github/workflows/`
4. **Update documentation** in `docs/` and README.md
5. **Configure IDE settings** in `.vscode/` or similar

## Related Documentation

- [Setup Guide](setup.md)
- [Automation Guide](automation.md)
- [API Reference](api.md)
- [Examples](examples/)
