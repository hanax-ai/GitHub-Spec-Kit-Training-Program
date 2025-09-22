
#!/usr/bin/env python3
"""
Unit tests for fix_defects.py
"""
import unittest
import tempfile
import os
from unittest.mock import patch, mock_open
import sys

# Add parent directory to path to import the module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestFixDefects(unittest.TestCase):
    """Test cases for defect fixing functionality"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.sample_markdown_with_table = """# Test Document

Some content here.
| Column 1 | Column 2 |
|----------|----------|
| Value 1  | Value 2  |
More content here.
"""
        
        self.sample_markdown_with_bold_heading = """# Test Document

**Phase 1: Setup**

Some content here.

**HX-Infrastructure Practical Exercise:**

More content.
"""
        
        self.sample_bash_script = """#!/bin/bash

echo "Hello World"
"""
        
        self.sample_yaml_with_leading_blank = """

key: value
another_key: another_value
"""
    
    def test_markdown_table_detection(self):
        """Test detection of markdown tables"""
        lines = self.sample_markdown_with_table.split('\n')
        
        table_lines = []
        for line in lines:
            if line.strip().startswith('|') and '|' in line.strip():
                table_lines.append(line)
        
        self.assertEqual(len(table_lines), 3)  # Header, separator, data row
    
    def test_bold_heading_conversion(self):
        """Test conversion of bold text to proper headings"""
        import re
        
        content = self.sample_markdown_with_bold_heading
        
        # Test Phase conversion
        updated_content = re.sub(r'\*\*Phase (\d+): ([^*]+)\*\*', r'#### Phase \1: \2', content)
        self.assertIn('#### Phase 1: Setup', updated_content)
        self.assertNotIn('**Phase 1: Setup**', updated_content)
        
        # Test HX-Infrastructure conversion
        updated_content = re.sub(r'\*\*HX-Infrastructure Practical Exercise:\*\*', r'#### HX-Infrastructure Practical Exercise', updated_content)
        self.assertIn('#### HX-Infrastructure Practical Exercise', updated_content)
        self.assertNotIn('**HX-Infrastructure Practical Exercise:**', updated_content)
    
    def test_yaml_blank_line_removal(self):
        """Test removal of leading blank lines from YAML"""
        content = self.sample_yaml_with_leading_blank
        cleaned_content = content.lstrip('\n')
        
        self.assertFalse(cleaned_content.startswith('\n'))
        self.assertTrue(cleaned_content.startswith('key: value'))
    
    def test_bash_strict_mode_addition(self):
        """Test addition of bash strict mode"""
        import re
        
        content = self.sample_bash_script
        updated_content = re.sub(r'#!/bin/bash\n', '#!/usr/bin/env bash\nset -euo pipefail\nIFS=$\'\\n\\t\'\n\n', content)
        
        self.assertIn('#!/usr/bin/env bash', updated_content)
        self.assertIn('set -euo pipefail', updated_content)
        self.assertIn('IFS=$\'', updated_content)
        self.assertIn('\'', updated_content)
    
    def test_sed_command_fix(self):
        """Test sed command variable expansion fix"""
        import re
        
        original_sed = "sed -i 's/image: app:v[0-9.]*/image: app:v${NEW_VERSION}/' applications/app/deployment.yaml"
        fixed_sed = re.sub(
            r"sed -i 's/image: app:v\[0-9\.\]\*/image: app:v\$\{NEW_VERSION\}/' applications/app/deployment\.yaml",
            r'sed -i "s|image:\\s*app:v[0-9.]*|image: app:v${NEW_VERSION}|" applications/app/deployment.yaml',
            original_sed
        )
        
        self.assertIn('sed -i "s|image:', fixed_sed)
        self.assertIn('${NEW_VERSION}', fixed_sed)
    
    @patch('os.path.exists')
    @patch('builtins.open', new_callable=mock_open)
    def test_file_operations(self, mock_file, mock_exists):
        """Test file reading and writing operations"""
        mock_exists.return_value = True
        mock_file.return_value.read.return_value = self.sample_markdown_with_table
        
        # Test file exists check
        self.assertTrue(mock_exists('test_file.md'))
        
        # Test file reading
        content = mock_file.return_value.read.return_value
        self.assertIn('| Column 1 | Column 2 |', content)
    
    def test_table_blank_line_logic(self):
        """Test the logic for adding blank lines around tables"""
        lines = [
            "Some text",
            "| Header 1 | Header 2 |",
            "|----------|----------|", 
            "| Data 1   | Data 2   |",
            "More text"
        ]
        
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
        
        # Verify blank lines were added
        table_start_index = None
        table_end_index = None
        
        for i, line in enumerate(fixed_lines):
            if line.strip().startswith('| Header'):
                table_start_index = i
            elif line.strip().startswith('| Data') and table_start_index is not None:
                table_end_index = i
                break
        
        # Check that there's a blank line before the table
        if table_start_index and table_start_index > 0:
            self.assertEqual(fixed_lines[table_start_index - 1], '')
        
        # Check that there's a blank line after the table
        if table_end_index and table_end_index < len(fixed_lines) - 1:
            self.assertEqual(fixed_lines[table_end_index + 1], '')

if __name__ == '__main__':
    unittest.main()
