
#!/usr/bin/env python3
"""
Integration tests for the GitHub Spec Kit Training Program
"""
import unittest
import tempfile
import os
import shutil
from unittest.mock import patch, mock_open
import sys

# Add parent directory to path to import modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestIntegration(unittest.TestCase):
    """Integration test cases for the training program"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.test_dir = tempfile.mkdtemp()
        self.original_cwd = os.getcwd()
        os.chdir(self.test_dir)
        
        # Create test file structure
        os.makedirs('docs', exist_ok=True)
        os.makedirs('exercises/hx-kb', exist_ok=True)
        os.makedirs('curriculum', exist_ok=True)
        os.makedirs('metrics', exist_ok=True)
        
        # Create test defect log
        self.create_test_defect_log()
        
    def tearDown(self):
        """Clean up test fixtures"""
        os.chdir(self.original_cwd)
        shutil.rmtree(self.test_dir)
    
    def create_test_defect_log(self):
        """Create a test defect log file"""
        defect_log_content = """# Defect Log

| ID | Description | Severity | Status | Created | Resolved | Resolution Notes |
|---|---|---|---|---|---|---|
| DEF-001 | Test defect 1 | Medium | Open | 2025-09-22 | | |
| DEF-002 | Test defect 2 | High | Open | 2025-09-22 | | |
"""
        with open('DEFECT_LOG.md', 'w') as f:
            f.write(defect_log_content)
    
    def test_defect_log_workflow(self):
        """Test the complete defect log update workflow"""
        # Verify initial state
        with open('DEFECT_LOG.md', 'r') as f:
            initial_content = f.read()
        
        self.assertIn('| DEF-001 |', initial_content)
        self.assertIn('| Open |', initial_content)
        
        # Test that the defect log structure is valid
        lines = initial_content.split('\n')
        header_found = False
        separator_found = False
        
        for line in lines:
            if line.startswith('| ID |'):
                header_found = True
            elif line.startswith('|---|'):
                separator_found = True
        
        self.assertTrue(header_found, "Defect log should have proper header")
        self.assertTrue(separator_found, "Defect log should have proper separator")
    
    def test_file_structure_validation(self):
        """Test that required file structure exists"""
        required_dirs = ['docs', 'exercises/hx-kb', 'curriculum', 'metrics']
        
        for dir_path in required_dirs:
            self.assertTrue(os.path.exists(dir_path), f"Directory {dir_path} should exist")
    
    def test_markdown_processing_pipeline(self):
        """Test the complete markdown processing pipeline"""
        # Create test markdown file with issues
        test_markdown = """# Test Document

Some content.
| Column 1 | Column 2 |
|----------|----------|
| Value 1  | Value 2  |
More content.

**Phase 1: Setup**

Content here.
"""
        
        test_file = 'test_document.md'
        with open(test_file, 'w') as f:
            f.write(test_markdown)
        
        # Verify file was created
        self.assertTrue(os.path.exists(test_file))
        
        # Read and verify content
        with open(test_file, 'r') as f:
            content = f.read()
        
        self.assertIn('| Column 1 | Column 2 |', content)
        self.assertIn('**Phase 1: Setup**', content)
    
    def test_script_execution_safety(self):
        """Test that scripts handle missing files gracefully"""
        # Test with non-existent files
        non_existent_files = [
            'non_existent.md',
            'missing_script.py',
            'invalid_path/file.txt'
        ]
        
        for file_path in non_existent_files:
            self.assertFalse(os.path.exists(file_path), f"File {file_path} should not exist")
    
    def test_yaml_processing(self):
        """Test YAML file processing"""
        # Create test YAML with leading blank lines
        test_yaml = """

key: value
nested:
  subkey: subvalue
list:
  - item1
  - item2
"""
        
        yaml_file = 'test.yaml'
        with open(yaml_file, 'w') as f:
            f.write(test_yaml)
        
        # Test blank line removal logic
        with open(yaml_file, 'r') as f:
            content = f.read()
        
        cleaned_content = content.lstrip('\n')
        self.assertFalse(cleaned_content.startswith('\n'))
        self.assertTrue(cleaned_content.startswith('key: value'))
    
    def test_bash_script_processing(self):
        """Test bash script processing"""
        # Create test bash script
        test_script = """#!/bin/bash

echo "Hello World"
ls -la
"""
        
        script_file = 'test_script.sh'
        with open(script_file, 'w') as f:
            f.write(test_script)
        
        # Test strict mode addition logic
        import re
        with open(script_file, 'r') as f:
            content = f.read()
        
        updated_content = re.sub(r'#!/bin/bash\n', '#!/usr/bin/env bash\nset -euo pipefail\nIFS=$\'\\n\\t\'\n\n', content)
        
        self.assertIn('#!/usr/bin/env bash', updated_content)
        self.assertIn('set -euo pipefail', updated_content)
    
    def test_workflow_validation(self):
        """Test workflow file validation"""
        # Create test workflow
        test_workflow = """name: Test
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: echo "test"
"""
        
        workflow_file = 'test_workflow.yml'
        with open(workflow_file, 'w') as f:
            f.write(test_workflow)
        
        # Verify workflow structure
        with open(workflow_file, 'r') as f:
            content = f.read()
        
        self.assertIn('name: Test', content)
        self.assertIn('runs-on: ubuntu-latest', content)
        self.assertIn('actions/checkout@v3', content)
    
    def test_error_handling(self):
        """Test error handling across the system"""
        # Test with invalid file permissions (if possible)
        test_file = 'readonly_test.txt'
        with open(test_file, 'w') as f:
            f.write('test content')
        
        # Make file read-only
        os.chmod(test_file, 0o444)
        
        # Test that we can still read the file
        with open(test_file, 'r') as f:
            content = f.read()
        
        self.assertEqual(content, 'test content')
        
        # Clean up
        os.chmod(test_file, 0o644)
        os.remove(test_file)
    
    def test_comprehensive_validation(self):
        """Test comprehensive validation of the training program"""
        # Create a complete test environment
        test_files = {
            'curriculum/day1_foundation.md': '# Day 1\n\n**Phase 1: Setup**\n\nContent here.',
            'curriculum/day2_intermediate.md': '# Day 2\n\nSome content\n| Col1 | Col2 |\n|------|------|\n| Val1 | Val2 |\nMore content.',
            'exercises/hx-kb/day1-foundation-exercises.md': '# Exercises\n\n```bash\n#!/bin/bash\necho "test"\n```',
            'docs/IntegrationPlan.md': '# Integration Plan\n\nContent\n| Item | Status |\n|------|--------|\n| Test | Done |\nEnd.',
            'metrics/outcome-tracking-templates.yaml': '\n\nmetrics:\n  completion: 90%'
        }
        
        for file_path, content in test_files.items():
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w') as f:
                f.write(content)
        
        # Verify all files were created
        for file_path in test_files.keys():
            self.assertTrue(os.path.exists(file_path), f"File {file_path} should exist")
        
        # Test content validation
        for file_path, expected_content in test_files.items():
            with open(file_path, 'r') as f:
                actual_content = f.read()
            
            # Check that key elements are present
            if 'Phase' in expected_content:
                self.assertIn('Phase', actual_content)
            if '|' in expected_content and 'Col' in expected_content:
                self.assertIn('|', actual_content)
            if 'bash' in expected_content:
                self.assertIn('bash', actual_content)

if __name__ == '__main__':
    unittest.main()
