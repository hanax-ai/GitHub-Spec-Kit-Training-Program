#!/usr/bin/env python3
import re
import os
from datetime import datetime

def fix_markdown_tables(file_path):
    """Fix MD058 - Add blank lines around tables"""
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return False
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Pattern to find tables that don't have blank lines before/after
    # Look for lines that start with | and are preceded/followed by non-blank lines
    lines = content.split('\n')
    fixed_lines = []
    
    for i, line in enumerate(lines):
        # Check if current line is a table row
        if line.strip().startswith('|') and '|' in line.strip():
            # Check if previous line exists and is not blank
            if i > 0 and lines[i-1].strip() != '' and not lines[i-1].strip().startswith('|'):
                # Add blank line before table
                if len(fixed_lines) > 0 and fixed_lines[-1] != '':
                    fixed_lines.append('')
            
            fixed_lines.append(line)
            
            # Check if this is the last row of the table
            is_last_table_row = (i == len(lines) - 1 or 
                                (i < len(lines) - 1 and not lines[i+1].strip().startswith('|')))
            
            if is_last_table_row:
                # Check if next line exists and is not blank
                if i < len(lines) - 1 and lines[i+1].strip() != '':
                    # Add blank line after table
                    fixed_lines.append('')
        else:
            fixed_lines.append(line)
    
    # Write back the fixed content
    with open(file_path, 'w') as f:
        f.write('\n'.join(fixed_lines))
    
    return True

def fix_bold_headings(file_path):
    """Fix MD036 - Convert bold text to proper headings"""
    if not os.path.exists(file_path):
        return False
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Replace **Phase X:** with #### Phase X:
    content = re.sub(r'\*\*Phase (\d+): ([^*]+)\*\*', r'#### Phase \1: \2', content)
    
    # Replace **HX-Infrastructure Practical Exercise:** with #### HX-Infrastructure Practical Exercise
    content = re.sub(r'\*\*HX-Infrastructure Practical Exercise:\*\*', r'#### HX-Infrastructure Practical Exercise', content)
    
    with open(file_path, 'w') as f:
        f.write(content)
    
    return True

def fix_yaml_blank_lines(file_path):
    """Fix YAML blank line issues"""
    if not os.path.exists(file_path):
        return False
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Remove leading blank lines
    content = content.lstrip('\n')
    
    with open(file_path, 'w') as f:
        f.write(content)
    
    return True

def fix_bash_scripts(file_path):
    """Add bash strict mode to scripts"""
    if not os.path.exists(file_path):
        return False
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Replace #!/bin/bash with strict mode version
    content = re.sub(r'#!/bin/bash\n', '#!/usr/bin/env bash\nset -euo pipefail\nIFS=$\'\\n\\t\'\n\n', content)
    
    with open(file_path, 'w') as f:
        f.write(content)
    
    return True

def fix_sed_command(file_path):
    """Fix sed command variable expansion"""
    if not os.path.exists(file_path):
        return False
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Fix the sed command to use double quotes and safer delimiter
    content = re.sub(
        r"sed -i 's/image: app:v\[0-9\.\]\*/image: app:v\$\{NEW_VERSION\}/' applications/app/deployment\.yaml",
        r'sed -i "s|image:\\s*app:v[0-9.]*|image: app:v${NEW_VERSION}|" applications/app/deployment.yaml',
        content
    )
    
    with open(file_path, 'w') as f:
        f.write(content)
    
    return True

def fix_metrics_script(file_path):
    """Fix metrics script to create directory"""
    if not os.path.exists(file_path):
        return False
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Add mkdir -p before writing to metrics/daily
    content = re.sub(
        r'# Create daily metrics file\ncat > "\$METRICS_DIR/\$DATE-\$PARTICIPANT_ID-day\$DAY\.json"',
        r'# Ensure directory exists\nmkdir -p "$METRICS_DIR"\n\n# Create daily metrics file\ncat > "$METRICS_DIR/$DATE-$PARTICIPANT_ID-day$DAY.json"',
        content
    )
    
    with open(file_path, 'w') as f:
        f.write(content)
    
    return True

def fix_workflow_actions(file_path):
    """Fix workflow to use pinned actions and add permissions"""
    if not os.path.exists(file_path):
        return False
    
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Pin actions to specific versions
    content = re.sub(r'uses: actions/checkout@v3', 'uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11 # v4', content)
    content = re.sub(r'uses: actions/setup-node@v3', 'uses: actions/setup-node@60edb5dd545a775178f52524783378180af0d1f8 # v4', content)
    content = re.sub(r'uses: gaurav-nelson/github-action-markdown-link-check@v1', 'uses: gaurav-nelson/github-action-markdown-link-check@a947807a87961f05621720101487bf0890a81bce # v1', content)
    
    # Add permissions block after runs-on
    content = re.sub(
        r'runs-on: ubuntu-latest\n    steps:',
        r'runs-on: ubuntu-latest\n    permissions:\n      contents: read\n      pull-requests: read\n    steps:',
        content
    )
    
    with open(file_path, 'w') as f:
        f.write(content)
    
    return True

# Now fix all the defects
print("Starting systematic defect remediation...")

# Fix markdown table formatting issues (MD058)
files_to_fix_tables = [
    'docs/IntegrationPlan.md',
    'exercises/hx-kb/day2-intermediate-exercises.md', 
    'curriculum/day2_intermediate.md',
    'metrics/training-outcomes.md'
]

for file_path in files_to_fix_tables:
    if fix_markdown_tables(file_path):
        print(f"Fixed table formatting in {file_path}")

# Fix bold headings (MD036)
if fix_bold_headings('curriculum/day1_foundation.md'):
    print("Fixed bold headings in curriculum/day1_foundation.md")

# Fix YAML blank lines
if fix_yaml_blank_lines('metrics/outcome-tracking-templates.yaml'):
    print("Fixed YAML blank lines in metrics/outcome-tracking-templates.yaml")

# Fix bash scripts
bash_files = [
    'exercises/hx-kb/day1-foundation-exercises.md',
    'exercises/hx-kb/day2-intermediate-exercises.md'
]

for file_path in bash_files:
    if fix_bash_scripts(file_path):
        print(f"Fixed bash scripts in {file_path}")

# Fix sed command
if fix_sed_command('exercises/hx-kb/day2-intermediate-exercises.md'):
    print("Fixed sed command in day2-intermediate-exercises.md")

# Fix metrics script
if fix_metrics_script('metrics/training-outcomes.md'):
    print("Fixed metrics script in training-outcomes.md")

print("Defect remediation completed!")
