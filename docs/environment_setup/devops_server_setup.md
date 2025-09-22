
# DevOps Server Environment Setup for GitHub Spec Kit
## Linux Server Installation and Configuration Guide

**Target Environment:** Linux DevOps Server in HX-Infrastructure landscape  
**Prerequisites:** SSH access, sudo privileges  
**Estimated Time:** 20-40 minutes  
**Compatibility:** Native Linux support for GitHub Spec Kit

---

## 🎯 Overview

GitHub Spec Kit runs natively on Linux servers, providing optimal performance and compatibility. This guide covers setup for common Linux distributions used in DevOps environments.

## 📋 Prerequisites Checklist

Before starting, ensure you have:
- [ ] SSH access to the DevOps server
- [ ] Sudo privileges or root access
- [ ] Internet connectivity from the server
- [ ] At least 2GB free disk space
- [ ] Basic familiarity with Linux command line

## 🚀 Step-by-Step Installation

### Step 1: Server Environment Assessment (5 minutes)

#### 1.1 System Information Gathering

```bash
# Connect to your DevOps server
ssh username@your-devops-server.hx-infrastructure.com

# Check system information
uname -a
cat /etc/os-release
df -h
free -h
```

#### 1.2 Supported Distributions

**Tested and Supported:**
- Ubuntu 20.04 LTS, 22.04 LTS, 24.04 LTS
- CentOS 7, 8, Stream
- RHEL 7, 8, 9
- Amazon Linux 2
- Debian 10, 11, 12
- SUSE Linux Enterprise Server

**Architecture Support:**
- x86_64 (Intel/AMD 64-bit)
- ARM64 (AArch64)

### Step 2: Update System and Install Dependencies (10-15 minutes)

#### 2.1 Ubuntu/Debian Systems

```bash
# Update package lists and system
sudo apt update && sudo apt upgrade -y

# Install essential development tools
sudo apt install -y curl wget git build-essential software-properties-common

# Install Python 3.11 (required for GitHub Spec Kit)
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update
sudo apt install -y python3.11 python3.11-pip python3.11-venv python3.11-dev

# Set Python 3.11 as default python3 (if needed)
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1

# Install additional useful tools
sudo apt install -y htop tree vim nano jq unzip
```

#### 2.2 CentOS/RHEL/Amazon Linux Systems

```bash
# Update system packages
sudo yum update -y
# OR for newer versions:
# sudo dnf update -y

# Install development tools
sudo yum groupinstall -y "Development Tools"
# OR: sudo dnf groupinstall -y "Development Tools"

# Install EPEL repository (for additional packages)
sudo yum install -y epel-release
# OR: sudo dnf install -y epel-release

# Install essential tools
sudo yum install -y curl wget git vim nano htop tree jq unzip
# OR: sudo dnf install -y curl wget git vim nano htop tree jq unzip

# Install Python 3.11 (compile from source if not available in repos)
sudo yum install -y gcc openssl-devel bzip2-devel libffi-devel zlib-devel
# OR: sudo dnf install -y gcc openssl-devel bzip2-devel libffi-devel zlib-devel

# Download and compile Python 3.11
cd /tmp
wget https://www.python.org/ftp/python/3.11.9/Python-3.11.9.tgz
tar -xf Python-3.11.9.tgz
cd Python-3.11.9
./configure --enable-optimizations
make -j$(nproc)
sudo make altinstall

# Create symlink for python3
sudo ln -sf /usr/local/bin/python3.11 /usr/local/bin/python3
```

#### 2.3 SUSE Linux Enterprise Server

```bash
# Update system
sudo zypper update -y

# Install development tools
sudo zypper install -y -t pattern devel_basis

# Install essential tools
sudo zypper install -y curl wget git vim nano htop tree jq unzip

# Install Python 3.11 (may need to compile from source)
sudo zypper install -y gcc libopenssl-devel libbz2-devel libffi-devel zlib-devel

# Follow Python compilation steps from CentOS section if needed
```

### Step 3: Install UV Package Manager (5 minutes)

```bash
# Install UV (Python package manager required for Spec Kit)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Reload shell configuration
source ~/.bashrc

# Verify UV installation
uv --version

# If UV is not in PATH, add it manually
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

### Step 4: Configure Git (5 minutes)

```bash
# Configure Git with your information
git config --global user.name "Your Name"
git config --global user.email "your.email@hx-infrastructure.com"

# Configure Git for server environment
git config --global init.defaultBranch main
git config --global pull.rebase false

# Verify Git configuration
git config --list
```

### Step 5: Install AI Coding Agent (10-15 minutes)

#### Option A: GitHub Copilot CLI (Recommended for servers)

```bash
# Install Node.js (required for GitHub Copilot CLI)
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs
# OR for CentOS/RHEL:
# curl -fsSL https://rpm.nodesource.com/setup_lts.x | sudo bash -
# sudo yum install -y nodejs

# Install GitHub Copilot CLI
npm install -g @githubnext/github-copilot-cli

# Authenticate with GitHub
github-copilot-cli auth login
```

#### Option B: Claude Code (if available)

```bash
# Follow Claude Code installation instructions for Linux
# Visit: https://claude.ai/code for latest instructions
```

#### Option C: Server-Optimized Setup

For servers without GUI or direct AI agent access:

```bash
# Create configuration for remote AI agent usage
mkdir -p ~/.config/spec-kit
cat > ~/.config/spec-kit/config.yaml << EOF
ai_agent:
  type: "remote"
  endpoint: "your-ai-service-endpoint"
  api_key: "your-api-key"
EOF
```

### Step 6: Test GitHub Spec Kit Installation (5-10 minutes)

```bash
# Create test directory
mkdir -p ~/spec_kit_test
cd ~/spec_kit_test

# Test Spec Kit installation
uvx --from git+https://github.com/github/spec-kit.git specify init test_project

# Verify installation
cd test_project
ls -la

# Check project structure
tree . || find . -type f | head -10
```

### Step 7: Configure Server-Specific Settings (5 minutes)

#### 7.1 Environment Variables

```bash
# Add environment variables for server operation
cat >> ~/.bashrc << EOF

# GitHub Spec Kit Configuration
export SPECIFY_ENVIRONMENT="devops-server"
export SPECIFY_LOG_LEVEL="INFO"
export SPECIFY_CACHE_DIR="$HOME/.cache/specify"

# HX-Infrastructure specific settings
export HX_INFRA_ENV="devops"
export HX_INFRA_SERVER="$(hostname)"

EOF

source ~/.bashrc
```

#### 7.2 Create Working Directories

```bash
# Create organized directory structure
mkdir -p ~/hx-infrastructure/{projects,templates,scripts,logs}
mkdir -p ~/.cache/specify
mkdir -p ~/.local/share/specify

# Set appropriate permissions
chmod 755 ~/hx-infrastructure
chmod 700 ~/.cache/specify ~/.local/share/specify
```

## 🔧 Troubleshooting Common Issues

### Issue 1: Python 3.11 Not Available in Package Manager

**Symptoms:** Package manager can't find Python 3.11

**Solutions:**
1. **Compile from Source:**
   ```bash
   # Install build dependencies
   sudo apt install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev
   
   # Download and compile Python 3.11
   cd /tmp
   wget https://www.python.org/ftp/python/3.11.9/Python-3.11.9.tgz
   tar -xf Python-3.11.9.tgz
   cd Python-3.11.9
   ./configure --enable-optimizations
   make -j$(nproc)
   sudo make altinstall
   
   # Create symlinks
   sudo ln -sf /usr/local/bin/python3.11 /usr/local/bin/python3
   sudo ln -sf /usr/local/bin/pip3.11 /usr/local/bin/pip3
   ```

2. **Use pyenv:**
   ```bash
   # Install pyenv
   curl https://pyenv.run | bash
   
   # Add to shell configuration
   echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
   echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
   echo 'eval "$(pyenv init -)"' >> ~/.bashrc
   source ~/.bashrc
   
   # Install Python 3.11
   pyenv install 3.11.9
   pyenv global 3.11.9
   ```

### Issue 2: UV Installation Fails

**Symptoms:** UV installer script fails or command not found

**Solutions:**
1. **Manual Installation:**
   ```bash
   # Install via pip
   python3 -m pip install --user uv
   
   # Add to PATH
   echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
   source ~/.bashrc
   ```

2. **Alternative Installation:**
   ```bash
   # Download binary directly
   curl -LsSf https://github.com/astral-sh/uv/releases/latest/download/uv-installer.sh | sh
   ```

### Issue 3: Network Connectivity Issues

**Symptoms:** Cannot reach GitHub or PyPI

**Solutions:**
1. **Check Firewall Settings:**
   ```bash
   # Test connectivity
   curl -I https://github.com
   curl -I https://pypi.org
   
   # Check firewall rules
   sudo iptables -L
   # OR: sudo firewall-cmd --list-all
   ```

2. **Configure Proxy (if needed):**
   ```bash
   # Set proxy environment variables
   export http_proxy=http://proxy.hx-infrastructure.com:8080
   export https_proxy=http://proxy.hx-infrastructure.com:8080
   export no_proxy=localhost,127.0.0.1,.hx-infrastructure.com
   
   # Add to ~/.bashrc for persistence
   echo 'export http_proxy=http://proxy.hx-infrastructure.com:8080' >> ~/.bashrc
   echo 'export https_proxy=http://proxy.hx-infrastructure.com:8080' >> ~/.bashrc
   echo 'export no_proxy=localhost,127.0.0.1,.hx-infrastructure.com' >> ~/.bashrc
   ```

### Issue 4: Permission Issues

**Symptoms:** Permission denied errors during installation

**Solutions:**
1. **Fix Directory Permissions:**
   ```bash
   # Fix home directory permissions
   chmod 755 ~
   chmod -R 755 ~/.local
   
   # Create directories with correct permissions
   mkdir -p ~/.local/bin ~/.local/lib ~/.cache
   chmod 755 ~/.local/bin ~/.local/lib ~/.cache
   ```

2. **Use User Installation:**
   ```bash
   # Install packages to user directory
   python3 -m pip install --user uv
   uvx --help  # Should work without sudo
   ```

### Issue 5: AI Agent Integration Issues

**Symptoms:** AI agent not accessible or not working

**Solutions:**
1. **Server Environment Configuration:**
   ```bash
   # Configure for headless operation
   export SPECIFY_AI_MODE="cli"
   export SPECIFY_HEADLESS="true"
   
   # Use remote AI service if available
   export SPECIFY_AI_ENDPOINT="https://your-ai-service.hx-infrastructure.com"
   ```

2. **Alternative AI Integration:**
   ```bash
   # Use API-based AI services
   pip3 install --user openai anthropic
   
   # Configure API keys (store securely)
   echo 'export OPENAI_API_KEY="your-key-here"' >> ~/.bashrc
   echo 'export ANTHROPIC_API_KEY="your-key-here"' >> ~/.bashrc
   ```

## ✅ Server Validation Script

Create and run this comprehensive validation script:

```bash
#!/bin/bash
# Save as validate_devops_server.sh

echo "=== DevOps Server GitHub Spec Kit Environment Validation ==="
echo "Server: $(hostname)"
echo "Date: $(date)"
echo ""

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

FAILURES=0

# Check OS
echo "Checking Operating System..."
if [ -f /etc/os-release ]; then
    . /etc/os-release
    echo -e "${GREEN}✓${NC} OS: $PRETTY_NAME"
else
    echo -e "${RED}✗${NC} Cannot determine OS"
    ((FAILURES++))
fi

# Check Python 3.11+
echo "Checking Python 3.11+..."
if command -v python3 >/dev/null 2>&1; then
    python_version=$(python3 --version 2>&1 | cut -d' ' -f2)
    if python3 -c "import sys; exit(0 if sys.version_info >= (3, 11) else 1)" 2>/dev/null; then
        echo -e "${GREEN}✓${NC} Python 3.11+ found: $python_version"
    else
        echo -e "${RED}✗${NC} Python 3.11+ required, found: $python_version"
        ((FAILURES++))
    fi
else
    echo -e "${RED}✗${NC} Python 3 not found"
    ((FAILURES++))
fi

# Check Git
echo "Checking Git..."
if command -v git >/dev/null 2>&1; then
    git_version=$(git --version)
    echo -e "${GREEN}✓${NC} Git found: $git_version"
else
    echo -e "${RED}✗${NC} Git not found"
    ((FAILURES++))
fi

# Check UV
echo "Checking UV..."
if command -v uv >/dev/null 2>&1; then
    uv_version=$(uv --version)
    echo -e "${GREEN}✓${NC} UV found: $uv_version"
else
    echo -e "${RED}✗${NC} UV not found"
    ((FAILURES++))
fi

# Check network connectivity
echo "Checking network connectivity..."
if curl -s --connect-timeout 5 https://github.com >/dev/null; then
    echo -e "${GREEN}✓${NC} GitHub accessible"
else
    echo -e "${RED}✗${NC} GitHub not accessible"
    ((FAILURES++))
fi

if curl -s --connect-timeout 5 https://pypi.org >/dev/null; then
    echo -e "${GREEN}✓${NC} PyPI accessible"
else
    echo -e "${YELLOW}⚠${NC} PyPI not accessible (may affect package installation)"
fi

# Check disk space
echo "Checking disk space..."
available_space=$(df ~ | tail -1 | awk '{print $4}')
if [ "$available_space" -gt 2097152 ]; then  # 2GB in KB
    echo -e "${GREEN}✓${NC} Sufficient disk space available"
else
    echo -e "${YELLOW}⚠${NC} Low disk space (less than 2GB available)"
fi

# Test GitHub Spec Kit
echo "Testing GitHub Spec Kit installation..."
temp_dir="/tmp/spec_kit_server_test_$$"
mkdir -p "$temp_dir"
cd "$temp_dir"

if timeout 60 uvx --from git+https://github.com/github/spec-kit.git specify init server_validation_test >/dev/null 2>&1; then
    echo -e "${GREEN}✓${NC} GitHub Spec Kit installation successful"
    rm -rf "$temp_dir"
else
    echo -e "${RED}✗${NC} GitHub Spec Kit installation failed"
    ((FAILURES++))
    rm -rf "$temp_dir"
fi

# Check server-specific configurations
echo "Checking server configuration..."
if [ -d ~/.config/spec-kit ] || [ -f ~/.bashrc ]; then
    echo -e "${GREEN}✓${NC} Configuration directories present"
else
    echo -e "${YELLOW}⚠${NC} Configuration may need setup"
fi

# Summary
echo ""
echo "=== Validation Summary ==="
if [ $FAILURES -eq 0 ]; then
    echo -e "${GREEN}🎉 Server validation PASSED!${NC}"
    echo "Your DevOps server is ready for GitHub Spec Kit training."
else
    echo -e "${RED}❌ Server validation FAILED with $FAILURES critical issues.${NC}"
    echo "Please address the issues above before proceeding."
fi

echo ""
echo "Server Information:"
echo "- Hostname: $(hostname)"
echo "- Uptime: $(uptime)"
echo "- Load: $(cat /proc/loadavg)"
echo "- Memory: $(free -h | grep Mem | awk '{print $3 "/" $2}')"
echo "- Disk: $(df -h ~ | tail -1 | awk '{print $3 "/" $2 " (" $5 " used)"}')"

exit $FAILURES
```

Run the validation:
```bash
chmod +x validate_devops_server.sh
./validate_devops_server.sh
```

## 🎯 Next Steps

After successful setup:

1. **Run Comprehensive Validation:**
   ```bash
   cd /home/ubuntu/github_spec_training
   ./validate_environment.sh
   ```

2. **Configure HX-Infrastructure Integration:**
   ```bash
   # Clone HX-Infrastructure-Knowledge-Base
   git clone https://github.com/hanax-ai/HX-Infrastructure-Knowledge-Base.git
   ```

3. **Begin Training:**
   ```bash
   cd curriculum
   cat day1_foundation.md
   ```

## 📚 Additional Resources

### Linux Server Management:
- [Ubuntu Server Guide](https://ubuntu.com/server/docs)
- [CentOS/RHEL Documentation](https://docs.redhat.com/)
- [Linux System Administration](https://www.tldp.org/LDP/sag/html/)

### DevOps Best Practices:
- [Infrastructure as Code](https://www.terraform.io/docs)
- [Configuration Management](https://docs.ansible.com/)
- [Monitoring and Logging](https://prometheus.io/docs/)

### Security Considerations:
- [Linux Security Hardening](https://www.cisecurity.org/cis-benchmarks/)
- [SSH Security Best Practices](https://www.ssh.com/academy/ssh/security)
- [Firewall Configuration](https://help.ubuntu.com/community/UFW)

---

**Server Setup Complete!** Your DevOps server environment is now optimized for GitHub Spec Kit training and production use. The native Linux environment provides excellent performance and compatibility.

*Estimated total setup time: 20-40 minutes*  
*Next: Begin Day 1 Foundation Training*
