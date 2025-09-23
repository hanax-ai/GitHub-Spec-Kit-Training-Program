#!/bin/bash
# Environment Validation Script for GitHub Spec Kit Training Program
# Version: 1.0
# Date: 2025-09-22

echo "=== GitHub Spec Kit Training Program - Environment Validation ==="
echo "Starting validation at: $(date '+%Y-%m-%d %H:%M:%S')"
echo ""

VALIDATION_PASSED=0
VALIDATION_FAILED=0

validate_component() {
    local component="$1"
    local command="$2"
    local expected="$3"
    
    echo -n "Validating $component... "
    if eval "$command" > /dev/null 2>&1; then
        echo "✅ PASS"
        ((VALIDATION_PASSED++))
    else
        echo "❌ FAIL"
        ((VALIDATION_FAILED++))
    fi
}

# System Components
echo "=== System Components ==="
validate_component "CA Certificates" "test \$(ls /etc/ssl/certs/ | wc -l) -gt 100"
validate_component "Git Installation" "git --version"
validate_component "Python 3.12" "python3 --version | grep -q '3.12'"
validate_component "SSH Directory" "test -d ~/.ssh && test \$(stat -c '%a' ~/.ssh) = '700'"
validate_component "Development Tools" "gcc --version && curl --version && vim --version"

# Network Configuration
echo ""
echo "=== Network Configuration ==="
validate_component "Domain Resolution" "getent hosts dev-test.hana-x.ai"
validate_component "Hosts File Entries" "grep -q 'dev-test.hana-x.ai' /etc/hosts"

# Training Environment
echo ""
echo "=== Training Environment ==="
validate_component "Training Directory" "test -d ~/training/hx-spec-kit"
validate_component "Virtual Environment" "test -d ~/training/hx-spec-kit/.venv-hx-spec-kit-py312"
validate_component "Environment Test Script" "test -f ~/training/hx-spec-kit/test_environment.py"

# Run comprehensive test
echo ""
echo "=== Comprehensive Environment Test ==="
cd ~/training/hx-spec-kit
if source .venv-hx-spec-kit-py312/bin/activate && python test_environment.py > /dev/null 2>&1; then
    echo "✅ Comprehensive test: PASS"
    ((VALIDATION_PASSED++))
else
    echo "❌ Comprehensive test: FAIL"
    ((VALIDATION_FAILED++))
fi

echo ""
echo "=== Validation Summary ==="
echo "Passed: $VALIDATION_PASSED"
echo "Failed: $VALIDATION_FAILED"
echo "Total:  $((VALIDATION_PASSED + VALIDATION_FAILED))"

if [ $VALIDATION_FAILED -eq 0 ]; then
    echo "🎉 All validations passed! Environment is ready for training."
    exit 0
else
    echo "❌ Some validations failed. Please review and fix issues."
    exit 1
fi
