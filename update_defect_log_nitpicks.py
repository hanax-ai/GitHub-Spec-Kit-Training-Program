#!/usr/bin/env python3
"""
Update defect log with missed nitpick comments
"""

import json
from datetime import datetime

def update_defect_log_with_nitpicks():
    """Update the defect log with missed nitpick comments"""
    
    # Load analysis results
    with open('nitpick_analysis_results.json', 'r') as f:
        results = json.load(f)
    
    # Read current defect log
    with open('DEFECT_LOG.md', 'r') as f:
        lines = f.readlines()
    
    # Find the end of the table (before the last line)
    table_end_idx = len(lines) - 1
    
    # Prepare new entries
    new_entries = []
    for entry in results['new_defect_entries']:
        # Format the table row
        description = f"{entry['file']} ({entry['line_range']}): **{entry['title']}** (NITPICK)"
        
        row = f"| {entry['id']} | 1 | {description} | {entry['severity']} | System | {entry['status']} | {entry['resolution_notes']} | 2025-09-22 | {'2025-09-22' if entry['status'] == 'Resolved' else ''} |\n"
        new_entries.append(row)
    
    # Insert new entries before the last line
    updated_lines = lines[:table_end_idx] + new_entries + lines[table_end_idx:]
    
    # Write updated defect log
    with open('DEFECT_LOG.md', 'w') as f:
        f.writelines(updated_lines)
    
    print(f"✅ Added {len(new_entries)} nitpick comments to defect log")
    return len(new_entries)

if __name__ == '__main__':
    count = update_defect_log_with_nitpicks()
    print(f"Defect log updated with {count} nitpick entries")
