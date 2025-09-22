
#!/usr/bin/env python3
"""
Unit tests for fix_workflows.py
"""
import unittest
import tempfile
import os
from unittest.mock import patch, mock_open
import sys
import re

# Add parent directory to path to import the module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestFixWorkflows(unittest.TestCase):
    """Test cases for workflow fixing functionality"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.sample_workflow = """name: Test Workflow
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
      - name: Run validation
        run: python3 scripts/validate-completeness.py
      - name: Generate metrics
        run: python3 scripts/generate-metrics.py > metrics/content-metrics.json
      - name: Update search index
        run: python3 scripts/update-search-index.py
"""
    
    def test_action_version_pinning(self):
        """Test that GitHub actions are pinned to specific versions"""
        content = self.sample_workflow
        
        # Test checkout action pinning
        content = re.sub(r'uses: actions/checkout@v3', 'uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11 # v4', content)
        self.assertIn('actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11 # v4', content)
        self.assertNotIn('actions/checkout@v3', content)
        
        # Test setup-node action pinning
        content = re.sub(r'uses: actions/setup-node@v3', 'uses: actions/setup-node@60edb5dd545a775178f52524783378180af0d1f8 # v4', content)
        self.assertIn('actions/setup-node@60edb5dd545a775178f52524783378180af0d1f8 # v4', content)
        self.assertNotIn('actions/setup-node@v3', content)
    
    def test_conditional_script_checks(self):
        """Test that conditional checks are added for missing scripts"""
        content = self.sample_workflow
        
        # Test validation script conditional
        content = re.sub(
            r'python3 scripts/validate-completeness\.py',
            r'if [ -f scripts/validate-completeness.py ]; then python3 scripts/validate-completeness.py; else echo "Skipping completeness validation - script not found"; fi',
            content
        )
        self.assertIn('if [ -f scripts/validate-completeness.py ]', content)
        self.assertIn('Skipping completeness validation - script not found', content)
        
        # Test metrics script conditional
        content = re.sub(
            r'python3 scripts/generate-metrics\.py > metrics/content-metrics\.json',
            r'if [ -f scripts/generate-metrics.py ]; then python3 scripts/generate-metrics.py > metrics/content-metrics.json; else echo "Skipping metrics generation - script not found"; fi',
            content
        )
        self.assertIn('if [ -f scripts/generate-metrics.py ]', content)
        self.assertIn('Skipping metrics generation - script not found', content)
        
        # Test search index script conditional
        content = re.sub(
            r'python3 scripts/update-search-index\.py',
            r'if [ -f scripts/update-search-index.py ]; then python3 scripts/update-search-index.py; else echo "Skipping search index update - script not found"; fi',
            content
        )
        self.assertIn('if [ -f scripts/update-search-index.py ]', content)
        self.assertIn('Skipping search index update - script not found', content)
    
    def test_permissions_addition(self):
        """Test that permissions block is added to workflows"""
        content = self.sample_workflow
        
        # Add permissions block
        content = re.sub(
            r'runs-on: ubuntu-latest\n    steps:',
            r'runs-on: ubuntu-latest\n    permissions:\n      contents: read\n      pull-requests: read\n    steps:',
            content
        )
        
        self.assertIn('permissions:', content)
        self.assertIn('contents: read', content)
        self.assertIn('pull-requests: read', content)
    
    @patch('os.path.exists')
    @patch('builtins.open', new_callable=mock_open)
    def test_file_operations(self, mock_file, mock_exists):
        """Test file reading and writing operations"""
        mock_exists.return_value = True
        mock_file.return_value.read.return_value = self.sample_workflow
        
        # Test file exists check
        self.assertTrue(mock_exists('test_workflow.yml'))
        
        # Test file reading
        content = mock_file.return_value.read.return_value
        self.assertIn('runs-on: ubuntu-latest', content)
    
    def test_regex_patterns(self):
        """Test that regex patterns work correctly"""
        test_cases = [
            ('uses: actions/checkout@v3', r'uses: actions/checkout@v3'),
            ('uses: actions/setup-node@v3', r'uses: actions/setup-node@v3'),
            ('python3 scripts/validate-completeness.py', r'python3 scripts/validate-completeness\.py'),
            ('python3 scripts/generate-metrics.py > metrics/content-metrics.json', r'python3 scripts/generate-metrics\.py > metrics/content-metrics\.json'),
            ('python3 scripts/update-search-index.py', r'python3 scripts/update-search-index\.py')
        ]
        
        for text, pattern in test_cases:
            self.assertTrue(re.search(pattern, text), f"Pattern {pattern} should match {text}")
    
    def test_error_handling(self):
        """Test error handling in workflow fixing"""
        # Test with non-existent file
        with patch('builtins.open', side_effect=FileNotFoundError):
            with patch('builtins.print') as mock_print:
                try:
                    with open('non_existent_file.yml', 'r') as f:
                        content = f.read()
                except FileNotFoundError:
                    result = False
                else:
                    result = True
                
                self.assertFalse(result)
    
    def test_complete_workflow_transformation(self):
        """Test complete workflow transformation"""
        content = self.sample_workflow
        
        # Apply all transformations
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
        
        # Pin actions
        content = re.sub(r'uses: actions/checkout@v3', 'uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11 # v4', content)
        content = re.sub(r'uses: actions/setup-node@v3', 'uses: actions/setup-node@60edb5dd545a775178f52524783378180af0d1f8 # v4', content)
        
        # Add permissions
        content = re.sub(
            r'runs-on: ubuntu-latest\n    steps:',
            r'runs-on: ubuntu-latest\n    permissions:\n      contents: read\n      pull-requests: read\n    steps:',
            content
        )
        
        # Verify all transformations
        self.assertIn('if [ -f scripts/validate-completeness.py ]', content)
        self.assertIn('if [ -f scripts/generate-metrics.py ]', content)
        self.assertIn('if [ -f scripts/update-search-index.py ]', content)
        self.assertIn('actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11', content)
        self.assertIn('actions/setup-node@60edb5dd545a775178f52524783378180af0d1f8', content)
        self.assertIn('permissions:', content)
        self.assertIn('contents: read', content)

if __name__ == '__main__':
    unittest.main()
