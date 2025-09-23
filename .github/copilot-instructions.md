# Automanic Repository
Automanic is a minimal repository containing license and basic documentation files. The repository serves as a foundational structure with GitHub workflows for CI, Auto Issue Management, and Copilot integration.

Always reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.

## Working Effectively
- **CRITICAL**: This is a minimal repository with no build system, dependencies, or source code files
- Repository structure validation:
  - `ls -la` -- Lists repository contents (takes <1 second)
  - `cat "Trash 1"` -- Shows Unlicense public domain license (takes <1 second)
  - `cat "Trash 2"` -- Shows basic README with "# automanic" (takes <1 second)
- Git operations:
  - `git status` -- Check repository status (takes <1 second)
  - `git log --oneline -n 5` -- View recent commits (takes <1 second)
  - `git branch -a` -- List all branches (takes <1 second)

## Available Development Tools
The following tools are available in the environment:
- **Node.js**: v20.19.5 (`/usr/local/bin/node`)
- **npm**: v10.8.2 (`/usr/local/bin/npm`)  
- **Python**: 3.12.3 (`/usr/bin/python3`)
- **Git**: 2.51.0 (`/usr/bin/git`)
- **Make**: Available (`/usr/bin/make`)
- **GCC**: Available (`/usr/bin/gcc`)
- **Java**: Available (`/usr/bin/java`, `/usr/bin/javac`)
- **Go**: Available (`/usr/bin/go`)
- **Cargo/Rust**: Available (`/home/runner/.cargo/bin/cargo`)

## Build and Test Commands
**IMPORTANT**: No build or test commands exist for this repository as it contains no source code.
- DO NOT run `npm install` -- no package.json exists
- DO NOT run `make` or `make test` -- no Makefile exists
- DO NOT run `python -m pytest` -- no Python source or test files exist
- DO NOT run `cargo build` -- no Cargo.toml exists
- DO NOT run `go build` -- no go.mod exists

## Validation Scenarios
Since this is a minimal repository, validation focuses on basic file operations and git functionality:

### Core Validation Steps
1. **Repository Structure Check**:
   ```bash
   ls -la
   ```
   Expected: Should show `.git/`, `.github/`, `Trash 1`, and `Trash 2` files

2. **License Validation**:
   ```bash
   cat "Trash 1"
   ```
   Expected: Should display Unlicense public domain license text

3. **README Validation**:
   ```bash
   cat "Trash 2"  
   ```
   Expected: Should display "# automanic"

4. **Git Status Check**:
   ```bash
   git status
   ```
   Expected: Should show clean working tree or staged changes

### Manual Testing Requirements  
- **File Access**: Verify both "Trash 1" and "Trash 2" files are readable
- **Git Operations**: Confirm git commands work without errors
- **Directory Structure**: Ensure .github directory exists after creation

## GitHub Workflows
The repository has the following GitHub workflows (visible at GitHub level):
- **CI** (`.github/workflows/ci.yml`) - Continuous Integration
- **Auto Issue Management** (`.github/workflows/auto-management.yml`) - Automated issue handling  
- **Copilot** (`dynamic/copilot-swe-agent/copilot`) - Copilot integration

**Note**: Workflow files may not be present in local working branches but exist at the repository level.

## Navigation and Key Locations
### Repository Root Structure
```
.
├── .git/           # Git repository metadata
├── .github/        # GitHub configuration and workflows
├── Trash 1         # Unlicense public domain license (1,211 bytes)
└── Trash 2         # Basic README with project name (12 bytes)
```

### Important Files
- **Trash 1**: Contains the complete Unlicense public domain dedication
- **Trash 2**: Contains minimal README with just "# automanic"
- **.github/**: Directory for GitHub-specific configuration files

## Common Operations and Timing
All operations in this minimal repository complete in under 1 second:

### File Operations  
- `ls -la` -- Repository listing (<1 second)
- `cat "Trash 1"` -- Read license file (<1 second)  
- `cat "Trash 2"` -- Read README (<1 second)

### Git Operations
- `git status` -- Check status (<1 second)
- `git log --oneline -n 5` -- View commits (<1 second)
- `git add .` -- Stage changes (<1 second)
- `git commit -m "message"` -- Commit changes (<1 second)

### Directory Operations
- `mkdir -p .github` -- Create GitHub directory (<1 second)
- `find . -name "*.md"` -- Search for markdown files (<1 second)

## Development Guidelines
- **File Creation**: Always use absolute paths when creating files
- **Git Operations**: Use git commands for version control; avoid direct file system operations for tracked files  
- **Documentation**: Follow the existing minimal documentation style
- **Testing**: Validate file readability and git functionality after changes

## Limitations and Considerations
- **No Build System**: Repository has no compilation or build requirements
- **No Dependencies**: No package managers or dependency files present
- **No Test Suite**: No automated testing infrastructure exists
- **No Source Code**: Repository contains only documentation and license files
- **Minimal Structure**: Designed for demonstration or template purposes

## Quick Start for New Developers
1. Clone the repository
2. Verify structure with `ls -la`  
3. Read license with `cat "Trash 1"`
4. Read README with `cat "Trash 2"`
5. Check git status with `git status`
6. Create .github directory if needed: `mkdir -p .github`

## Troubleshooting
- **File Not Found**: Ensure you're using quoted filenames for "Trash 1" and "Trash 2" due to spaces
- **Permission Issues**: Verify file permissions with `ls -la`
- **Git Issues**: Confirm you're on the correct branch with `git branch`
- **Missing .github**: Create directory with `mkdir -p .github`