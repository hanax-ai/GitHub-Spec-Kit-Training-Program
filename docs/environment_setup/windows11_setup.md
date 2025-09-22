
# Windows 11 Environment Setup for GitHub Spec Kit
## Complete Installation and Configuration Guide

**Target Environment:** Windows 11 PC  
**Prerequisites:** Administrator access, internet connection  
**Estimated Time:** 30-60 minutes  
**Compatibility:** GitHub Spec Kit via WSL2

---

## 🎯 Overview

GitHub Spec Kit requires a Linux/Unix environment to function properly. On Windows 11, this is achieved through Windows Subsystem for Linux 2 (WSL2), which provides excellent compatibility and performance.

## 📋 Prerequisites Checklist

Before starting, ensure you have:
- [ ] Windows 11 (Build 19041 or higher)
- [ ] Administrator privileges on your PC
- [ ] Stable internet connection
- [ ] At least 4GB free disk space
- [ ] Windows Terminal (recommended, usually pre-installed)

## 🚀 Step-by-Step Installation

### Step 1: Enable WSL2 (15-20 minutes)

#### 1.1 Install WSL2 via Command Line (Recommended)

Open PowerShell as Administrator and run:

```powershell
# Install WSL2 with Ubuntu (default distribution)
wsl --install

# If you already have WSL1, upgrade to WSL2
wsl --set-default-version 2
```

**Expected Output:**
```
Installing: Windows Subsystem for Linux
Installing: Virtual Machine Platform
Installing: Ubuntu
The requested operation is successful. Changes will not be effective until the system is rebooted.
```

#### 1.2 Alternative: Manual Installation

If the automatic installation fails:

1. **Enable WSL Feature:**
   ```powershell
   dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
   ```

2. **Enable Virtual Machine Platform:**
   ```powershell
   dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
   ```

3. **Restart your computer**

4. **Download and install WSL2 Linux kernel update:**
   - Visit: https://aka.ms/wsl2kernel
   - Download and install the update package

5. **Set WSL2 as default:**
   ```powershell
   wsl --set-default-version 2
   ```

#### 1.3 Install Ubuntu Distribution

```powershell
# Install Ubuntu (if not installed automatically)
wsl --install -d Ubuntu

# List available distributions
wsl --list --online
```

### Step 2: Configure Ubuntu Environment (10-15 minutes)

#### 2.1 Initial Ubuntu Setup

1. **Launch Ubuntu:**
   - Open Windows Terminal
   - Click the dropdown arrow and select "Ubuntu"
   - Or type `wsl` in PowerShell

2. **Create User Account:**
   ```bash
   # You'll be prompted to create a username and password
   # Choose a simple username (e.g., your first name)
   # Remember this password - you'll need it for sudo commands
   ```

3. **Update System:**
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```

#### 2.2 Install Required Dependencies

```bash
# Install essential tools
sudo apt install -y curl wget git build-essential

# Install Python 3.11 (required for GitHub Spec Kit)
sudo apt install -y software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt update
sudo apt install -y python3.11 python3.11-pip python3.11-venv

# Set Python 3.11 as default python3
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 1

# Verify Python version
python3 --version  # Should show Python 3.11.x
```

### Step 3: Install UV Package Manager (5 minutes)

```bash
# Install UV (Python package manager required for Spec Kit)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Reload shell configuration
source ~/.bashrc

# Verify UV installation
uv --version
```

### Step 4: Configure Git (5 minutes)

```bash
# Configure Git with your information
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Verify Git configuration
git config --list
```

### Step 5: Install and Configure AI Coding Agent (10-15 minutes)

#### Option A: VS Code with GitHub Copilot (Recommended)

1. **Install VS Code on Windows:**
   - Download from: https://code.visualstudio.com/
   - Install with default settings

2. **Install WSL Extension:**
   - Open VS Code
   - Install "WSL" extension by Microsoft
   - Install "Remote Development" extension pack

3. **Install GitHub Copilot:**
   - Install "GitHub Copilot" extension
   - Install "GitHub Copilot Chat" extension
   - Sign in with your GitHub account

4. **Connect to WSL:**
   ```bash
   # From Ubuntu terminal, open VS Code in WSL
   code .
   ```

#### Option B: Claude Code

1. **Install Claude Code:**
   - Visit: https://claude.ai/code
   - Follow installation instructions for your setup

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

# Test basic functionality
# In your AI agent (VS Code with Copilot), try:
# /specify --help
```

## 🔧 Troubleshooting Common Issues

### Issue 1: WSL2 Installation Fails

**Symptoms:** Error messages during WSL installation

**Solutions:**
1. **Check Windows Version:**
   ```powershell
   winver
   ```
   Ensure you have Windows 11 Build 19041 or higher

2. **Enable Virtualization in BIOS:**
   - Restart computer and enter BIOS
   - Enable Intel VT-x or AMD-V
   - Enable Hyper-V if available

3. **Manual Feature Installation:**
   ```powershell
   # Enable features manually
   Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
   Enable-WindowsOptionalFeature -Online -FeatureName VirtualMachinePlatform
   ```

### Issue 2: Python 3.11 Installation Problems

**Symptoms:** Python 3.11 not available or installation fails

**Solutions:**
1. **Alternative Installation Method:**
   ```bash
   # Use deadsnakes PPA
   sudo apt update
   sudo apt install -y software-properties-common
   sudo add-apt-repository ppa:deadsnakes/ppa
   sudo apt update
   sudo apt install -y python3.11 python3.11-pip python3.11-venv python3.11-dev
   ```

2. **Compile from Source (if needed):**
   ```bash
   # Download and compile Python 3.11
   wget https://www.python.org/ftp/python/3.11.9/Python-3.11.9.tgz
   tar -xf Python-3.11.9.tgz
   cd Python-3.11.9
   ./configure --enable-optimizations
   make -j$(nproc)
   sudo make altinstall
   ```

### Issue 3: UV Installation Fails

**Symptoms:** UV command not found or installation errors

**Solutions:**
1. **Manual Installation:**
   ```bash
   # Alternative installation method
   pip3 install uv
   
   # Or using pipx
   pip3 install pipx
   pipx install uv
   ```

2. **Path Issues:**
   ```bash
   # Add to PATH if needed
   echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
   source ~/.bashrc
   ```

### Issue 4: GitHub Spec Kit Installation Fails

**Symptoms:** uvx command fails or Spec Kit doesn't initialize

**Solutions:**
1. **Check Prerequisites:**
   ```bash
   # Verify all requirements
   python3 --version  # Should be 3.11+
   git --version
   uv --version
   ```

2. **Network Issues:**
   ```bash
   # Test GitHub connectivity
   ping github.com
   
   # Try with different options
   uvx --from git+https://github.com/github/spec-kit.git specify init test_project --debug
   ```

3. **Alternative Installation:**
   ```bash
   # Clone repository manually
   git clone https://github.com/github/spec-kit.git
   cd spec-kit
   uv run specify init test_project
   ```

### Issue 5: VS Code WSL Integration Problems

**Symptoms:** VS Code can't connect to WSL or extensions don't work

**Solutions:**
1. **Reinstall WSL Extension:**
   - Uninstall and reinstall WSL extension in VS Code
   - Restart VS Code

2. **Reset WSL Connection:**
   ```bash
   # From Windows PowerShell
   wsl --shutdown
   wsl
   ```

3. **Check WSL Status:**
   ```powershell
   # Verify WSL is running
   wsl --list --verbose
   wsl --status
   ```

## ✅ Validation Script

Create and run this validation script to ensure everything is working:

```bash
#!/bin/bash
# Save as validate_windows_setup.sh

echo "=== Windows 11 GitHub Spec Kit Environment Validation ==="
echo ""

# Check WSL2
echo "Checking WSL2..."
if grep -qi microsoft /proc/version; then
    echo "✓ WSL2 detected"
else
    echo "✗ WSL2 not detected"
fi

# Check Python 3.11+
echo "Checking Python 3.11+..."
python3_version=$(python3 --version 2>&1 | cut -d' ' -f2)
if python3 -c "import sys; exit(0 if sys.version_info >= (3, 11) else 1)" 2>/dev/null; then
    echo "✓ Python 3.11+ found: $python3_version"
else
    echo "✗ Python 3.11+ required, found: $python3_version"
fi

# Check Git
echo "Checking Git..."
if command -v git >/dev/null 2>&1; then
    git_version=$(git --version)
    echo "✓ Git found: $git_version"
else
    echo "✗ Git not found"
fi

# Check UV
echo "Checking UV..."
if command -v uv >/dev/null 2>&1; then
    uv_version=$(uv --version)
    echo "✓ UV found: $uv_version"
else
    echo "✗ UV not found"
fi

# Check GitHub connectivity
echo "Checking GitHub connectivity..."
if ping -c 1 github.com >/dev/null 2>&1; then
    echo "✓ GitHub accessible"
else
    echo "✗ GitHub not accessible"
fi

# Test Spec Kit
echo "Testing GitHub Spec Kit..."
temp_dir="/tmp/spec_kit_test_$$"
mkdir -p "$temp_dir"
cd "$temp_dir"

if uvx --from git+https://github.com/github/spec-kit.git specify init validation_test >/dev/null 2>&1; then
    echo "✓ GitHub Spec Kit installation works"
    rm -rf "$temp_dir"
else
    echo "✗ GitHub Spec Kit installation failed"
    rm -rf "$temp_dir"
fi

echo ""
echo "=== Validation Complete ==="
```

Run the validation:
```bash
chmod +x validate_windows_setup.sh
./validate_windows_setup.sh
```

## 🎯 Next Steps

After successful setup:

1. **Run Environment Validation:**
   ```bash
   cd /home/ubuntu/github_spec_training
   ./validate_environment.sh
   ```

2. **Begin Training:**
   ```bash
   cd curriculum
   cat day1_foundation.md
   ```

3. **Configure Development Environment:**
   - Set up VS Code workspace in WSL
   - Configure GitHub Copilot settings
   - Create project directories

## 📚 Additional Resources

### Windows 11 + WSL2:
- [WSL2 Official Documentation](https://docs.microsoft.com/en-us/windows/wsl/)
- [Windows Terminal Setup](https://docs.microsoft.com/en-us/windows/terminal/)
- [VS Code WSL Extension](https://code.visualstudio.com/docs/remote/wsl)

### GitHub Spec Kit:
- [Official Repository](https://github.com/github/spec-kit)
- [Getting Started Guide](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/)

### Troubleshooting:
- [WSL2 Troubleshooting](https://docs.microsoft.com/en-us/windows/wsl/troubleshooting)
- [Python Installation Issues](https://docs.python.org/3/using/windows.html)

---

**Setup Complete!** Your Windows 11 environment is now ready for intensive GitHub Spec Kit training. The WSL2 environment provides excellent compatibility and performance for all training activities.

*Estimated total setup time: 30-60 minutes*  
*Next: Begin Day 1 Foundation Training*
