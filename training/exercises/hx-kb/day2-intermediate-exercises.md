
# Day 2: Intermediate Exercises - HX-Infrastructure Knowledge Base

## Overview
These exercises focus on content integration, sprint documentation, and operational runbook creation using advanced GitHub Spec Kit techniques.

## Exercise 1: Sprint Documentation Integration (120 minutes)

### Objective
Create comprehensive documentation for all four HX-Infrastructure project sprints, integrating lessons learned and best practices.

### Tasks

#### 1.1 Sprint 1 Documentation (30 minutes)
**Focus:** Repository restructuring, foundational CI/CD, architecture documentation

```bash
cd /home/ubuntu/github_spec_training/HX-Infrastructure-Knowledge-Base

# Create Sprint 1 specification
uvx --from git+https://github.com/github/spec-kit.git specify init sprint1_documentation --ai copilot
```bash

Using the `/specify` command, create specifications for Sprint 1 documentation including:
- **Objective:** Transform basic infrastructure into structured, automated system
- **Key Achievements:** Repository organization, CI/CD pipeline setup, architecture docs
- **Technical Implementation:** Ansible restructuring, GitHub Actions setup, documentation standards
- **Lessons Learned:** Over-scoping challenges, importance of early structure, automation benefits
- **Metrics:** Deployment time reduction, error rate improvements, documentation coverage

Create `docs/history/sprints/sprint-1-summary.md` with:
```markdown
# Sprint 1: Repository Restructuring & CI/CD Foundation

## Overview
- **Duration:** [Sprint timeframe]
- **Objective:** Transform basic infrastructure into structured, automated system
- **Success Criteria:** Organized repository, functional CI/CD, comprehensive documentation

## Key Achievements
- ✅ Repository restructured with clear organization
- ✅ Initial CI/CD pipeline implemented
- ✅ Architecture documentation established
- ✅ Ansible roles organized and standardized

## Technical Implementation
### Repository Restructuring
- Organized Ansible roles into logical categories
- Established consistent naming conventions
- Created clear directory structure
- Implemented documentation standards

### CI/CD Pipeline Setup
- GitHub Actions workflows for validation
- Automated testing with Molecule
- Security scanning integration
- Deployment automation framework

### Architecture Documentation
- System overview and component diagrams
- Technology stack decisions
- Integration patterns and standards
- Security architecture baseline

## Lessons Learned
### What Worked Well
- **Early Structure Investment:** Time spent on organization paid dividends
- **Automation First:** CI/CD setup prevented many issues downstream
- **Documentation Discipline:** Consistent documentation improved team velocity

### Challenges and Solutions
- **Over-Scoping:** Initial scope too broad, refined to focus on essentials
- **Branch Management:** Multiple branches created confusion, adopted trunk-based development
- **Complexity Management:** Broke down complex tasks into smaller, manageable pieces

## Metrics and Impact

| Metric | Before Sprint 1 | After Sprint 1 | Improvement |
|--------|----------------|----------------|-------------|
| Deployment Time | 45 minutes | 15 minutes | 67% reduction |
| Error Rate | 15% | 5% | 67% reduction |
| Documentation Coverage | 20% | 85% | 325% increase |
| Team Velocity | Baseline | +40% | 40% increase |

## Technical Artifacts
- [Repository Structure](../../architecture/repository-structure.md)
- [CI/CD Pipeline Configuration](../../examples/cicd/github-actions-basic.yml)
- [Ansible Role Standards](../../templates/ansible/role-template/)
- [Documentation Templates](../../templates/documentation/)

## Next Sprint Preparation
- Enhanced testing frameworks
- Monitoring and alerting integration
- Performance optimization planning
- Security hardening roadmap
```bash

**Deliverable:** Complete Sprint 1 documentation with metrics and lessons learned

#### 1.2 Sprint 2 Documentation (30 minutes)
**Focus:** Testing frameworks, enhanced pipelines, monitoring integration

Create `docs/history/sprints/sprint-2-summary.md` focusing on:
- Testing framework implementation (Molecule, integration tests)
- Enhanced CI/CD pipelines with comprehensive validation
- Monitoring and alerting system integration
- Performance baseline establishment

**Key lessons to document:**
- Testing framework benefits and challenges
- Monitoring strategy effectiveness
- Pipeline optimization techniques
- Quality gate implementation

#### 1.3 Sprint 3 Documentation (30 minutes)
**Focus:** Blue-green deployments, backups, performance optimization

Create `docs/history/sprints/sprint-3-summary.md` covering:
- Blue-green deployment strategy implementation
- Backup and recovery procedures
- Performance optimization achievements
- Scalability improvements

**Key lessons to document:**
- Deployment strategy benefits and trade-offs
- Backup validation importance
- Performance tuning techniques
- Scalability planning approaches

#### 1.4 Sprint 4 Documentation (30 minutes)
**Focus:** AI-driven orchestration, self-healing, multi-cloud strategies

Create `docs/history/sprints/sprint-4-summary.md` detailing:
- AI integration for automated operations
- Self-healing system implementation
- Multi-cloud strategy execution
- Advanced automation capabilities

**Key lessons to document:**
- AI integration challenges and solutions
- Self-healing system effectiveness
- Multi-cloud complexity management
- Advanced automation benefits

## Exercise 2: Architecture Documentation Creation (90 minutes)

### Objective
Create comprehensive architecture documentation that captures the system design, decisions, and evolution.

### Tasks

#### 2.1 System Architecture Overview (45 minutes)

```bash
# Create architecture specification
uvx --from git+https://github.com/github/spec-kit.git specify init architecture_documentation --ai copilot
```bash

Create `docs/architecture/overview.md` with:

```markdown
# HX-Infrastructure System Architecture

## System Overview
The HX-Infrastructure system is a multi-cloud, AI-enhanced infrastructure platform designed for enterprise-scale operations with automated management and self-healing capabilities.

## Architecture Principles
- **Cloud Agnostic:** Multi-cloud support (AWS, Azure, GCP)
- **Automation First:** AI-driven operations and self-healing
- **Security by Design:** Integrated security controls and compliance
- **Scalability:** Horizontal and vertical scaling capabilities
- **Observability:** Comprehensive monitoring and alerting

## High-Level Architecture

```mermaid
graph TB
    subgraph "Multi-Cloud Infrastructure"
        AWS[AWS Resources]
        Azure[Azure Resources]
        GCP[GCP Resources]
    end
    
    subgraph "Platform Layer"
        K8s[Kubernetes Clusters]
        SM[Service Mesh]
        API[API Gateway]
    end
    
    subgraph "Application Layer"
        MS[Microservices]
        DB[(Databases)]
        Cache[(Cache Layer)]
    end
    
    subgraph "Operations Layer"
        Mon[Monitoring]
        Log[Logging]
        AI[AI Orchestration]
    end
    
    AWS --> K8s
    Azure --> K8s
    GCP --> K8s
    K8s --> SM
    SM --> API
    API --> MS
    MS --> DB
    MS --> Cache
    Mon --> AI
    Log --> AI
    AI --> K8s
```bash

## Component Details

### Infrastructure Layer
- **Compute:** Auto-scaling VM instances and container orchestration
- **Storage:** Distributed storage with automated backup and replication
- **Networking:** Software-defined networking with security controls
- **Security:** Identity management, encryption, and compliance monitoring

### Platform Layer
- **Container Orchestration:** Kubernetes with multi-cluster management
- **Service Mesh:** Istio for service-to-service communication
- **API Management:** Centralized API gateway with rate limiting and authentication
- **Configuration Management:** GitOps-based configuration deployment

### Application Layer
- **Microservices Architecture:** Domain-driven service decomposition
- **Data Layer:** Multi-database strategy with CQRS patterns
- **Caching Strategy:** Distributed caching with Redis clusters
- **Message Queuing:** Event-driven architecture with Kafka

### Operations Layer
- **Monitoring:** Prometheus and Grafana with custom dashboards
- **Logging:** Centralized logging with ELK stack
- **AI Orchestration:** Machine learning for predictive operations
- **Incident Response:** Automated incident detection and response

## Technology Stack

| Layer | Technologies | Purpose |
|-------|-------------|---------|
| Infrastructure | Terraform, Ansible | Infrastructure as Code |
| Container Platform | Kubernetes, Docker | Container orchestration |
| Service Mesh | Istio, Envoy | Service communication |
| Monitoring | Prometheus, Grafana | Metrics and alerting |
| Logging | Elasticsearch, Logstash, Kibana | Log aggregation |
| CI/CD | GitHub Actions, ArgoCD | Deployment automation |
| Security | Vault, OPA, Falco | Security and compliance |
| AI/ML | TensorFlow, Kubeflow | AI-driven operations |

## Security Architecture

### Security Controls
- **Identity and Access Management:** RBAC with OIDC integration
- **Network Security:** Zero-trust networking with micro-segmentation
- **Data Protection:** Encryption at rest and in transit
- **Compliance:** Automated compliance monitoring and reporting

### Security Layers
1. **Perimeter Security:** WAF, DDoS protection, network firewalls
2. **Application Security:** OWASP compliance, security scanning
3. **Data Security:** Encryption, access controls, audit logging
4. **Runtime Security:** Container security, behavioral monitoring

## Scalability and Performance

### Scaling Strategies
- **Horizontal Scaling:** Auto-scaling based on metrics and predictions
- **Vertical Scaling:** Resource optimization and right-sizing
- **Geographic Distribution:** Multi-region deployment for latency optimization
- **Load Balancing:** Intelligent traffic distribution

### Performance Optimization
- **Caching Strategy:** Multi-level caching with intelligent invalidation
- **Database Optimization:** Query optimization and connection pooling
- **Network Optimization:** CDN integration and edge computing
- **Resource Optimization:** AI-driven resource allocation

## Disaster Recovery and Business Continuity

### Backup Strategy
- **Data Backup:** Automated, encrypted backups with point-in-time recovery
- **Configuration Backup:** GitOps-based configuration versioning
- **Application Backup:** Container image and state backup
- **Cross-Region Replication:** Multi-region data replication

### Recovery Procedures
- **RTO Target:** 15 minutes for critical services
- **RPO Target:** 5 minutes maximum data loss
- **Failover Strategy:** Automated failover with manual override
- **Testing:** Regular disaster recovery testing and validation
```bash

**Deliverable:** Complete system architecture documentation with diagrams

#### 2.2 Multi-Cloud Strategy Documentation (45 minutes)

Create `docs/architecture/multi-cloud-strategy.md` detailing:
- Cloud provider selection criteria
- Workload distribution strategy
- Data synchronization and consistency
- Cost optimization across clouds
- Vendor lock-in mitigation strategies

Include specific implementation details for:
- AWS-specific configurations and services
- Azure integration patterns and services
- GCP deployment strategies and services
- Cross-cloud networking and security

**Deliverable:** Comprehensive multi-cloud strategy documentation

## Exercise 3: Operational Runbook Development (120 minutes)

### Objective
Create detailed operational runbooks for key system management procedures.

### Tasks

#### 3.1 Deployment Runbook Creation (40 minutes)

```bash
# Create deployment runbook specification
uvx --from git+https://github.com/github/spec-kit.git specify init deployment_runbooks --ai copilot
```bash

Create `docs/operations/runbooks/application-deployment.md`:

```markdown
# Application Deployment Runbook

## Overview
- **Purpose:** Deploy applications to HX-Infrastructure platform
- **Scope:** Production and staging environment deployments
- **Prerequisites:** Access to deployment tools, validated application artifacts
- **Estimated Time:** 15-30 minutes depending on application complexity

## Pre-Deployment Checklist
- [ ] Application artifacts validated and tested
- [ ] Deployment configuration reviewed and approved
- [ ] Database migrations prepared (if applicable)
- [ ] Rollback plan prepared and validated
- [ ] Monitoring and alerting configured
- [ ] Stakeholders notified of deployment window

## Deployment Procedure

### Step 1: Environment Preparation
**Objective:** Ensure target environment is ready for deployment

```bash
# Verify cluster health
kubectl get nodes
kubectl get pods --all-namespaces | grep -v Running

# Check resource availability
kubectl top nodes
kubectl describe nodes | grep -A 5 "Allocated resources"

# Verify monitoring systems
curl -s http://prometheus:9090/-/healthy
curl -s http://grafana:3000/api/health
```bash

**Expected Output:** All nodes healthy, sufficient resources available, monitoring systems operational

**Validation:** 
- All cluster nodes in Ready state
- Resource utilization below 80%
- Monitoring endpoints responding

### Step 2: Application Deployment
**Objective:** Deploy application using GitOps workflow

```bash
# Update application configuration
cd /path/to/gitops-repo
git checkout main
git pull origin main

# Update application version
sed -i "s|image:\s*app:v[0-9.]*|image: app:v${NEW_VERSION}|" applications/app/deployment.yaml

# Commit and push changes
git add applications/app/deployment.yaml
git commit -m "Deploy app version ${NEW_VERSION}"
git push origin main

# Monitor ArgoCD sync
argocd app sync app-production
argocd app wait app-production --health
```bash

**Expected Output:** ArgoCD successfully syncs and application reaches healthy state

**Validation:**
- ArgoCD shows application as synced and healthy
- All pods in Running state
- Health checks passing

### Step 3: Post-Deployment Validation
**Objective:** Verify deployment success and application functionality

```bash
# Check application pods
kubectl get pods -l app=myapp -n production

# Verify service endpoints
kubectl get svc -n production
curl -s http://myapp.production.svc.cluster.local/health

# Check application logs
kubectl logs -l app=myapp -n production --tail=50

# Verify metrics collection
curl -s http://prometheus:9090/api/v1/query?query=up{job="myapp"}
```bash

**Expected Output:** All pods running, health endpoints responding, metrics being collected

**Validation:**
- Application health check returns 200 OK
- No error logs in recent application logs
- Prometheus collecting application metrics

### Step 4: Smoke Testing
**Objective:** Perform basic functionality testing

```bash
# Run automated smoke tests
cd /path/to/test-suite
./run-smoke-tests.sh --environment production --app myapp

# Verify key user journeys
curl -s -X POST http://myapp.production/api/test-endpoint \
  -H "Content-Type: application/json" \
  -d '{"test": "data"}'

# Check database connectivity (if applicable)
kubectl exec -it deployment/myapp -n production -- \
  /app/scripts/test-db-connection.sh
```bash

**Expected Output:** All smoke tests pass, API endpoints responding correctly

**Validation:**
- Smoke test suite returns 0 exit code
- API responses match expected format
- Database connectivity confirmed

## Troubleshooting

| Issue | Symptoms | Resolution |
|-------|----------|------------|
| Pod CrashLoopBackOff | Pods continuously restarting | Check logs: `kubectl logs <pod> -n production` |
| Service Unavailable | Health checks failing | Verify service configuration and pod readiness |
| Database Connection Failed | Application cannot connect to DB | Check database credentials and network policies |
| High Memory Usage | Pods being OOMKilled | Review resource limits and application memory usage |

## Rollback Procedure

### Emergency Rollback
If critical issues are detected:

```bash
# Immediate rollback to previous version
argocd app rollback app-production

# Or manual rollback
kubectl rollout undo deployment/myapp -n production

# Verify rollback success
kubectl rollout status deployment/myapp -n production
```bash

### Planned Rollback
For planned rollbacks:

```bash
# Update GitOps repository to previous version
cd /path/to/gitops-repo
git revert HEAD
git push origin main

# Monitor ArgoCD sync
argocd app sync app-production
argocd app wait app-production --health
```bash

## Post-Deployment Validation

### Immediate Validation (0-15 minutes)
- [ ] All pods in Running state
- [ ] Health checks passing
- [ ] No error logs in application logs
- [ ] Metrics being collected

### Extended Validation (15-60 minutes)
- [ ] Performance metrics within acceptable ranges
- [ ] No increase in error rates
- [ ] User acceptance testing completed
- [ ] Monitoring alerts not triggered

### Long-term Validation (1-24 hours)
- [ ] System stability maintained
- [ ] Performance baselines met
- [ ] No degradation in user experience
- [ ] Resource utilization stable

## Communication

### Deployment Notification Template
```bash
Subject: [DEPLOYMENT] Application v${VERSION} deployed to Production

Deployment Details:
- Application: ${APP_NAME}
- Version: ${VERSION}
- Environment: Production
- Deployment Time: ${TIMESTAMP}
- Deployed By: ${DEPLOYER}

Validation Results:
- Health Checks: ✅ Passing
- Smoke Tests: ✅ Passed
- Performance: ✅ Within baselines

Next Steps:
- Monitor application for 24 hours
- Extended validation in progress
- Rollback plan available if needed

Contact: ${CONTACT_INFO}
```bash

### Incident Escalation
If issues are detected:
1. **Immediate:** Notify on-call engineer via PagerDuty
2. **15 minutes:** Escalate to team lead if unresolved
3. **30 minutes:** Engage incident commander
4. **60 minutes:** Consider rollback if no resolution path
```bash

**Deliverable:** Complete deployment runbook with troubleshooting guide

#### 3.2 Monitoring and Incident Response Runbook (40 minutes)

Create `docs/operations/runbooks/incident-response.md` covering:
- Incident classification and severity levels
- Response team roles and responsibilities
- Escalation procedures and timelines
- Communication protocols
- Post-incident review process

Include specific procedures for:
- Service outage response
- Performance degradation handling
- Security incident response
- Data loss or corruption incidents

**Deliverable:** Comprehensive incident response runbook

#### 3.3 Backup and Recovery Runbook (40 minutes)

Create `docs/operations/runbooks/backup-recovery.md` detailing:
- Backup procedures and schedules
- Recovery testing protocols
- Disaster recovery activation
- Data restoration procedures
- Business continuity measures

Include step-by-step procedures for:
- Database backup and restoration
- Configuration backup and recovery
- Application state backup
- Cross-region failover procedures

**Deliverable:** Complete backup and recovery runbook

## Exercise 4: Configuration Template Development (90 minutes)

### Objective
Create reusable configuration templates for common infrastructure and application patterns.

### Tasks

#### 4.1 Ansible Role Templates (30 minutes)

Create standardized Ansible role templates in `templates/ansible/`:

```bash
mkdir -p templates/ansible/{role-template,playbook-template}

# Create role template structure
cd templates/ansible/role-template
mkdir -p {tasks,handlers,templates,files,vars,defaults,meta}
```bash

Create `templates/ansible/role-template/README.md`:
```markdown
# Ansible Role Template

## Overview
This template provides a standardized structure for Ansible roles in the HX-Infrastructure project.

## Directory Structure
```bash
role-name/
├── tasks/          # Main tasks and task includes
├── handlers/       # Event handlers
├── templates/      # Jinja2 templates
├── files/          # Static files to copy
├── vars/           # Role variables
├── defaults/       # Default variables
├── meta/           # Role metadata and dependencies
└── README.md       # Role documentation
```bash

## Usage
1. Copy this template directory
2. Rename to your role name
3. Update meta/main.yml with role information
4. Implement tasks in tasks/main.yml
5. Add appropriate tests and documentation

## Standards
- Follow Ansible best practices
- Use descriptive variable names
- Include comprehensive documentation
- Implement idempotent tasks
- Add appropriate tags for task control
```bash

**Deliverable:** Complete Ansible role template with documentation

#### 4.2 Terraform Module Templates (30 minutes)

Create `templates/terraform/module-template/` with:
- Standard module structure
- Variable definitions and validation
- Output specifications
- Documentation templates
- Example usage

**Deliverable:** Reusable Terraform module template

#### 4.3 CI/CD Pipeline Templates (30 minutes)

Create `templates/cicd/` with templates for:
- GitHub Actions workflows
- Application deployment pipelines
- Infrastructure deployment pipelines
- Security scanning workflows
- Testing and validation pipelines

**Deliverable:** Complete CI/CD pipeline template library

## Exercise 5: Quality Assurance and Validation (60 minutes)

### Objective
Implement comprehensive quality assurance processes for all created content.

### Tasks

#### 5.1 Content Validation Framework (30 minutes)

Create enhanced validation scripts:

```bash
mkdir -p scripts/validation

# Create comprehensive validation script
cat > scripts/validation/validate-day2-content.sh << 'EOF'
#!/usr/bin/env bash
set -euo pipefail
IFS=$'
	'

# Day 2 content validation script

echo "Validating Day 2 HX-KB content..."

# Check sprint documentation
sprint_docs=("sprint-1-summary.md" "sprint-2-summary.md" "sprint-3-summary.md" "sprint-4-summary.md")
for doc in "${sprint_docs[@]}"; do
    if [ -f "docs/history/sprints/$doc" ]; then
        echo "✓ $doc exists"
        # Check for required sections
        if grep -q "## Overview" "docs/history/sprints/$doc" && \
           grep -q "## Key Achievements" "docs/history/sprints/$doc" && \
           grep -q "## Lessons Learned" "docs/history/sprints/$doc"; then
            echo "✓ $doc has required sections"
        else
            echo "✗ $doc missing required sections"
            exit 1
        fi
    else
        echo "✗ $doc missing"
        exit 1
    fi
done

# Check architecture documentation
arch_docs=("overview.md" "multi-cloud-strategy.md")
for doc in "${arch_docs[@]}"; do
    if [ -f "docs/architecture/$doc" ]; then
        echo "✓ Architecture $doc exists"
    else
        echo "✗ Architecture $doc missing"
        exit 1
    fi
done

# Check runbooks
runbooks=("application-deployment.md" "incident-response.md" "backup-recovery.md")
for runbook in "${runbooks[@]}"; do
    if [ -f "docs/operations/runbooks/$runbook" ]; then
        echo "✓ Runbook $runbook exists"
    else
        echo "✗ Runbook $runbook missing"
        exit 1
    fi
done

# Check templates
template_dirs=("ansible" "terraform" "cicd")
for dir in "${template_dirs[@]}"; do
    if [ -d "templates/$dir" ]; then
        echo "✓ Template directory $dir exists"
    else
        echo "✗ Template directory $dir missing"
        exit 1
    fi
done

echo "Day 2 content validation passed!"
EOF

chmod +x scripts/validation/validate-day2-content.sh
```bash

**Deliverable:** Comprehensive validation framework for Day 2 content

#### 5.2 Quality Review and Improvement (30 minutes)

Run validation and improve content quality:

```bash
# Run validation
./scripts/validation/validate-day2-content.sh

# Check markdown formatting
find docs -name "*.md" -exec markdownlint {} \; 2>/dev/null || echo "Install markdownlint for formatting checks"

# Validate internal links
find docs -name "*.md" -exec grep -l "\[.*\](.*\.md)" {} \; | while read file; do
    echo "Checking links in $file"
    grep -o "\[.*\](.*\.md)" "$file" | sed 's/.*(\(.*\))/\1/' | while read link; do
        if [ -f "$link" ] || [ -f "$(dirname "$file")/$link" ]; then
            echo "✓ Link $link valid"
        else
            echo "✗ Broken link $link in $file"
        fi
    done
done
```bash

Review and improve:
- Content completeness and accuracy
- Formatting consistency
- Link validity
- Code example functionality
- Documentation clarity

**Deliverable:** Quality-validated content with improvements implemented

## Success Metrics

### Quantitative Measures
- **Sprint Documentation:** 4 complete sprint summaries created
- **Architecture Documentation:** 2 comprehensive architecture documents
- **Runbooks:** 3 detailed operational runbooks created
- **Templates:** Complete template library for Ansible, Terraform, and CI/CD
- **Validation Success:** All validation scripts pass

### Qualitative Measures
- **Completeness:** All sections include required content
- **Accuracy:** Technical information is correct and current
- **Usability:** Documentation is clear and actionable
- **Consistency:** Formatting and structure are consistent across documents

## Troubleshooting Guide

### Common Issues

#### Issue: Specification creation fails
**Symptoms:** Spec Kit commands return errors
**Solution:**
```bash
# Check Spec Kit installation
uvx --from git+https://github.com/github/spec-kit.git specify --help

# Reinstall if needed
uv cache clean
uvx --from git+https://github.com/github/spec-kit.git specify init test_project --ai copilot
```bash

#### Issue: Content validation fails
**Symptoms:** Validation scripts report missing content
**Solution:**
```bash
# Check specific validation errors
./scripts/validation/validate-day2-content.sh

# Create missing content based on templates
cp templates/documentation/sprint-summary-template.md docs/history/sprints/sprint-1-summary.md
```bash

#### Issue: Markdown formatting issues
**Symptoms:** Inconsistent formatting across documents
**Solution:**
```bash
# Install markdownlint
npm install -g markdownlint-cli

# Fix formatting issues
find docs -name "*.md" -exec markdownlint --fix {} \;
```bash

## Next Steps

Upon completion of Day 2 exercises:

1. **Comprehensive Review:** Validate all deliverables against success criteria
2. **Integration Testing:** Test integration with existing systems and workflows
3. **Stakeholder Feedback:** Gather feedback from potential users
4. **Day 3 Preparation:** Review advanced optimization topics and complex scenarios

## Resources

- [Sprint Documentation Template](../../templates/documentation/sprint-summary-template.md)
- [Architecture Documentation Guide](../../docs/guides/architecture-documentation.md)
- [Runbook Best Practices](../../docs/guides/runbook-best-practices.md)
- [Template Development Guide](../../docs/guides/template-development.md)

---

*← [Day 1 Exercises](day1-foundation-exercises.md) | [Day 3 Exercises](day3-advanced-exercises.md) →*
