#!/usr/bin/env python3
from datetime import datetime

# Read the current defect log
with open('DEFECT_LOG.md', 'r') as f:
    content = f.read()

# Current date for resolution
current_date = datetime.now().strftime('%Y-%m-%d')

# Define which defects we've resolved and their resolution notes
resolved_defects = {
    'DEF-001': 'Added blank lines around table in IntegrationPlan.md',
    'DEF-002': 'Added blank lines around troubleshooting table',
    'DEF-003': 'Added language specification to code blocks',
    'DEF-004': 'Added bash strict mode (set -euo pipefail)',
    'DEF-005': 'Replaced fragile regex with conditional script checks',
    'DEF-006': 'Added bash strict mode to validation script',
    'DEF-007': 'Fixed hard-coded main branch reference to use dynamic detection',
    'DEF-008': 'Pinned Spec Kit version to v1.0.0 for reproducibility',
    'DEF-009': 'Added blank lines around Sprint Documentation Template table',
    'DEF-010': 'Removed leading blank line from YAML file',
    'DEF-011': 'Added blank lines around Training Completion Metrics table',
    'DEF-012': 'Added blank lines around Project Outcome Metrics table',
    'DEF-013': 'Added blank lines around Knowledge Retention Metrics table',
    'DEF-014': 'Converted bold Phase lines to proper headings (####)',
    'DEF-015': 'Created missing referenced files: docs/sdd-guide.md, templates/*.md',
    'DEF-016': 'Fixed incident-response path to use docs/operations/runbooks/',
    'DEF-017': 'Pinned actions, added permissions, created missing config file',
    'DEF-018': 'Added conditional checks for missing scripts in workflow',
    'DEF-019': 'Fixed sed command to use double quotes for variable expansion',
    'DEF-020': 'Added mkdir -p to ensure metrics/daily directory exists',
    'DEF-021': 'Converted HX-Infrastructure Practical Exercise to proper heading'
}

# Update the defect log
lines = content.split('\n')
updated_lines = []

for line in lines:
    updated_line = line
    for defect_id, resolution in resolved_defects.items():
        if defect_id in line and '| Open |' in line:
            # Update status from Open to Resolved and add resolution notes and date
            updated_line = line.replace('| Open |', '| Resolved |')
            updated_line = updated_line.replace('| |', f'| {resolution} |')
            updated_line = updated_line.replace(f'| {current_date} | |', f'| {current_date} | {current_date} |')
    updated_lines.append(updated_line)

# Write the updated defect log
with open('DEFECT_LOG.md', 'w') as f:
    f.write('\n'.join(updated_lines))

print(f"Updated defect log with {len(resolved_defects)} resolved defects")
