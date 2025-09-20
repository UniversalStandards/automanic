# Contributing to Automanic

Thank you for considering contributing to Automanic! This document provides guidelines and information for contributors.

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When creating a bug report, include:

- **Clear title and description**
- **Steps to reproduce** the issue
- **Expected vs actual behavior**
- **Environment details** (OS, language versions, etc.)
- **Screenshots** if applicable

Use the bug report template when creating issues.

### Suggesting Enhancements

Enhancement suggestions are welcome! Before creating enhancement suggestions:

- Check if the enhancement is already suggested
- Consider if it fits the project scope
- Provide clear use cases and benefits

Use the feature request template when suggesting enhancements.

### Contributing Code

#### Getting Started

1. **Fork the repository**
   ```bash
   git clone https://github.com/your-username/automanic.git
   cd automanic
   ```

2. **Set up development environment**
   ```bash
   ./scripts/dev.sh setup
   ```

3. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

#### Development Workflow

1. **Write code** following the style guidelines
2. **Add tests** for new functionality
3. **Update documentation** if needed
4. **Run tests** to ensure everything works
5. **Commit your changes** with clear commit messages
6. **Push to your fork** and create a pull request

#### Code Style Guidelines

**Python:**
- Follow PEP 8
- Use Black for formatting
- Add type hints
- Write docstrings for functions and classes
- Use meaningful variable names

**JavaScript/TypeScript:**
- Use ESLint and Prettier
- Follow modern ES6+ patterns
- Add JSDoc comments for functions
- Use TypeScript types where applicable

**Shell Scripts:**
- Use `#!/bin/bash` shebang
- Use `set -e` for error handling
- Quote variables properly
- Add comments for complex logic

#### Commit Messages

Follow the conventional commit format:

```
type(scope): description

[optional body]

[optional footer]
```

**Types:**
- `feat` - New feature
- `fix` - Bug fix
- `docs` - Documentation changes
- `style` - Code style changes (formatting)
- `refactor` - Code refactoring
- `test` - Adding or updating tests
- `chore` - Maintenance tasks

**Examples:**
```
feat(python): add FastAPI template support
fix(workflows): resolve CI workflow permission issue  
docs(readme): update installation instructions
```

#### Pull Request Process

1. **Update documentation** for any new features
2. **Add or update tests** as appropriate
3. **Ensure all tests pass** locally
4. **Use the PR template** and fill out all sections
5. **Link related issues** using keywords (fixes #123)
6. **Request review** from maintainers

**PR Requirements:**
- [ ] All tests pass
- [ ] Documentation updated
- [ ] Code follows style guidelines
- [ ] No merge conflicts
- [ ] Commit messages follow convention

## Development Setup

### Prerequisites

- Python 3.8+
- Node.js 14+ (for JavaScript/TypeScript features)
- Git
- Docker (optional, for testing deployment features)

### Local Development

```bash
# Clone your fork
git clone https://github.com/your-username/automanic.git
cd automanic

# Set up development environment
./scripts/dev.sh setup

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install pre-commit hooks
pre-commit install

# Run tests
./scripts/dev.sh test

# Run linting
./scripts/dev.sh lint

# Format code
./scripts/dev.sh format
```

### Testing

**Run all tests:**
```bash
pytest
```

**Run with coverage:**
```bash
pytest --cov=scripts --cov-report=html
```

**Run specific tests:**
```bash
pytest tests/test_generate_structure.py
```

### Adding New Features

#### Adding Language Support

1. **Update configuration options** in `scripts/generate-structure.py`
2. **Add language-specific templates** in `templates/`
3. **Update file generation logic** in the `StructureGenerator` class
4. **Add tests** for the new language
5. **Update documentation** with new language support

#### Adding Framework Support

1. **Add framework to valid options** in configuration
2. **Implement framework-specific file generation**
3. **Create framework templates** and examples
4. **Update workflows** if needed
5. **Test integration** with existing features

#### Adding New Templates

1. **Create template files** in appropriate `templates/` subdirectory
2. **Add configuration mapping** in generation scripts
3. **Include example README.md** with configuration
4. **Document template features** and usage
5. **Add tests** for template generation

### Documentation

#### Building Documentation

```bash
# Build documentation locally
./scripts/dev.sh docs

# Start documentation server
cd docs
python -m http.server 8000
```

#### Writing Documentation

- Use clear, concise language
- Include code examples
- Add screenshots for UI changes
- Keep documentation up to date with code changes
- Use markdown for consistency

### Release Process

Releases are automated through GitHub Actions, but contributors should:

1. **Update CHANGELOG.md** with new features
2. **Ensure documentation is current**
3. **Run full test suite**
4. **Update version numbers** if applicable

## Community

### Getting Help

- **GitHub Discussions** - For questions and general discussion
- **GitHub Issues** - For bug reports and feature requests
- **Documentation** - Check docs/ for detailed guides

### Recognition

Contributors will be:
- Listed in the project contributors
- Credited in release notes
- Invited to join maintainer discussions (for significant contributions)

## Project Structure

```
automanic/
├── .github/              # GitHub templates and workflows
├── docs/                # Documentation
├── scripts/             # Automation scripts
├── templates/           # Project templates
├── config/             # Configuration files
├── tests/              # Test files
├── README.md           # Main documentation
├── CONTRIBUTING.md     # This file
├── CHANGELOG.md        # Change history
├── SECURITY.md         # Security policy
└── LICENSE            # License file
```

## Questions?

If you have questions about contributing, please:

1. Check existing documentation
2. Search existing issues and discussions
3. Create a new discussion or issue
4. Reach out to maintainers

Thank you for contributing to Automanic! 🚀