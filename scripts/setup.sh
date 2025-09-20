#!/bin/bash

# Automanic Setup Script
# Automatically configures repository structure based on README.md configuration

set -e

echo "🚀 Automanic Repository Setup"
echo "=============================="

# Check if README.md exists
if [ ! -f "README.md" ]; then
    echo "❌ Error: README.md not found. Please upload your project README.md with required configuration fields."
    exit 1
fi

# Check for Python (required for parsing)
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is required but not installed."
    exit 1
fi

echo "📋 Parsing README.md configuration..."
python3 scripts/generate-structure.py --config-file README.md

echo "🏗️  Setting up GitHub workflows..."
python3 scripts/setup-workflows.py

echo "📁 Creating project structure..."
python3 scripts/create-structure.py

echo "🔧 Configuring development environment..."
python3 scripts/setup-dev-env.py

echo "✅ Setup complete! Your repository is now configured."
echo ""
echo "Next steps:"
echo "1. Review generated files and customize as needed"
echo "2. Commit and push your changes"
echo "3. Configure any additional settings in repository settings"
echo "4. Start developing!"