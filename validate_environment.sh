#!/bin/bash

# GitHub Spec Kit Environment Validation Script
# Compatible with Linux, macOS, and WSL2 on Windows 11
# Version: 1.0
# Date: September 22, 2025

set -e

echo "=========================================="
echo "GitHub Spec Kit Environment Validation"
echo "=========================================="
echo "Date: $(date)"
echo "System: $(uname -a)"
echo ""

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Validation results
VALIDATION_RESULTS=()
CRITICAL_FAILURES=0
WARNINGS=0

# Function to check command availability
check_command() {
    local cmd=$1
    local name=$2
    local required=${3:-true}
    
    if command -v "$cmd" >/dev/null 2>&1; then
        local version=$($cmd --version 2>/dev/null | head -n1 || echo "Version unknown")
        echo -e "${GREEN}✓${NC} $name: Found ($version)"
        VALIDATION_RESULTS+=("✓ $name: Available")
        return 0
    else
        if [ "$required" = "true" ]; then
            echo -e "${RED}✗${NC} $name: Not found (REQUIRED)"
            VALIDATION_RESULTS+=("✗ $name: Missing (CRITICAL)")
            ((CRITICAL_FAILURES++))
        else
            echo -e "${YELLOW}⚠${NC} $name: Not found (OPTIONAL)"
            VALIDATION_RESULTS+=("⚠ $name: Missing (OPTIONAL)")
            ((WARNINGS++))
        fi
        return 1
    fi
}

# Function to check Python version
check_python_version() {
    echo -e "${BLUE}Checking Python version...${NC}"
    
    if command -v python3 >/dev/null 2>&1; then
        local python_version=$(python3 --version 2>&1 | cut -d' ' -f2)
        local major=$(echo $python_version | cut -d'.' -f1)
        local minor=$(echo $python_version | cut -d'.' -f2)
        
        if [ "$major" -eq 3 ] && [ "$minor" -ge 11 ]; then
            echo -e "${GREEN}✓${NC} Python 3.11+: Found (Python $python_version)"
            VALIDATION_RESULTS+=("✓ Python 3.11+: Available ($python_version)")
            return 0
        else
            echo -e "${RED}✗${NC} Python 3.11+: Found Python $python_version but need 3.11+ (REQUIRED)"
            VALIDATION_RESULTS+=("✗ Python 3.11+: Insufficient version ($python_version)")
            ((CRITICAL_FAILURES++))
            return 1
        fi
    else
        echo -e "${RED}✗${NC} Python 3.11+: Not found (REQUIRED)"
        VALIDATION_RESULTS+=("✗ Python 3.11+: Missing")
        ((CRITICAL_FAILURES++))
        return 1
    fi
}

# Function to check WSL2 on Windows
check_wsl2() {
    if [[ "$OSTYPE" == "linux-gnu"* ]] && grep -qi microsoft /proc/version 2>/dev/null; then
        echo -e "${GREEN}✓${NC} WSL2: Detected (Windows Subsystem for Linux)"
        VALIDATION_RESULTS+=("✓ WSL2: Available")
        
        # Check WSL version
        if command -v wsl.exe >/dev/null 2>&1; then
            local wsl_version=$(wsl.exe --version 2>/dev/null | head -n1 || echo "Version unknown")
            echo -e "${GREEN}  ${NC} WSL Version: $wsl_version"
        fi
        return 0
    elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "cygwin" ]]; then
        echo -e "${YELLOW}⚠${NC} Windows detected but not WSL2. Consider using WSL2 for better compatibility."
        VALIDATION_RESULTS+=("⚠ WSL2: Not detected (Windows native)")
        ((WARNINGS++))
        return 1
    else
        echo -e "${BLUE}ℹ${NC} WSL2: Not applicable (Linux/macOS system)"
        VALIDATION_RESULTS+=("ℹ WSL2: Not applicable")
        return 0
    fi
}

# Function to check AI coding agents
check_ai_agents() {
    echo -e "${BLUE}Checking AI Coding Agents...${NC}"
    local agents_found=0
    
    # List of supported AI agents
    local agents=(
        "claude:Claude Code"
        "copilot:GitHub Copilot"
        "gemini:Gemini CLI"
        "cursor:Cursor"
        "qwen:Qwen CLI"
        "opencode:OpenCode"
        "codex:Codex CLI"
        "windsurf:Windsurf"
    )
    
    for agent_info in "${agents[@]}"; do
        local cmd=$(echo $agent_info | cut -d':' -f1)
        local name=$(echo $agent_info | cut -d':' -f2)
        
        if command -v "$cmd" >/dev/null 2>&1; then
            echo -e "${GREEN}✓${NC} $name: Found"
            ((agents_found++))
        fi
    done
    
    # Check for VS Code (often used with GitHub Copilot)
    if command -v code >/dev/null 2>&1; then
        echo -e "${GREEN}✓${NC} VS Code: Found (GitHub Copilot compatible)"
        ((agents_found++))
    fi
    
    if [ $agents_found -eq 0 ]; then
        echo -e "${RED}✗${NC} AI Coding Agents: None found (REQUIRED)"
        echo -e "${YELLOW}  ${NC} Install at least one: Claude Code, GitHub Copilot, Gemini CLI, Cursor, etc."
        VALIDATION_RESULTS+=("✗ AI Coding Agents: None available")
        ((CRITICAL_FAILURES++))
        return 1
    else
        echo -e "${GREEN}✓${NC} AI Coding Agents: $agents_found agent(s) found"
        VALIDATION_RESULTS+=("✓ AI Coding Agents: $agents_found available")
        return 0
    fi
}

# Function to test GitHub Spec Kit installation
test_spec_kit_install() {
    echo -e "${BLUE}Testing GitHub Spec Kit installation...${NC}"
    
    # Create a temporary directory for testing
    local test_dir="/tmp/spec_kit_test_$$"
    mkdir -p "$test_dir"
    cd "$test_dir"
    
    # Try to initialize a test project
    if uvx --from git+https://github.com/github/spec-kit.git specify init test_project --debug 2>/dev/null; then
        echo -e "${GREEN}✓${NC} GitHub Spec Kit: Installation test successful"
        VALIDATION_RESULTS+=("✓ GitHub Spec Kit: Installation works")
        
        # Check if files were created
        if [ -d "test_project" ]; then
            echo -e "${GREEN}  ${NC} Project structure created successfully"
            ls -la test_project/ 2>/dev/null | head -5
        fi
        
        # Cleanup
        rm -rf "$test_dir"
        return 0
    else
        echo -e "${RED}✗${NC} GitHub Spec Kit: Installation test failed"
        VALIDATION_RESULTS+=("✗ GitHub Spec Kit: Installation failed")
        ((CRITICAL_FAILURES++))
        
        # Cleanup
        rm -rf "$test_dir"
        return 1
    fi
}

# Function to check network connectivity
check_network() {
    echo -e "${BLUE}Checking network connectivity...${NC}"
    
    if ping -c 1 github.com >/dev/null 2>&1; then
        echo -e "${GREEN}✓${NC} GitHub connectivity: Available"
        VALIDATION_RESULTS+=("✓ Network: GitHub accessible")
    else
        echo -e "${RED}✗${NC} GitHub connectivity: Failed"
        VALIDATION_RESULTS+=("✗ Network: GitHub not accessible")
        ((CRITICAL_FAILURES++))
    fi
    
    if ping -c 1 pypi.org >/dev/null 2>&1; then
        echo -e "${GREEN}✓${NC} PyPI connectivity: Available"
        VALIDATION_RESULTS+=("✓ Network: PyPI accessible")
    else
        echo -e "${YELLOW}⚠${NC} PyPI connectivity: Failed"
        VALIDATION_RESULTS+=("⚠ Network: PyPI not accessible")
        ((WARNINGS++))
    fi
}

# Main validation sequence
main() {
    echo -e "${BLUE}Starting environment validation...${NC}"
    echo ""
    
    # Core system checks
    echo -e "${BLUE}=== Core System Requirements ===${NC}"
    check_wsl2
    check_python_version
    check_command "git" "Git" true
    check_command "uv" "UV Package Manager" true
    echo ""
    
    # AI agents check
    echo -e "${BLUE}=== AI Coding Agents ===${NC}"
    check_ai_agents
    echo ""
    
    # Network connectivity
    echo -e "${BLUE}=== Network Connectivity ===${NC}"
    check_network
    echo ""
    
    # GitHub Spec Kit installation test
    echo -e "${BLUE}=== GitHub Spec Kit Test ===${NC}"
    if [ $CRITICAL_FAILURES -eq 0 ]; then
        test_spec_kit_install
    else
        echo -e "${YELLOW}⚠${NC} Skipping Spec Kit test due to missing prerequisites"
        VALIDATION_RESULTS+=("⚠ GitHub Spec Kit: Skipped due to prerequisites")
    fi
    echo ""
    
    # Optional tools
    echo -e "${BLUE}=== Optional Tools ===${NC}"
    check_command "docker" "Docker" false
    check_command "node" "Node.js" false
    check_command "npm" "NPM" false
    check_command "curl" "cURL" false
    check_command "wget" "wget" false
    echo ""
    
    # Summary
    echo -e "${BLUE}=== Validation Summary ===${NC}"
    echo "Total checks performed: ${#VALIDATION_RESULTS[@]}"
    echo -e "Critical failures: ${RED}$CRITICAL_FAILURES${NC}"
    echo -e "Warnings: ${YELLOW}$WARNINGS${NC}"
    echo ""
    
    if [ $CRITICAL_FAILURES -eq 0 ]; then
        echo -e "${GREEN}🎉 Environment validation PASSED!${NC}"
        echo -e "${GREEN}Your system is ready for GitHub Spec Kit training.${NC}"
        echo ""
        echo -e "${BLUE}Next steps:${NC}"
        echo "1. Install any missing optional tools if needed"
        echo "2. Configure your preferred AI coding agent"
        echo "3. Begin the intensive training program"
        return 0
    else
        echo -e "${RED}❌ Environment validation FAILED!${NC}"
        echo -e "${RED}Please address the critical failures before proceeding.${NC}"
        echo ""
        echo -e "${BLUE}Required actions:${NC}"
        
        if ! command -v python3 >/dev/null 2>&1 || ! python3 -c "import sys; exit(0 if sys.version_info >= (3, 11) else 1)" 2>/dev/null; then
            echo "• Install Python 3.11 or higher"
        fi
        
        if ! command -v git >/dev/null 2>&1; then
            echo "• Install Git"
        fi
        
        if ! command -v uv >/dev/null 2>&1; then
            echo "• Install UV package manager: pip install uv"
        fi
        
        echo "• Install at least one AI coding agent (Claude Code, GitHub Copilot, etc.)"
        echo "• Ensure network connectivity to GitHub and PyPI"
        
        return 1
    fi
}

# Installation help
show_installation_help() {
    echo -e "${BLUE}=== Installation Help ===${NC}"
    echo ""
    echo -e "${YELLOW}For Ubuntu/Debian:${NC}"
    echo "sudo apt update"
    echo "sudo apt install python3.11 python3.11-pip git curl"
    echo "pip3 install uv"
    echo ""
    echo -e "${YELLOW}For macOS:${NC}"
    echo "brew install python@3.11 git"
    echo "pip3 install uv"
    echo ""
    echo -e "${YELLOW}For Windows 11 (WSL2):${NC}"
    echo "1. Enable WSL2: wsl --install"
    echo "2. Install Ubuntu from Microsoft Store"
    echo "3. Run Ubuntu and follow Ubuntu/Debian instructions above"
    echo ""
    echo -e "${YELLOW}AI Coding Agents:${NC}"
    echo "• GitHub Copilot: Install VS Code + GitHub Copilot extension"
    echo "• Claude Code: Visit https://claude.ai/code"
    echo "• Cursor: Download from https://cursor.sh/"
    echo ""
}

# Handle command line arguments
case "${1:-}" in
    --help|-h)
        echo "GitHub Spec Kit Environment Validation Script"
        echo ""
        echo "Usage: $0 [OPTIONS]"
        echo ""
        echo "Options:"
        echo "  --help, -h     Show this help message"
        echo "  --install-help Show installation instructions"
        echo "  --quiet, -q    Suppress verbose output"
        echo ""
        exit 0
        ;;
    --install-help)
        show_installation_help
        exit 0
        ;;
    --quiet|-q)
        exec >/dev/null 2>&1
        ;;
esac

# Run main validation
main
exit_code=$?

# Save results to file
{
    echo "GitHub Spec Kit Environment Validation Results"
    echo "Date: $(date)"
    echo "System: $(uname -a)"
    echo ""
    echo "Validation Results:"
    printf '%s\n' "${VALIDATION_RESULTS[@]}"
    echo ""
    echo "Summary:"
    echo "Critical failures: $CRITICAL_FAILURES"
    echo "Warnings: $WARNINGS"
    echo "Status: $([ $exit_code -eq 0 ] && echo "PASSED" || echo "FAILED")"
} > "/tmp/spec_kit_validation_$(date +%Y%m%d_%H%M%S).log"

echo -e "${BLUE}Validation results saved to: /tmp/spec_kit_validation_$(date +%Y%m%d_%H%M%S).log${NC}"

exit $exit_code
