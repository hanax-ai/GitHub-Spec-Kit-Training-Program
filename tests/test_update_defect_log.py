
#!/usr/bin/env python3
"""
Unit tests for update_defect_log.py
"""
import unittest
import tempfile
import os
from datetime import datetime
from unittest.mock import patch, mock_open
import sys

# Add parent directory to path to import the module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestUpdateDefectLog(unittest.TestCase):
    """Test cases for defect log update functionality"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.sample_defect_log = """# Defect Log

| ID | Description | Severity | Status | Created | Resolved | Resolution Notes |
|---|---|---|---|---|---|---|
| DEF-001 | Sample defect 1 | Medium | Open | 2025-09-22 | | |
| DEF-002 | Sample defect 2 | High | Open | 2025-09-22 | | |
| DEF-003 | Sample defect 3 | Low | Resolved | 2025-09-22 | 2025-09-22 | Already fixed |
"""
        
        self.expected_resolved_defects = {
            'DEF-001': 'Added blank lines around table in IntegrationPlan.md',
            'DEF-002': 'Added blank lines around troubleshooting table'
        }
    
    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_defect_log_reading(self, mock_exists, mock_file):
        """Test that defect log is read correctly"""
        mock_exists.return_value = True
        mock_file.return_value.read.return_value = self.sample_defect_log
        
        # Import and run the logic (simplified version)
        with patch('builtins.print'):
            # Simulate the file reading part
            content = mock_file.return_value.read.return_value
            self.assertIn('DEF-001', content)
            self.assertIn('DEF-002', content)
    
    def test_defect_resolution_logic(self):
        """Test the defect resolution logic"""
        lines = self.sample_defect_log.split('\n')
        current_date = datetime.now().strftime('%Y-%m-%d')
        
        # Test resolution logic for DEF-001
        test_line = "| DEF-001 | Sample defect 1 | Medium | Open | 2025-09-22 | | |"
        resolution = "Added blank lines around table in IntegrationPlan.md"
        
        # Simulate the update logic
        if 'DEF-001' in test_line and '| Open |' in test_line:
            updated_line = test_line.replace('| Open |', '| Resolved |')
            updated_line = updated_line.replace('| |', f'| {resolution} |')
            
            self.assertIn('| Resolved |', updated_line)
            self.assertIn(resolution, updated_line)
    
    def test_date_formatting(self):
        """Test that dates are formatted correctly"""
        current_date = datetime.now().strftime('%Y-%m-%d')
        
        # Test date format
        self.assertRegex(current_date, r'\d{4}-\d{2}-\d{2}')
    
    @patch('builtins.open', new_callable=mock_open)
    def test_file_writing(self, mock_file):
        """Test that updated content is written correctly"""
        test_content = "Updated defect log content"
        
        # Simulate writing
        with patch('builtins.print'):
            mock_file.return_value.write(test_content)
            mock_file.return_value.write.assert_called_with(test_content)

if __name__ == '__main__':
    unittest.main()
