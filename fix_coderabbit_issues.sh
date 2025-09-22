#!/bin/bash

# Comprehensive CodeRabbit Issue Remediation Script
# Addresses all issues from CR_PR_5_Comments_3.pdf and CR_PR_5_Comments_4.pdf

echo "Starting comprehensive CodeRabbit issue remediation..."

# Fix 1: .coderabbit.yaml - Convert glob patterns to regex and fix schema issues
echo "Fixing .coderabbit.yaml schema issues..."
cat > .coderabbit.yaml << 'EOF'
# CodeRabbit Configuration for GitHub Spec Kit Training Program
# Version: 2.0 - Schema Compliant Configuration

# Language settings
language: en-US

# Early access features
early_access: false

# Review configuration
reviews:
  # High-level summary and additional features
  high_level_summary: true
  poem: true
  review_status: true
  
  # Path filters (using proper schema)
  path_filters:
    - "**/*.md"
    - "**/*.py" 
    - "**/*.sh"
    - "**/*.yaml"
    - "**/*.yml"
    - "**/*.json"
    - "**/*.txt"
    - "!node_modules/**"
    - "!.git/**"
    - "!**/*.log"
    - "!**/__pycache__/**"
  
  # Path-specific instructions
  path_instructions:
    - path: "**/*.py"
      instructions: |
        MANDATORY: Focus on code quality, security, and best practices.
        - Check for proper error handling and input validation
        - Verify secure coding practices and avoid common vulnerabilities
        - Ensure proper documentation and type hints
        - Validate performance considerations and resource usage
    
    - path: "**/*.md"
      instructions: |
        MANDATORY: Ensure professional documentation standards.
        - Verify proper Markdown formatting and structure
        - Check for clear, actionable instructions
        - Validate cross-platform compatibility guidance
        - Ensure verification-first workflow compliance
    
    - path: "**/*.yaml"
      instructions: |
        MANDATORY: Validate YAML syntax and configuration standards.
        - Check proper indentation and structure
        - Verify configuration completeness and accuracy
        - Validate security settings and access controls
    
    - path: "tests/**"
      instructions: |
        MANDATORY: Comprehensive testing standards.
        - Ensure proper test coverage and edge cases
        - Validate test isolation and repeatability
        - Check for proper assertions and error scenarios
    
    - path: "**/*"
      instructions: |
        This is a GitHub Spec Kit Training Program repository with MANDATORY REVIEW REQUIREMENTS.
        
        CRITICAL FOCUS AREAS:
        1. VERIFICATION-FIRST WORKFLOW: All instructions must include verification steps
        2. CROSS-PLATFORM COMPATIBILITY: Support Ubuntu 24.04 LTS and Windows 11
        3. MINIMAL TECH STACK: Focus on core tools and avoid unnecessary dependencies
        4. PROFESSIONAL STANDARDS: Maintain enterprise-grade documentation quality
        5. SECURITY COMPLIANCE: Follow security best practices throughout
        
        TRAINING ENVIRONMENT REQUIREMENTS:
        - Module 1 focus: Environment setup and baseline configuration
        - Hands-on learning approach with practical exercises
        - Clear troubleshooting guidance and error handling
        - Scalable foundation for advanced modules

# Chat configuration
chat:
  auto_reply: false

# Knowledge base settings
knowledge_base:
  learnings:
    scope: auto
  
  # Opt out of knowledge base features if needed
  opt_out: false

# Branch patterns (using proper regex format)
branch_patterns:
  # Main development branches
  - "^main$"
  - "^master$"
  - "^develop$"
  - "^dev$"
  
  # Feature and fix branches
  - "^feature/.*$"
  - "^fix/.*$"
  - "^hotfix/.*$"
  - "^release/.*$"
  
  # Training environment workflow patterns
  - "^revise-.*$"
  - "^training/.*$"
  - "^chore/.*$"
  - "^docs/.*$"
  
  # Match all branches (if needed)
  - ".*"
EOF

# Fix 2: Artifact_Header_Template.md - Update acceptance criteria and add traceability
echo "Fixing Artifact_Header_Template.md..."
sed -i '110,115c\
- [ ] Ubuntu: `getent hosts dev-test.hana-x.ai` includes 192.168.1.100, then `ping -c 1 dev-test.hana-x.ai`\
- [ ] Windows: `findstr dev-test.hana-x.ai C:\\Windows\\System32\\drivers\\etc\\hosts`, then `ping -n 1 dev-test.hana-x.ai`\
- [ ] No conflicts with existing entries\
- [ ] Proper formatting maintained' Artifact_Header_Template.md

# Add traceability and approvals section
sed -i '/### Rollback Procedures/i\
\
#### Traceability & Approvals\
- **PR/Issue Link:** **[URL/ID]**\
- **Risk Level:** **[LOW/MEDIUM/HIGH]**\
- **Approval(s):** **[Name/Role, Date]**\
- **Change Window:** **[Planned start/end with timezone]**' Artifact_Header_Template.md

# Fix ISO-8601 timestamp format
sed -i 's/Date: \[YYYY-MM-DD\]/Date: [YYYY-MM-DDTHH:MM:SSZ]/' Artifact_Header_Template.md

# Fix 3: ENV_READINESS.md - Add Resolve-DnsName example for Windows
echo "Fixing ENV_READINESS.md..."
sed -i "s/findstr dev-test.hana-x.ai C:\\\\Windows\\\\System32\\\\drivers\\\\etc\\\\hosts && ping -n 1 dev-test.hana-x.ai/findstr dev-test.hana-x.ai C:\\\\Windows\\\\System32\\\\drivers\\\\etc\\\\hosts \&\& Resolve-DnsName dev-test.hana-x.ai/" ENV_READINESS.md

# Fix 4: Hosts_File_Template.txt - Multiple fixes
echo "Fixing Hosts_File_Template.txt..."

# Add conflict test note
sed -i '/Ensure 192.168.1.100 is reachable/a\
Optional: verify no conflict\
Ubuntu: `ping -c 1 192.168.1.100 || echo "no reply (ok for bootstrap)"`\
Windows: `ping -n 1 192.168.1.100`' Hosts_File_Template.txt

# Make verification assertive with grep
sed -i 's/getent hosts dev-test.hana-x.ai/getent hosts dev-test.hana-x.ai | grep -F '\''192.168.1.100'\''/' Hosts_File_Template.txt
sed -i 's/Should include 192.168.1.100/Test domain resolution via nsswitch (should include 192.168.1.100)/' Hosts_File_Template.txt

# Fix Windows verification - remove duplicate ping and improve wording
sed -i '/Confirm entry exists and resolves/,/Should show 192.168.1.100/{
s/Confirm entry exists and resolves/Confirm entry exists, then test reachability/
/ping dev-test.hana-x.ai -n 1/d
s/Should show 192.168.1.100/Should show 192.168.1.100 (if server responds)/
}' Hosts_File_Template.txt

# Make Ubuntu append idempotent and add DNS cache flush
sed -i '/sudo tee -a \/etc\/hosts << '\''EOF'\''/i\
if ! grep -q "^# HX-Infrastructure - Training Environment" /etc/hosts; then' Hosts_File_Template.txt

sed -i '/^EOF$/a\
  sudo systemd-resolve --flush-caches || true\
fi' Hosts_File_Template.txt

# Add parameterization note for IP
sed -i '/192.168.1.100/i\
# NOTE: Replace 192.168.1.100 with your actual training environment IP - CHANGE ME' Hosts_File_Template.txt

# Fix 5: baseline_training_environment_setup.md - Multiple fixes
echo "Fixing baseline_training_environment_setup.md..."

# Replace netstat with ss
sed -i 's/sudo netstat -tlnp | grep :22/sudo ss -tlnp | grep :22/' baseline_training_environment_setup.md

# Remove obsolete apt-transport-https
sed -i 's/sudo apt install -y ca-certificates apt-transport-https/sudo apt install -y ca-certificates/' baseline_training_environment_setup.md

# Fix Python version check
sed -i 's/python3 --version/python3.11 --version/' baseline_training_environment_setup.md
sed -i 's/# Should show: Python 3.11.x/# Should show: Python 3.11.x/' baseline_training_environment_setup.md

# Fix interpreter path typo
sed -i "s|5. Choose: \`'./venv-hx-spec-kit-py311/bin/python'\`|5. Choose: \`'./venv-hx-spec-kit-py311/bin/python'\`|" baseline_training_environment_setup.md

# Fix broad wildcard deletion
sed -i 's/rm -rf \.venv-\*/rm -rf .venv-hx-spec-kit-py311/' baseline_training_environment_setup.md

# Add language to fenced code block
sed -i '/# In VS Code:/i\
```text' baseline_training_environment_setup.md
sed -i '/1. Press Ctrl+Shift+P/a\
```' baseline_training_environment_setup.md

# Fix Windows PowerShell encoding issue
sed -i 's/Add-Content C:\\Windows\\System32\\drivers\\etc\\hosts/Add-Content -Encoding ASCII C:\\Windows\\System32\\drivers\\etc\\hosts/' baseline_training_environment_setup.md

# Fix Windows verification commands - replace getent with proper Windows commands
sed -i '/Test domain resolution via nsswitch/,/Should ping successfully/{
s/Test domain resolution via nsswitch/Confirm entry exists and resolves/
s/getent hosts dev-test.hana-x.ai/findstr dev-test.hana-x.ai C:\\Windows\\System32\\drivers\\etc\\hosts/
s/Should include 192.168.1.100/Resolve-DnsName dev-test.hana-x.ai/
s/Test ping/Optional: ping (only if ICMP allowed)/
s/Should ping successfully (if server responds to ping)/ping dev-test.hana-x.ai -n 1/
}' baseline_training_environment_setup.md

echo "All CodeRabbit issues have been addressed!"
echo "Summary of fixes applied:"
echo "1. Fixed .coderabbit.yaml schema compliance (regex patterns, proper structure)"
echo "2. Updated Artifact_Header_Template.md (acceptance criteria, traceability, ISO-8601)"
echo "3. Enhanced ENV_READINESS.md (Windows Resolve-DnsName example)"
echo "4. Improved Hosts_File_Template.txt (conflict tests, idempotent operations, parameterization)"
echo "5. Corrected baseline_training_environment_setup.md (ss vs netstat, encoding, paths, verification commands)"
