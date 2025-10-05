# Automation Guide

This guide explains the automated features and workflows provided by Automanic.

## GitHub Actions Workflows

Automanic generates several GitHub Actions workflows to automate your development process.

### Continuous Integration (CI)

**File:** `.github/workflows/ci.yml`

**Triggers:**
- Push to `main` or `develop` branches
- Pull requests to `main`

**Features:**
- Multi-version testing (Python: 3.8-3.11, Node.js: 16-20)
- Code linting and formatting checks
- Test execution with coverage reporting
- Security scanning
- Artifact caching for faster builds

**Language-Specific Actions:**

**Python:**
```yaml
- Black formatting check
- Flake8 linting
- MyPy type checking
- Pytest with coverage
- Bandit security scan
```

**JavaScript/TypeScript:**
```yaml
- ESLint linting
- Prettier formatting check
- Jest testing
- TypeScript compilation (TS only)
- NPM audit security check
```

**Go:**
```yaml
- Go fmt formatting check
- Go vet linting
- Go test with race detection
- Go mod tidy verification
- Gosec security scan
```

### Automated Issue Management

**File:** `.github/workflows/auto-management.yml`

**Features:**

1. **Auto-labeling Issues:**
   - Analyzes issue title and content
   - Applies relevant labels (bug, enhancement, documentation, etc.)
   - Sets priority levels (high, medium, low)
   - Estimates complexity

2. **Auto-assigning Pull Request Reviewers:**
   - Analyzes changed files
   - Assigns experts based on file types
   - Considers CODEOWNERS file
   - Limits to 2 reviewers maximum

3. **Project Board Integration:**
   - Automatically adds issues to project boards
   - Organizes by type and priority
   - Updates status based on labels

**Example Auto-labels:**
```yaml
# Content analysis triggers
'bug' keywords → bug label
'feature' keywords → enhancement label
'docs' keywords → documentation label
'security' keywords → security label
'performance' keywords → performance label
```

### Release Automation

**File:** `.github/workflows/auto-release.yml`

**Features:**

1. **Semantic Versioning:**
   - Analyzes commit messages
   - Determines version bumps
   - Creates git tags
   - Generates changelogs

2. **Automated Releases:**
   - Creates GitHub releases
   - Publishes to package registries
   - Uploads artifacts
   - Notifies stakeholders

3. **Dependabot Auto-merge:**
   - Automatically merges passing dependency updates
   - Requires all checks to pass
   - Uses squash merge strategy

**Commit Message Convention:**
```
feat: add new feature (minor version bump)
fix: bug fix (patch version bump)
feat!: breaking change (major version bump)
docs: documentation update (no version bump)
```

### Security Automation

**File:** `.github/workflows/security.yml`

**Features:**

1. **CodeQL Analysis:**
   - Static analysis for security vulnerabilities
   - Supports multiple languages
   - Creates security advisories
   - Integrates with GitHub Security tab

2. **Dependency Scanning:**
   - Scans for vulnerable dependencies
   - Creates security alerts
   - Suggests updates
   - Tracks resolution status

3. **Secret Scanning:**
   - Prevents committing secrets
   - Scans for API keys, tokens
   - Provides remediation guidance

## Issue Templates

Automanic provides comprehensive issue templates to standardize bug reports, feature requests, and documentation updates.

### Bug Report Template

**File:** `.github/ISSUE_TEMPLATE/bug_report.md`

**Sections:**
- Bug description
- Steps to reproduce
- Expected behavior
- Screenshots
- Environment details
- Possible solution

### Feature Request Template

**File:** `.github/ISSUE_TEMPLATE/feature_request.md`

**Sections:**
- Feature description
- Problem statement
- Proposed solution
- Acceptance criteria
- Mockups/examples
- Design considerations

### Documentation Template

**File:** `.github/ISSUE_TEMPLATE/documentation.md`

**Sections:**
- Documentation issue
- Location specification
- Content requirements
- Target audience
- Additional context

## Pull Request Automation

### PR Template

**File:** `.github/PULL_REQUEST_TEMPLATE.md`

**Features:**
- Change description
- Issue linking
- Change type classification
- Testing checklist
- Review checklist

### Automated Checks

**PR Validation:**
- All tests must pass
- Code coverage requirements
- No merge conflicts
- Updated documentation
- Proper commit messages

**Auto-merge Conditions:**
- Dependabot PRs
- All checks passing
- Required reviews completed
- No conflicts

## Development Environment Automation

### Pre-commit Hooks

**File:** `.pre-commit-config.yaml`

**Hooks:**
```yaml
- trailing-whitespace    # Remove trailing whitespace
- end-of-file-fixer     # Ensure files end with newline
- check-yaml            # Validate YAML syntax
- check-ast             # Validate Python AST
- black                 # Python formatting
- flake8                # Python linting
- isort                 # Import sorting
- mypy                  # Type checking
- bandit                # Security linting
```

### Development Scripts

**File:** `scripts/dev.sh`

**Commands:**
```bash
./scripts/dev.sh setup     # Set up development environment
./scripts/dev.sh test      # Run tests
./scripts/dev.sh coverage  # Run tests with coverage
./scripts/dev.sh lint      # Run linters
./scripts/dev.sh format    # Format code
./scripts/dev.sh clean     # Clean up generated files
./scripts/dev.sh docs      # Build documentation
./scripts/dev.sh release   # Prepare release
```

### IDE Configuration

**VS Code Settings:**
- Python interpreter configuration
- Formatting on save
- Linting integration
- Testing integration
- Extension recommendations

**Extensions:**
- Language-specific extensions
- Git integration
- Testing frameworks
- Code quality tools

## Deployment Automation

### Docker Integration

**Generated Files:**
- `Dockerfile` - Multi-stage builds
- `docker-compose.yml` - Local development
- `.dockerignore` - Optimize build context

**Features:**
- Language-optimized base images
- Security best practices
- Multi-architecture builds
- Health checks

### Kubernetes Deployment

**Generated Manifests:**
- Deployment configurations
- Service definitions
- Ingress rules
- ConfigMaps and Secrets
- Horizontal Pod Autoscaling

### Cloud Platform Integration

**AWS:**
- ECR integration
- ECS/EKS deployment
- CloudFormation templates
- Lambda deployment (serverless)

**Google Cloud:**
- Container Registry
- Cloud Run deployment
- GKE integration
- Cloud Functions

**Azure:**
- Container Registry
- Container Apps
- AKS integration
- Azure Functions

## Monitoring and Observability

### Health Checks

**Endpoints:**
- `/health` - Basic health check
- `/ready` - Readiness probe
- `/metrics` - Prometheus metrics

### Logging

**Configuration:**
- Structured logging (JSON)
- Log levels (DEBUG, INFO, WARN, ERROR)
- Request/response logging
- Error tracking integration

### Metrics

**Prometheus Integration:**
- Application metrics
- Custom metrics
- Grafana dashboards
- Alerting rules

## Customizing Automation

### Adding Custom Workflows

1. Create new workflow file in `.github/workflows/`
2. Use existing workflows as templates
3. Configure triggers and jobs
4. Test with pull requests

### Modifying Existing Workflows

1. Edit workflow files directly
2. Update trigger conditions
3. Add/remove steps
4. Configure environment variables

### Environment Variables and Secrets

**Required Secrets:**
- `GITHUB_TOKEN` - Automatically provided
- `DOCKERHUB_USERNAME` - Docker registry
- `DOCKERHUB_TOKEN` - Docker authentication
- `CODECOV_TOKEN` - Coverage reporting

**Environment Variables:**
- `NODE_VERSION` - Node.js version matrix
- `PYTHON_VERSION` - Python version matrix
- `GO_VERSION` - Go version

### Integration with External Services

**Supported Integrations:**
- Codecov - Coverage reporting
- Snyk - Security scanning
- SonarCloud - Code quality
- Slack - Notifications
- Discord - Notifications

## Best Practices

### Workflow Organization

1. **Keep workflows focused** - One workflow per purpose
2. **Use reusable workflows** - Share common patterns
3. **Cache dependencies** - Speed up builds
4. **Parallel jobs** - Reduce total runtime
5. **Conditional execution** - Skip unnecessary work

### Security Considerations

1. **Minimal permissions** - Use least privilege principle
2. **Secret management** - Never hardcode secrets
3. **Dependency scanning** - Regular security updates
4. **Code analysis** - Static security analysis
5. **Branch protection** - Enforce policies

### Performance Optimization

1. **Efficient caching** - Cache dependencies and build artifacts
2. **Matrix strategies** - Test multiple configurations efficiently
3. **Conditional jobs** - Skip jobs when not needed
4. **Resource limits** - Optimize resource usage
5. **Workflow triggers** - Avoid unnecessary runs

## Troubleshooting

### Common Issues

**Workflow failures:**
1. Check workflow logs
2. Verify environment variables
3. Check secret configuration
4. Validate YAML syntax

**Permission issues:**
1. Check repository settings
2. Verify secret access
3. Review workflow permissions
4. Check branch protection rules

**Performance issues:**
1. Review cache usage
2. Optimize job parallelization
3. Reduce dependency installation time
4. Use more specific triggers

### Getting Help

1. Check GitHub Actions documentation
2. Review workflow run logs
3. Use community actions
4. Open issues for bugs
5. Join discussions for help

For more information, see:
- [Configuration Reference](configuration.md)
- [API Documentation](api.md)
- [Setup Guide](setup.md)