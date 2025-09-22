#!/usr/bin/env python3
import re

def fix_workflow_scripts(file_path):
    """Add conditional checks for missing scripts in workflows"""
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Add conditional checks for missing scripts
        replacements = [
            (r'python3 scripts/validate-completeness\.py', 
             r'if [ -f scripts/validate-completeness.py ]; then python3 scripts/validate-completeness.py; else echo "Skipping completeness validation - script not found"; fi'),
            (r'python3 scripts/generate-metrics\.py > metrics/content-metrics\.json',
             r'if [ -f scripts/generate-metrics.py ]; then python3 scripts/generate-metrics.py > metrics/content-metrics.json; else echo "Skipping metrics generation - script not found"; fi'),
            (r'python3 scripts/update-search-index\.py',
             r'if [ -f scripts/update-search-index.py ]; then python3 scripts/update-search-index.py; else echo "Skipping search index update - script not found"; fi')
        ]
        
        for old, new in replacements:
            content = re.sub(old, new, content)
        
        # Pin actions and add permissions
        content = re.sub(r'uses: actions/checkout@v3', 'uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11 # v4', content)
        content = re.sub(r'uses: actions/setup-node@v3', 'uses: actions/setup-node@60edb5dd545a775178f52524783378180af0d1f8 # v4', content)
        
        # Add permissions block
        content = re.sub(
            r'runs-on: ubuntu-latest\n    steps:',
            r'runs-on: ubuntu-latest\n    permissions:\n      contents: read\n      pull-requests: read\n    steps:',
            content
        )
        
        with open(file_path, 'w') as f:
            f.write(content)
        
        return True
    except Exception as e:
        print(f"Error fixing {file_path}: {e}")
        return False

# Fix the workflow issues
if fix_workflow_scripts('curriculum/day2_intermediate.md'):
    print("Fixed workflow scripts in curriculum/day2_intermediate.md")

