#!/bin/bash
# Test Environment Setup Script for GitHub Spec Kit Training Program
# Version: 1.0
# Date: 2025-09-22

set -e  # Exit on any error

echo "=== GitHub Spec Kit Training Program - Test Environment Setup ==="
echo "Starting setup at: $(date '+%Y-%m-%d %H:%M:%S')"
echo ""

# Step 1: System Update and CA Certificates
echo "Step 1: System Update and CA Certificates"
sudo apt update && sudo apt upgrade -y
sudo apt install -y ca-certificates apt-transport-https
echo "✅ System updated and CA certificates installed"
echo ""

# Step 2: Git Installation and Configuration
echo "Step 2: Git Installation and Configuration"
sudo apt install -y git
git config --global user.name "Agent0"
git config --global user.email "agent0@hana-x.ai"
git config --global init.defaultBranch main
git config --global core.editor vim
echo "✅ Git installed and configured"
echo ""

# Step 3: Python 3.12 Environment Setup
echo "Step 3: Python 3.12 Environment Setup"
sudo apt install -y python3 python3-venv python3-dev python3-pip
echo "✅ Python 3.12 environment installed"
echo ""

# Step 4: OpenSSH Server Configuration
echo "Step 4: OpenSSH Server Configuration"
sudo apt install -y openssh-server
mkdir -p ~/.ssh
chmod 700 ~/.ssh
echo "✅ SSH server installed and configured"
echo ""

# Step 5: Development Tools
echo "Step 5: Development Tools"
sudo apt install -y build-essential curl wget vim tree unzip
echo "✅ Development tools installed"
echo ""

# Step 6: Hosts File Configuration
echo "Step 6: Hosts File Configuration"
sudo cp /etc/hosts /etc/hosts.backup
sudo tee -a /etc/hosts > /dev/null << 'HOSTS_EOF'

# HX-Infrastructure - Training Environment
# Version: 1.0 - Bootstrap/Fallback Configuration
# Management: Manual (will migrate to Ansible in future iterations)
# Purpose: Local DNS resolution for training environment
192.168.1.100    dev-test.hana-x.ai
192.168.1.100    api.dev-test.hana-x.ai
192.168.1.100    app.dev-test.hana-x.ai
# End HX-Infrastructure
HOSTS_EOF
echo "✅ Hosts file configured"
echo ""

# Step 7: Virtual Environment Setup
echo "Step 7: Virtual Environment Setup"
mkdir -p ~/training/hx-spec-kit
cd ~/training/hx-spec-kit
python3 -m venv .venv-hx-spec-kit-py312
source .venv-hx-spec-kit-py312/bin/activate
pip install --upgrade pip
pip install pytest requests
echo "✅ Virtual environment created and configured"
echo ""

echo "=== Setup completed successfully at: $(date '+%Y-%m-%d %H:%M:%S') ==="
echo "Virtual environment location: ~/training/hx-spec-kit/.venv-hx-spec-kit-py312"
echo "To activate: source ~/training/hx-spec-kit/.venv-hx-spec-kit-py312/bin/activate"
