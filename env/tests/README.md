
# Unit Tests for GitHub Spec Kit Training Program

This directory contains comprehensive unit tests for the GitHub Spec Kit Training Program Python scripts and functionality.

## Test Structure

### Test Files

- `test_update_defect_log.py` - Tests for defect log update functionality
- `test_fix_defects.py` - Tests for defect fixing functionality  
- `test_fix_workflows.py` - Tests for workflow fixing functionality
- `test_integration.py` - Integration tests for the complete system
- `run_tests.py` - Test runner script

### Test Coverage

The test suite covers:

1. **Defect Log Management**
   - Reading and parsing defect logs
   - Updating defect status and resolution notes
   - Date formatting and validation
   - File I/O operations

2. **Defect Fixing Functionality**
   - Markdown table formatting (MD058)
   - Bold heading conversion (MD036)
   - YAML blank line removal
   - Bash script strict mode addition
   - Sed command variable expansion fixes
   - File operation safety checks

3. **Workflow Management**
   - GitHub Actions version pinning
   - Conditional script execution
   - Permissions block addition
   - Regex pattern validation
   - Error handling

4. **Integration Testing**
   - End-to-end workflow validation
   - File structure verification
   - Content processing pipelines
   - Error handling across components

## Running Tests

### Run All Tests
```bash
python3 tests/run_tests.py
```

### Run Specific Test Module
```bash
python3 tests/run_tests.py test_update_defect_log
python3 tests/run_tests.py test_fix_defects
python3 tests/run_tests.py test_fix_workflows
python3 tests/run_tests.py test_integration
```

### Run Individual Test Files
```bash
python3 -m unittest tests.test_update_defect_log
python3 -m unittest tests.test_fix_defects
python3 -m unittest tests.test_fix_workflows
python3 -m unittest tests.test_integration
```

### Run with Verbose Output
```bash
python3 -m unittest tests.test_update_defect_log -v
```

## Test Requirements

The tests use Python's built-in `unittest` framework and require no additional dependencies beyond the standard library.

Optional testing enhancements are listed in `requirements-test.txt` but are not required for basic test execution.

## Test Design Principles

### 1. **Isolation**
- Each test is independent and can run in isolation
- Tests use mocking to avoid file system dependencies where appropriate
- Temporary directories are used for integration tests

### 2. **Comprehensive Coverage**
- Tests cover both happy path and error conditions
- Edge cases and boundary conditions are tested
- Integration tests validate end-to-end functionality

### 3. **Maintainability**
- Tests are well-documented with clear descriptions
- Test data is organized and reusable
- Helper methods reduce code duplication

### 4. **Safety**
- Tests never modify actual project files
- Temporary files and directories are properly cleaned up
- File permissions and error conditions are handled gracefully

## Test Data

Test fixtures include:
- Sample defect log entries
- Markdown files with various formatting issues
- YAML files with blank line problems
- Bash scripts requiring strict mode
- GitHub workflow files needing updates

## Continuous Integration

These tests are designed to run in CI/CD environments and provide:
- Clear pass/fail status
- Detailed error reporting
- Performance benchmarks
- Coverage reporting (when using pytest-cov)

## Contributing

When adding new functionality:
1. Add corresponding unit tests
2. Ensure tests cover both success and failure cases
3. Update this README if new test categories are added
4. Run the full test suite before submitting changes

## Test Results Interpretation

- **PASS**: All functionality working correctly
- **FAIL**: Specific functionality broken, check error details
- **ERROR**: Test setup or infrastructure issue
- **SKIP**: Test skipped due to missing dependencies or conditions

For detailed test output and debugging information, run tests with the `-v` (verbose) flag.
