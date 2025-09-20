#!/usr/bin/env python3
"""
Automanic Validation Script

Tests and validates the complete Automanic setup.
"""

import os
import sys
import subprocess
from pathlib import Path
from typing import List, Tuple

class AutomanicValidator:
    """Validates Automanic installation and functionality"""
    
    def __init__(self):
        self.base_path = Path.cwd()
        self.errors = []
        self.warnings = []
        
    def validate_installation(self) -> bool:
        """Validate the complete installation"""
        print("🔍 Validating Automanic Installation")
        print("=" * 50)
        
        # Check required files and directories
        self._check_structure()
        
        # Validate scripts
        self._validate_scripts()
        
        # Check templates
        self._check_templates()
        
        # Validate workflows
        self._check_workflows()
        
        # Test configuration parsing
        self._test_config_parsing()
        
        # Summary
        self._print_summary()
        
        return len(self.errors) == 0
        
    def _check_structure(self):
        """Check required directory structure"""
        print("📁 Checking directory structure...")
        
        required_dirs = [
            ".github/workflows",
            ".github/ISSUE_TEMPLATE", 
            "scripts",
            "docs",
            "templates/python",
            "templates/javascript",
            "templates/go",
            "config"
        ]
        
        for dir_path in required_dirs:
            full_path = self.base_path / dir_path
            if not full_path.exists():
                self.errors.append(f"Missing directory: {dir_path}")
            else:
                print(f"✅ {dir_path}")
                
        required_files = [
            "README.md",
            "CONTRIBUTING.md", 
            "CHANGELOG.md",
            "SECURITY.md",
            "LICENSE",
            "scripts/setup.sh",
            "scripts/generate-structure.py",
            "scripts/setup-workflows.py",
            "scripts/create-structure.py",
            "scripts/setup-dev-env.py",
            "scripts/interactive-setup.sh",
            ".github/workflows/ci.yml",
            ".github/workflows/auto-management.yml",
            ".github/workflows/auto-release.yml",
            ".github/ISSUE_TEMPLATE/bug_report.md",
            ".github/ISSUE_TEMPLATE/feature_request.md",
            ".github/PULL_REQUEST_TEMPLATE.md",
            ".github/dependabot.yml"
        ]
        
        for file_path in required_files:
            full_path = self.base_path / file_path
            if not full_path.exists():
                self.errors.append(f"Missing file: {file_path}")
            else:
                print(f"✅ {file_path}")
                
    def _validate_scripts(self):
        """Validate script files"""
        print("\n🐍 Validating Python scripts...")
        
        python_scripts = [
            "scripts/generate-structure.py",
            "scripts/setup-workflows.py", 
            "scripts/create-structure.py",
            "scripts/setup-dev-env.py"
        ]
        
        for script_path in python_scripts:
            full_path = self.base_path / script_path
            if full_path.exists():
                # Check if script is executable
                if not os.access(full_path, os.X_OK):
                    self.warnings.append(f"Script not executable: {script_path}")
                    
                # Try to compile the script
                try:
                    with open(full_path, 'r') as f:
                        compile(f.read(), script_path, 'exec')
                    print(f"✅ {script_path} - syntax OK")
                except SyntaxError as e:
                    self.errors.append(f"Syntax error in {script_path}: {e}")
                    
        print("\n🔧 Validating shell scripts...")
        
        shell_scripts = [
            "scripts/setup.sh",
            "scripts/interactive-setup.sh"
        ]
        
        for script_path in shell_scripts:
            full_path = self.base_path / script_path
            if full_path.exists():
                if not os.access(full_path, os.X_OK):
                    self.errors.append(f"Script not executable: {script_path}")
                else:
                    print(f"✅ {script_path} - executable")
                    
    def _check_templates(self):
        """Check template files"""
        print("\n📄 Checking templates...")
        
        template_files = [
            "templates/python/fastapi-web-app.md",
            "templates/javascript/cli-tool.md",
            "templates/go/api-service.md"
        ]
        
        for template_path in template_files:
            full_path = self.base_path / template_path
            if full_path.exists():
                # Check if template has config block
                with open(full_path, 'r') as f:
                    content = f.read()
                    if "AUTOMANIC-CONFIG-START" in content and "AUTOMANIC-CONFIG-END" in content:
                        print(f"✅ {template_path} - config block found")
                    else:
                        self.warnings.append(f"Template missing config block: {template_path}")
            else:
                self.warnings.append(f"Template file not found: {template_path}")
                
    def _check_workflows(self):
        """Check GitHub Actions workflows"""
        print("\n⚙️  Checking GitHub workflows...")
        
        workflow_files = [
            ".github/workflows/ci.yml",
            ".github/workflows/auto-management.yml", 
            ".github/workflows/auto-release.yml"
        ]
        
        for workflow_path in workflow_files:
            full_path = self.base_path / workflow_path
            if full_path.exists():
                try:
                    import yaml
                    with open(full_path, 'r') as f:
                        yaml.safe_load(f)
                    print(f"✅ {workflow_path} - valid YAML")
                except yaml.YAMLError as e:
                    self.errors.append(f"Invalid YAML in {workflow_path}: {e}")
                except ImportError:
                    self.warnings.append("PyYAML not available for workflow validation")
                    print(f"⚠️  {workflow_path} - unable to validate (missing PyYAML)")
                    
    def _test_config_parsing(self):
        """Test configuration parsing"""
        print("\n🧪 Testing configuration parsing...")
        
        # Create a test README with config
        test_readme = '''# Test Project

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

Test project description.
'''
        
        test_file = self.base_path / "test_readme.md"
        try:
            with open(test_file, 'w') as f:
                f.write(test_readme)
                
            # Import and test the configuration parser
            sys.path.insert(0, str(self.base_path / "scripts"))
            
            try:
                from generate_structure import AutomanicConfig
                
                config_parser = AutomanicConfig()
                config = config_parser.parse_readme(str(test_file))
                
                if len(config) == 10:  # All required fields
                    print("✅ Configuration parsing - OK")
                else:
                    self.errors.append(f"Configuration parsing failed - only got {len(config)} fields")
                    
            except ImportError as e:
                self.warnings.append(f"Could not test config parsing (import error): {e}")
                print("⚠️  Configuration parsing - skipped (import error)")
            except Exception as e:
                self.errors.append(f"Configuration parsing error: {e}")
                
        finally:
            # Clean up test file
            if test_file.exists():
                test_file.unlink()
                
    def _print_summary(self):
        """Print validation summary"""
        print("\n" + "=" * 50)
        print("📊 VALIDATION SUMMARY")
        print("=" * 50)
        
        if not self.errors and not self.warnings:
            print("🎉 Perfect! All validations passed.")
        else:
            if self.errors:
                print(f"❌ {len(self.errors)} Error(s):")
                for error in self.errors:
                    print(f"   • {error}")
                    
            if self.warnings:
                print(f"⚠️  {len(self.warnings)} Warning(s):")
                for warning in self.warnings:
                    print(f"   • {warning}")
                    
        print("\n🔗 Next Steps:")
        if not self.errors:
            print("✅ Installation is valid!")
            print("   • Try running: ./scripts/interactive-setup.sh")
            print("   • Or use a template from templates/ directory")
            print("   • Read docs/setup.md for detailed instructions")
        else:
            print("❌ Please fix the errors above before proceeding")
            print("   • Check file permissions with: chmod +x scripts/*.sh")
            print("   • Ensure all required files are present")
            print("   • Review the setup documentation")

def main():
    validator = AutomanicValidator()
    success = validator.validate_installation()
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()