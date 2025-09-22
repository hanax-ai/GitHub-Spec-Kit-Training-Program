
# Artifact Edit Requirements Template

**Purpose:** This template must be used before editing any configuration file, script, or template to ensure proper documentation and rollback capability.

---

## Artifact Documentation Header

Copy and complete this header before making any file edits:

```markdown
## Artifact Edit Requirements

**Edit Date:** [YYYY-MM-DD HH:MM:SS]
**Editor:** [Your Name/Role]
**Change Request:** [Brief description of why this change is needed]

### Artifact Information
- **Owner:** [Who owns/maintains this file]
- **Path:** [Full file path]
- **Purpose:** [What this file does/controls]
- **Consumers:** [What systems/processes use this file]
- **Format:** [File format and syntax requirements]

### Change Details
- **Type:** [CREATE/UPDATE/DELETE]
- **Scope:** [What sections/lines are being changed]
- **Impact:** [What will be affected by this change]

### Acceptance Criteria
- [ ] [Specific test 1 that must pass]
- [ ] [Specific test 2 that must pass]
- [ ] [Specific test 3 that must pass]

### Rollback Procedures
- **Backup Location:** [Where backup is stored]
- **Rollback Command:** [Exact command to restore original]
- **Verification:** [How to verify rollback worked]

### Dependencies
- **Prerequisites:** [What must be in place before this change]
- **Related Files:** [Other files that may need updates]
- **Services to Restart:** [Services that need restart after change]
```

---

## Example Usage

### Example 1: SSH Configuration File

```markdown
## Artifact Edit Requirements

**Edit Date:** 2025-09-22 14:30:00
**Editor:** Agent0
**Change Request:** Configure SSH server for secure remote access

### Artifact Information
- **Owner:** agent0 (system administrator)
- **Path:** /etc/ssh/sshd_config
- **Purpose:** SSH server configuration and security settings
- **Consumers:** SSH daemon, remote connections, VS Code Remote-SSH
- **Format:** SSH configuration file format (key value pairs)

### Change Details
- **Type:** UPDATE
- **Scope:** Security settings (PermitRootLogin, PasswordAuthentication, etc.)
- **Impact:** SSH connection behavior and security posture

### Acceptance Criteria
- [ ] SSH service restarts without errors
- [ ] Remote SSH connection still works
- [ ] Security settings applied correctly
- [ ] No authentication lockout

### Rollback Procedures
- **Backup Location:** /etc/ssh/sshd_config.backup
- **Rollback Command:** `sudo cp /etc/ssh/sshd_config.backup /etc/ssh/sshd_config && sudo systemctl restart ssh`
- **Verification:** `sudo systemctl status ssh` shows active, SSH connection works

### Dependencies
- **Prerequisites:** SSH server installed and running
- **Related Files:** ~/.ssh/authorized_keys, ~/.ssh/config
- **Services to Restart:** ssh (sshd)
```

### Example 2: Hosts File Update

```markdown
## Artifact Edit Requirements

**Edit Date:** 2025-09-22 15:45:00
**Editor:** Agent0
**Change Request:** Add HX-Infrastructure domain entries for training environment

### Artifact Information
- **Owner:** agent0 (system administrator)
- **Path:** /etc/hosts (Ubuntu) / C:\Windows\System32\drivers\etc\hosts (Windows)
- **Purpose:** Local DNS resolution for HX-Infrastructure domains
- **Consumers:** System DNS resolver, applications, browsers, training tools
- **Format:** Standard hosts file format (IP hostname [aliases])

### Change Details
- **Type:** UPDATE (append entries)
- **Scope:** Add HX-Infrastructure section with training domains
- **Impact:** Local DNS resolution for dev-test.hana-x.ai and subdomains

### Acceptance Criteria
- [ ] nslookup dev-test.hana-x.ai resolves to correct IP
- [ ] ping dev-test.hana-x.ai works (if server responds)
- [ ] No conflicts with existing entries
- [ ] Proper formatting maintained

### Rollback Procedures
- **Backup Location:** /etc/hosts.backup (Ubuntu) / hosts.backup (Windows)
- **Rollback Command:** `sudo cp /etc/hosts.backup /etc/hosts` (Ubuntu) / `Copy-Item hosts.backup C:\Windows\System32\drivers\etc\hosts` (Windows)
- **Verification:** `nslookup dev-test.hana-x.ai` fails (returns to original state)

### Dependencies
- **Prerequisites:** Admin/sudo access to edit hosts file
- **Related Files:** DNS configuration files
- **Services to Restart:** systemd-resolved (Ubuntu) / DNS Client (Windows)
```

---

## Mandatory Usage Guidelines

### When to Use This Template

**ALWAYS use this template before:**
- Editing configuration files (/etc/ssh/sshd_config, /etc/hosts, etc.)
- Creating or modifying scripts
- Updating application configuration files
- Making changes to system service files
- Modifying environment files (.bashrc, .profile, etc.)

### Documentation Requirements

1. **Complete ALL sections** - No empty fields allowed
2. **Specific acceptance criteria** - Must be testable/verifiable
3. **Exact rollback commands** - Copy-paste ready
4. **Backup before edit** - Always create backup first
5. **Test after edit** - Run all acceptance criteria

### Integration with Verification Workflow

This template integrates with the Do → Verify → Log pattern:

1. **Before Do:** Complete this template
2. **During Do:** Follow the documented change plan
3. **During Verify:** Use the acceptance criteria
4. **During Log:** Reference this documentation in ENV_READINESS.md

### File Naming Convention

Save artifact documentation as:
- `[filename]_edit_[YYYYMMDD_HHMMSS].md`
- Example: `sshd_config_edit_20250922_143000.md`

### Storage Location

Store artifact documentation in:
- `~/training/documentation/artifact_edits/`
- Organize by date and component

---

## Quality Checklist

Before making any file edit, verify:

- [ ] Artifact header template completed
- [ ] Backup created and verified
- [ ] Acceptance criteria defined and testable
- [ ] Rollback procedure documented and tested
- [ ] Dependencies identified and addressed
- [ ] Change impact assessed
- [ ] Documentation stored in proper location

---

*This template ensures systematic, documented, and reversible file modifications with proper change management practices.*
