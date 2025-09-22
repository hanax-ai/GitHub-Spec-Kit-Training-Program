
# Baseline Training Environment Setup Guide
## Verification-First Minimal Approach

**Version:** 2.0  
**Date:** September 22, 2025  
**Target Environment:** Windows PC (HANA-X-JR0) → Ubuntu 24.04 Server (HX dev server)  
**Approach:** Verification-first workflow with minimal tech stack for Module 1

---

## Table of Contents

1. [Overview](#overview)
2. [Verification-First Workflow](#verification-first-workflow)
3. [Minimal Tech Stack](#minimal-tech-stack)
4. [Prerequisites](#prerequisites)
5. [Ubuntu 24.04 Server Setup](#ubuntu-2404-server-setup)
6. [Windows PC Setup](#windows-pc-setup)
7. [SSH Connection Configuration](#ssh-connection-configuration)
8. [VS Code Remote-SSH Setup](#vs-code-remote-ssh-setup)
9. [Hosts File Configuration](#hosts-file-configuration)
10. [Virtual Environment Setup](#virtual-environment-setup)
11. [Final Verification](#final-verification)
12. [Troubleshooting](#troubleshooting)
13. [Supporting Templates](#supporting-templates)

---

## Overview

This guide establishes a baseline training environment using a **verification-first approach** with minimal tech stack for Module 1 training activities.

### Key Principles
- **Do → Verify → Log**: Every step includes verification and logging to ENV_READINESS.md
- **Minimal Scope**: Only tools required for Module 1 (defer optional components)
- **Artifact Management**: Structured approach to file edits with documentation
- **Communicative Naming**: Specific virtual environment names (.venv-hx-spec-kit-py311)

### Success Criteria
- All verification steps pass and logged in ENV_READINESS.md
- Working VS Code Remote-SSH connection with Python 3.11 environment
- Standardized hosts file configuration
- Foundation ready for Module 1 training activities

---

## Verification-First Workflow

### Do → Verify → Log Pattern

Every installation and configuration step follows this pattern:

1. **Do**: Execute the command or make the change
2. **Verify**: Run verification command to prove it worked
3. **Log**: Record result in ENV_READINESS.md with timestamp and status

### ENV_READINESS.md Logging

All verification results must be logged using the provided template. Example:

```markdown
| Component | Status | Timestamp | Verification Command | Result |
|-----------|--------|-----------|---------------------|---------|
| Git | ✅ PASS | 2025-09-22 10:30:15 | `git --version` | git version 2.34.1 |
```

### Stop and Fix Approach

- **CRITICAL**: Do not proceed if any verification step fails
- Fix the issue before continuing to next step
- Re-run verification after fix
- Update log with final status

---

## Minimal Tech Stack

### Module 1 Requirements Only

**Core Components (Required):**
- Ubuntu 24.04 LTS - Base OS (already provisioned)
- OpenSSH + Remote-SSH - Remote development and file operations
- CA Certificates - TLS trust for git/curl operations
- Git - Clone/pull training repositories
- Python 3.11 + venv + pip - Run training scripts and tests
- VS Code - IDE with Remote-SSH extension

**Deferred Components (Optional):**
- Node LTS - Defer unless specifically needed for Module 1
- Docker Engine - Defer unless specifically needed for Module 1
- Additional databases - Defer unless specifically needed

### Expansion Criteria

Optional components will be added only when:
- Explicitly required by Module 1 training materials
- Blocking progress on core training activities
- Requested by training supervisor

---

## Prerequisites

### System Requirements
- **Windows PC:** Windows 10/11 with admin privileges
- **Ubuntu Server:** Ubuntu 24.04 LTS with sudo access
- **Network:** SSH connectivity between systems (port 22)
- **Account:** Domain admin account `agent0` on both systems

### Before You Begin

**Do:**
```bash
# Check network connectivity
ping <ubuntu-server-ip>
```

**Verify:**
```bash
# Should show successful ping responses
# Example: 64 bytes from <ip>: icmp_seq=1 ttl=64 time=1.23 ms
```

**Log:** Record connectivity test result in ENV_READINESS.md

---

## Ubuntu 24.04 Server Setup

### Step 1: System Update and CA Certificates

**Do:**
```bash
# Update system packages
sudo apt update && sudo apt upgrade -y

# Install CA certificates for TLS trust
sudo apt install -y ca-certificates apt-transport-https
```

**Verify:**
```bash
# Check CA certificates installation
ls -la /etc/ssl/certs/ | wc -l
# Should show 100+ certificate files

# Test TLS connectivity
curl -I https://github.com
# Should return HTTP/2 200 without SSL errors
```

**Log:** Record system update and CA certificates status in ENV_READINESS.md

### Step 2: Git Installation and Configuration

**Do:**
```bash
# Install Git
sudo apt install -y git

# Configure Git globally
git config --global user.name "Agent0"
git config --global user.email "agent0@hana-x.ai"
git config --global init.defaultBranch main
git config --global core.editor vim
```

**Verify:**
```bash
# Check Git version and configuration
git --version
git config --list | grep -E "(user.name|user.email|init.defaultBranch)"
```

**Log:** Record Git installation and configuration in ENV_READINESS.md

### Step 3: Python 3.11 Environment Setup

**Do:**
```bash
# Install Python 3.11 and development tools
sudo apt install -y python3.11 python3.11-venv python3.11-dev python3-pip

# Use Python 3.11 explicitly for virtual environments (do not change system python3)
# Example: python3.11 -m venv .venv-hx-spec-kit-py311
```

**Verify:**
```bash
# Check Python version
python3 --version
# Should show: Python 3.11.x

# Check pip installation
python3 -m pip --version
# Should show pip version

# Test virtual environment creation
python3.11 -m venv /tmp/test-venv
source /tmp/test-venv/bin/activate
python --version
deactivate
rm -rf /tmp/test-venv
```

**Log:** Record Python 3.11 installation and venv capability in ENV_READINESS.md

### Step 4: OpenSSH Server Configuration

**Do:**
```bash
# Install and configure OpenSSH server
sudo apt install -y openssh-server

# Start and enable SSH service
sudo systemctl start ssh
sudo systemctl enable ssh

# Create .ssh directory with proper permissions
mkdir -p ~/.ssh
chmod 700 ~/.ssh
```

**Verify:**
```bash
# Check SSH service status
sudo systemctl status ssh | grep "Active:"
# Should show: Active: active (running)

# Check SSH port listening
sudo netstat -tlnp | grep :22
# Should show SSH listening on port 22

# Verify .ssh directory permissions
ls -ld ~/.ssh
# Should show: drwx------ ... .ssh
```

**Log:** Record SSH server installation and configuration in ENV_READINESS.md

### Step 5: Basic Development Tools

**Do:**
```bash
# Install essential development packages
sudo apt install -y \
    build-essential \
    curl \
    wget \
    vim \
    tree \
    unzip
```

**Verify:**
```bash
# Check essential tools
gcc --version | head -1
curl --version | head -1
wget --version | head -1
vim --version | head -1
tree --version
```

**Log:** Record development tools installation in ENV_READINESS.md

---

## Windows PC Setup

### Step 1: VS Code Installation

**Do:**
1. Download VS Code from <https://code.visualstudio.com/>
2. Run installer with default settings
3. Launch VS Code

**Verify:**
```powershell
# Check VS Code installation
code --version
# Should show version, commit, and architecture
```

**Log:** Record VS Code installation in ENV_READINESS.md

### Step 2: Git for Windows Installation

**Do:**
1. Download Git from <https://git-scm.com/download/win>
2. Run installer with default settings
3. Open Git Bash or PowerShell

**Verify:**
```powershell
# Check Git installation
git --version
# Should show: git version 2.x.x.windows.x

# Check SSH client
ssh -V
# Should show OpenSSH version
```

**Log:** Record Git for Windows installation in ENV_READINESS.md

### Step 3: VS Code Remote-SSH Extension

**Do:**
1. Open VS Code
2. Go to Extensions (Ctrl+Shift+X)
3. Search and install "Remote - SSH" (ms-vscode-remote.remote-ssh)
4. Install "Remote - SSH: Editing Configuration Files" (ms-vscode-remote.remote-ssh-edit)

**Verify:**
```
# In VS Code:
1. Press Ctrl+Shift+P
2. Type "Remote-SSH"
3. Should see Remote-SSH commands available
```

**Log:** Record Remote-SSH extension installation in ENV_READINESS.md

---

## SSH Connection Configuration

### Step 1: SSH Key Generation (Windows)

**Do:**
```powershell
# Generate SSH key pair
ssh-keygen -t ed25519 -C "agent0@hana-x.ai" -f ~/.ssh/id_ed25519_hx_dev

# Start the Windows OpenSSH Agent service and add key
Start-Service ssh-agent
Set-Service -Name ssh-agent -StartupType Automatic
ssh-add $env:USERPROFILE\.ssh\id_ed25519_hx_dev
```

**Verify:**
```powershell
# Check key files exist
ls ~/.ssh/id_ed25519_hx_dev*
# Should show private and public key files

# Check key added to agent
ssh-add -l
# Should show the key fingerprint
```

**Log:** Record SSH key generation in ENV_READINESS.md

### Step 2: SSH Key Deployment (Ubuntu)

**Do:**
```bash
# On Ubuntu server, add public key to authorized_keys
# (Copy public key content from Windows ~/.ssh/id_ed25519_hx_dev.pub)
echo "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAA... agent0@hana-x.ai" >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
```

**Verify:**
```bash
# Check authorized_keys file
ls -la ~/.ssh/authorized_keys
# Should show: -rw------- ... authorized_keys

# Test SSH connection from Windows
# ssh -i ~/.ssh/id_ed25519_hx_dev agent0@<ubuntu-server-ip>
```

**Log:** Record SSH key deployment and connection test in ENV_READINESS.md

### Step 3: SSH Config File (Windows)

**Do:**
```powershell
# Create SSH config file
New-Item -Path ~/.ssh/config -ItemType File -Force
Add-Content ~/.ssh/config @"
Host hx-dev-server
    HostName <ubuntu-server-ip>
    User agent0
    IdentityFile ~/.ssh/id_ed25519_hx_dev
    ServerAliveInterval 60
    ServerAliveCountMax 3
"@
```

**Verify:**
```powershell
# Test SSH connection using config
ssh hx-dev-server "echo 'SSH connection successful'"
# Should show: SSH connection successful
```

**Log:** Record SSH config creation and connection test in ENV_READINESS.md

---

## VS Code Remote-SSH Setup

### Step 1: Remote-SSH Connection Configuration

**Do:**
1. Open VS Code
2. Press Ctrl+Shift+P
3. Type "Remote-SSH: Connect to Host"
4. Select "Configure SSH Hosts"
5. Choose user SSH config file
6. Add or verify hx-dev-server configuration

**Verify:**
1. Press Ctrl+Shift+P
2. Type "Remote-SSH: Connect to Host"
3. Select "hx-dev-server"
4. Should connect successfully and show Ubuntu environment

**Log:** Record VS Code Remote-SSH connection in ENV_READINESS.md

### Step 2: Remote Extensions Installation

**Do:**
1. Connect to hx-dev-server via Remote-SSH
2. Install Python extension on remote server
3. Install Git extension on remote server

**Verify:**
1. Open terminal in VS Code (connected to remote)
2. Run: `python3 --version`
3. Run: `git --version`
4. Both should work without errors

**Log:** Record remote extensions installation in ENV_READINESS.md

---

## Hosts File Configuration

### Step 1: Ubuntu Hosts File Update

**Artifact Edit Requirements:**
- **Owner:** agent0
- **Path:** /etc/hosts
- **Purpose:** HX-Infrastructure domain resolution
- **Consumers:** System DNS resolution, training applications
- **Format:** Standard hosts file format
- **Acceptance Criteria:** dev-test.hana-x.ai resolves correctly
- **Rollback:** Backup exists at /etc/hosts.backup

**Do:**
```bash
# Backup current hosts file
sudo cp /etc/hosts /etc/hosts.backup

# Add HX-Infrastructure entries
sudo tee -a /etc/hosts << 'EOF'

# HX-Infrastructure - Training Environment
# Version: 1.0 - Bootstrap/Fallback Configuration
# Management: Manual (will migrate to Ansible in future iterations)
# Purpose: Local DNS resolution for training environment
192.168.1.100    dev-test.hana-x.ai
192.168.1.100    api.dev-test.hana-x.ai
192.168.1.100    app.dev-test.hana-x.ai
# End HX-Infrastructure
EOF
```

**Verify:**
```bash
# Test domain resolution via nsswitch
getent hosts dev-test.hana-x.ai
# Should include 192.168.1.100

# Test ping
ping -c 1 dev-test.hana-x.ai
# Should ping successfully (if server responds to ping)

# Verify hosts file format
grep -A 10 "HX-Infrastructure" /etc/hosts
```

**Log:** Record hosts file configuration in ENV_READINESS.md

### Step 2: Windows Hosts File Update

**Artifact Edit Requirements:**
- **Owner:** agent0
- **Path:** C:\Windows\System32\drivers\etc\hosts
- **Purpose:** HX-Infrastructure domain resolution
- **Consumers:** System DNS resolution, VS Code, browsers
- **Format:** Standard Windows hosts file format
- **Acceptance Criteria:** dev-test.hana-x.ai resolves correctly
- **Rollback:** Backup exists at hosts.backup

**Do:**
```powershell
# Run PowerShell as Administrator
# Backup current hosts file
Copy-Item C:\Windows\System32\drivers\etc\hosts C:\Windows\System32\drivers\etc\hosts.backup

# Add HX-Infrastructure entries
Add-Content C:\Windows\System32\drivers\etc\hosts @"

# HX-Infrastructure - Training Environment
# Version: 1.0 - Bootstrap/Fallback Configuration
# Management: Manual (will migrate to Ansible in future iterations)
# Purpose: Local DNS resolution for training environment
192.168.1.100    dev-test.hana-x.ai
192.168.1.100    api.dev-test.hana-x.ai
192.168.1.100    app.dev-test.hana-x.ai
# End HX-Infrastructure
"@
```

**Verify:**
```powershell
# Test domain resolution via nsswitch
getent hosts dev-test.hana-x.ai
# Should include 192.168.1.100

# Test ping
ping dev-test.hana-x.ai -n 1
# Should ping successfully (if server responds to ping)
```

**Log:** Record Windows hosts file configuration in ENV_READINESS.md

---

## Virtual Environment Setup

### Step 1: Communicative Virtual Environment Naming

**Naming Convention:**
- Format: `.venv-{project}-{purpose}-{runtime}`
- Example: `.venv-hx-spec-kit-py311`
- Components:
  - `hx`: Project prefix (HANA-X)
  - `spec-kit`: Repository/module name
  - `py311`: Runtime version (Python 3.11)

### Step 2: Create Training Virtual Environment

**Do:**
```bash
# Navigate to training workspace
mkdir -p ~/training/hx-spec-kit
cd ~/training/hx-spec-kit

# Create virtual environment with communicative name
python3.11 -m venv .venv-hx-spec-kit-py311

# Activate virtual environment
source .venv-hx-spec-kit-py311/bin/activate

# Upgrade pip and install basic packages
pip install --upgrade pip
pip install pytest requests
```

**Verify:**
```bash
# Check virtual environment activation
which python
# Should show: /home/agent0/training/hx-spec-kit/.venv-hx-spec-kit-py311/bin/python

# Check Python version in venv
python --version
# Should show: Python 3.11.x

# Check installed packages
pip list
# Should show pip, pytest, requests
```

**Log:** Record virtual environment creation in ENV_READINESS.md

### Step 3: VS Code Python Interpreter Configuration

**Do:**
1. Open VS Code connected to hx-dev-server
2. Open ~/training/hx-spec-kit folder
3. Press Ctrl+Shift+P
4. Type "Python: Select Interpreter"
5. Choose: `./venv-hx-spec-kit-py311/bin/python`

**Verify:**
1. Check status bar shows correct Python interpreter
2. Open terminal in VS Code
3. Should automatically activate virtual environment
4. Run: `which python` - should show venv path

**Log:** Record VS Code Python interpreter configuration in ENV_READINESS.md

---

## Final Verification

### Step 1: Complete Environment Test

**Do:**
```bash
# Create test script
cat > ~/training/hx-spec-kit/test_environment.py << 'EOF'
#!/usr/bin/env python3
"""
Environment verification test script
Tests all core components of the training environment
"""

import sys
import subprocess
import socket

def test_python_version():
    """Test Python 3.11 is available"""
    version = sys.version_info
    assert version.major == 3 and version.minor == 11, f"Expected Python 3.11, got {version.major}.{version.minor}"
    print(f"✅ Python version: {version.major}.{version.minor}.{version.micro}")

def test_git_available():
    """Test Git is available"""
    result = subprocess.run(['git', '--version'], capture_output=True, text=True)
    assert result.returncode == 0, "Git not available"
    print(f"✅ Git available: {result.stdout.strip()}")

def test_domain_resolution():
    """Test HX-Infrastructure domain resolution"""
    try:
        socket.gethostbyname('dev-test.hana-x.ai')
        print("✅ Domain resolution: dev-test.hana-x.ai resolves correctly")
    except socket.gaierror:
        print("❌ Domain resolution: dev-test.hana-x.ai failed to resolve")
        raise

def test_virtual_environment():
    """Test virtual environment is active"""
    venv_path = sys.prefix
    assert '.venv-hx-spec-kit-py311' in venv_path, f"Virtual environment not active: {venv_path}"
    print(f"✅ Virtual environment active: {venv_path}")

if __name__ == "__main__":
    print("🔍 Running environment verification tests...")
    test_python_version()
    test_git_available()
    test_domain_resolution()
    test_virtual_environment()
    print("🎉 All environment tests passed!")
EOF

# Make script executable
chmod +x ~/training/hx-spec-kit/test_environment.py
```

**Verify:**
```bash
# Run environment test script
cd ~/training/hx-spec-kit
source .venv-hx-spec-kit-py311/bin/activate
python test_environment.py
# Should show all tests passing
```

**Log:** Record final environment verification in ENV_READINESS.md

### Step 2: VS Code Integration Test

**Do:**
1. Open VS Code connected to hx-dev-server
2. Open ~/training/hx-spec-kit/test_environment.py
3. Run script using VS Code Python extension (F5 or Run button)

**Verify:**
1. Script should run successfully in VS Code terminal
2. All tests should pass
3. Python interpreter should show correct venv path

**Log:** Record VS Code integration test in ENV_READINESS.md

---

## Troubleshooting

### Common Issues and Solutions

#### SSH Connection Issues
**Problem:** SSH connection refused or timeout
**Solution:**
1. Verify SSH service running: `sudo systemctl status ssh`
2. Check firewall: `sudo ufw status`
3. Test network connectivity: `ping <server-ip>`

#### Python Virtual Environment Issues
**Problem:** Virtual environment not activating
**Solution:**
1. Check Python 3.11 installation: `python3.11 --version`
2. Recreate virtual environment: `rm -rf .venv-* && python3.11 -m venv .venv-hx-spec-kit-py311`
3. Check permissions: `ls -la .venv-*`

#### Domain Resolution Issues
**Problem:** dev-test.hana-x.ai not resolving
**Solution:**
1. Check hosts file entries: `grep hana-x /etc/hosts`
2. Clear DNS cache: `sudo systemctl restart systemd-resolved`
3. Test with IP directly: `ping 192.168.1.100`

#### VS Code Remote-SSH Issues
**Problem:** Cannot connect to remote server
**Solution:**
1. Check SSH config: `cat ~/.ssh/config`
2. Test SSH connection: `ssh hx-dev-server`
3. Restart VS Code and try again

---

## Supporting Templates

### ENV_READINESS.md Template
See: [ENV_READINESS.md](ENV_READINESS.md) for verification logging template

### Artifact Header Template
See: [Artifact Header Template](../templates/Artifact_Header_Template.md) for file edit documentation requirements

### Hosts File Template
See: [Hosts File Template](../templates/Hosts_File_Template.txt) for standardized HX-Infrastructure entries

---

## Baseline Checklist

### Pre-Setup Verification
- [ ] Network connectivity between Windows and Ubuntu
- [ ] Admin/sudo access on both systems
- [ ] Internet connectivity on both systems

### Ubuntu Server Setup
- [ ] System updated and CA certificates installed
- [ ] Git installed and configured
- [ ] Python 3.11 installed with venv capability
- [ ] OpenSSH server running and configured
- [ ] Development tools installed
- [ ] All steps verified and logged

### Windows PC Setup
- [ ] VS Code installed and verified
- [ ] Git for Windows installed and verified
- [ ] Remote-SSH extension installed and verified
- [ ] All steps verified and logged

### SSH Configuration
- [ ] SSH keys generated and deployed
- [ ] SSH config file created
- [ ] SSH connection tested and working
- [ ] All steps verified and logged

### VS Code Remote Setup
- [ ] Remote-SSH connection established
- [ ] Remote extensions installed
- [ ] Python interpreter configured
- [ ] All steps verified and logged

### Hosts File Configuration
- [ ] Ubuntu hosts file updated with HX-Infrastructure entries
- [ ] Windows hosts file updated with HX-Infrastructure entries
- [ ] Domain resolution tested and working
- [ ] All steps verified and logged

### Virtual Environment Setup
- [ ] Communicative virtual environment created (.venv-hx-spec-kit-py311)
- [ ] Virtual environment activated and tested
- [ ] VS Code Python interpreter configured
- [ ] All steps verified and logged

### Final Verification
- [ ] Environment test script created and executed
- [ ] All tests passing
- [ ] VS Code integration tested
- [ ] ENV_READINESS.md completed with all verification results

### Success Criteria Met
- [ ] All verification steps passed and logged
- [ ] Working VS Code Remote-SSH connection
- [ ] Python 3.11 virtual environment functional
- [ ] HX-Infrastructure domain resolution working
- [ ] Foundation ready for Module 1 training activities

---

### End of Guide

*This guide implements a verification-first approach with minimal tech stack focused on Module 1 requirements. All optional components are deferred until specifically needed.*
