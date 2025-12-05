#!/bin/bash

# Automanic Interactive Setup Script
# Provides a command-line interface for project configuration

set -e

echo "🚀 Automanic Interactive Setup"
echo "=============================="
echo ""

# Check for Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is required but not installed."
    exit 1
fi

# Run the Python interactive setup script
python3 "$(dirname "$0")/interactive-setup.py"
