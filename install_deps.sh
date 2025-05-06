#!/bin/bash

python3 -m venv venv
source venv/bin/activate

# Check if venv is activated
if [[ "$VIRTUAL_ENV" == "" ]]; then
  echo "❌ Virtual environment is not activated."
  echo "Please activate it before running this script."
  exit 1
fi

# Install dependencies
echo "📦 Installing dependencies from requirements.txt..."
pip install -r requirements.txt

echo "✅ Dependencies installed."
echo "To use venv, refer to README.md"
