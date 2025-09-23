#!/bin/bash
# Environment Status Script for GitHub Spec Kit Training Program
# Version: 1.0
# Date: 2025-09-22

echo "=== GitHub Spec Kit Training Program - Environment Status ==="
echo "Generated at: $(date '+%Y-%m-%d %H:%M:%S')"
echo ""

echo "=== Environment Information ==="
echo "Repository Location: $(pwd)"
echo "Training Environment: ~/training/hx-spec-kit/"
echo "Virtual Environment: .venv-hx-spec-kit-py312"
echo "Python Version: $(python3 --version)"
echo "Git Version: $(git --version)"
echo ""

echo "=== Quick Access Commands ==="
echo "Activate Training Environment:"
echo "  cd ~/training/hx-spec-kit && source .venv-hx-spec-kit-py312/bin/activate"
echo ""
echo "Run Environment Test:"
echo "  cd ~/training/hx-spec-kit && source .venv-hx-spec-kit-py312/bin/activate && python test_environment.py"
echo ""
echo "Validate Environment:"
echo "  cd /home/ubuntu/github_repos/GitHub-Spec-Kit-Training-Program && ./scripts/validate_env.sh"
echo ""

echo "=== Domain Resolution Status ==="
if getent hosts dev-test.hana-x.ai > /dev/null 2>&1; then
    echo "✅ dev-test.hana-x.ai: $(getent hosts dev-test.hana-x.ai)"
else
    echo "❌ dev-test.hana-x.ai: Not resolving"
fi

echo ""
echo "=== Virtual Environment Status ==="
if [ -d ~/training/hx-spec-kit/.venv-hx-spec-kit-py312 ]; then
    echo "✅ Virtual Environment: Available"
    echo "   Location: ~/training/hx-spec-kit/.venv-hx-spec-kit-py312"
else
    echo "❌ Virtual Environment: Not found"
fi

echo ""
echo "=== Available Scripts ==="
echo "Setup Environment:    ./scripts/setup_test_env.sh"
echo "Validate Environment: ./scripts/validate_env.sh"
echo "Environment Status:   ./scripts/env_status.sh"
echo ""

echo "=== Documentation ==="
echo "Setup Guide:          docs/environment/baseline_training_environment_setup.md"
echo "Readiness Log:        docs/environment/ENV_READINESS.md"
echo "Setup Report:         docs/environment/TEST_ENV_SETUP_REPORT.md"
echo ""

echo "=== Training Readiness ==="
if [ -f ~/training/hx-spec-kit/test_environment.py ] && [ -d ~/training/hx-spec-kit/.venv-hx-spec-kit-py312 ]; then
    echo "🎉 Environment Status: READY FOR TRAINING"
else
    echo "⚠️  Environment Status: SETUP INCOMPLETE"
fi
