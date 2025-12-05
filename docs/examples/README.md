# Automanic Examples

This directory contains example configurations for different project types.

## Quick Links

- [Python FastAPI Web App](python-fastapi.md)
- [JavaScript CLI Tool](javascript-cli.md)
- [Go REST API](go-api.md)
- [TypeScript React App](typescript-react.md)
- [Data Science Project](data-science.md)

## Example Configurations

### Python FastAPI Web Application

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

### JavaScript CLI Tool

```markdown
<!-- AUTOMANIC-CONFIG-START -->
PROJECT_TYPE: cli-tool
LANGUAGE: javascript
FRAMEWORK: none
BUILD_SYSTEM: npm
DATABASE: none
DEPLOYMENT: none
CI_CD: github-actions
TESTING: jest
LICENSE_TYPE: mit
VISIBILITY: public
<!-- AUTOMANIC-CONFIG-END -->
```

### Go REST API

```markdown
<!-- AUTOMANIC-CONFIG-START -->
PROJECT_TYPE: api
LANGUAGE: go
FRAMEWORK: gin
BUILD_SYSTEM: go
DATABASE: postgresql
DEPLOYMENT: kubernetes
CI_CD: github-actions
TESTING: go-test
LICENSE_TYPE: apache-2.0
VISIBILITY: public
<!-- AUTOMANIC-CONFIG-END -->
```

### TypeScript React Application

```markdown
<!-- AUTOMANIC-CONFIG-START -->
PROJECT_TYPE: web-app
LANGUAGE: typescript
FRAMEWORK: react
BUILD_SYSTEM: npm
DATABASE: none
DEPLOYMENT: vercel
CI_CD: github-actions
TESTING: jest
LICENSE_TYPE: mit
VISIBILITY: public
<!-- AUTOMANIC-CONFIG-END -->
```

### Python Data Science Project

```markdown
<!-- AUTOMANIC-CONFIG-START -->
PROJECT_TYPE: data-science
LANGUAGE: python
FRAMEWORK: pytorch
BUILD_SYSTEM: pip
DATABASE: none
DEPLOYMENT: docker
CI_CD: github-actions
TESTING: pytest
LICENSE_TYPE: mit
VISIBILITY: public
<!-- AUTOMANIC-CONFIG-END -->
```

### Rust CLI Tool

```markdown
<!-- AUTOMANIC-CONFIG-START -->
PROJECT_TYPE: cli-tool
LANGUAGE: rust
FRAMEWORK: none
BUILD_SYSTEM: cargo
DATABASE: none
DEPLOYMENT: none
CI_CD: github-actions
TESTING: cargo-test
LICENSE_TYPE: apache-2.0
VISIBILITY: public
<!-- AUTOMANIC-CONFIG-END -->
```

### Java Spring Boot API

```markdown
<!-- AUTOMANIC-CONFIG-START -->
PROJECT_TYPE: api
LANGUAGE: java
FRAMEWORK: spring
BUILD_SYSTEM: maven
DATABASE: postgresql
DEPLOYMENT: kubernetes
CI_CD: github-actions
TESTING: junit
LICENSE_TYPE: apache-2.0
VISIBILITY: private
<!-- AUTOMANIC-CONFIG-END -->
```

## Usage

1. Copy the appropriate configuration block to your README.md
2. Customize the values as needed
3. Run `./scripts/setup.sh` to generate your project structure

For more details, see the [Configuration Reference](../configuration.md).
