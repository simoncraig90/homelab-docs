# ADR-003: Backup and Recovery Strategy

## Status
Accepted

## Context
The homelab runs on a single physical host and supports workloads with
different criticality levels, including:

- Always-on media services
- Automation and background jobs
- Monitoring and observability
- Experimental and learning workloads

Given the single-host design, failures such as disk loss, OS corruption,
or hardware failure must be assumed possible.

The environment requires a backup strategy that:
- Protects against host-level failure
- Allows predictable recovery under stress
- Balances reliability with operational simplicity
- Is maintainable by a single operator

## Problem Statement
Snapshots alone are insufficient protection against catastrophic host
failure. At the same time, enterprise-grade high availability and
replication are out of scope for this environment.

A layered, pragmatic backup approach is required.

## Options Considered

### Option 1: Snapshots Only
- Fast and convenient
- Useful for short-term rollback
- Does not protect against disk or host failure

**Rejected**: insufficient as a sole protection mechanism.

---

### Option 2: Full VM Backups Only
- Protects against host loss
- Slower restores
- Less convenient for quick rollback

**Rejected**: lacks flexibility for day-to-day recovery.

---

### Option 3: Layered Strategy (Snapshots + External Backups)
- Combines fast rollback with durable recovery
- Supports both minor and catastrophic failure scenarios
- Matches operational realities of a single-node lab

**Accepted**.

## Decision
A layered backup strategy is used:

- **Snapshots**
  - Used for short-term rollback
  - Taken before risky changes or experiments
  - Not treated as long-term backups

- **External VM Backups**
  - Used for disaster recovery
  - Stored outside the Proxmox host
  - Restorable onto a clean Proxmox installation

This strategy is documented and exercised via the Proxmox recovery runbook.

## Scope of Backups

### Included
- VM disks for production and automation workloads
- VM configuration metadata
- Critical data volumes where applicable

### Excluded (by design)
- Disposable experimental VMs
- Easily reproducible test environments
- Temporary scratch data

Exclusions are intentional to reduce noise and operational overhead.

## Recovery Objectives (Informal)
This environment does not enforce strict SLAs, but aims for:

- **RPO (Recovery Point Objective)**: last scheduled backup
- **RTO (Recovery Time Objective)**: hours, not minutes

These targets reflect realistic expectations for a single-operator lab.

## Consequences

### Positive
- Clear distinction between rollback and recovery
- Reduced risk of total data loss
- Recovery procedures are documented and repeatable
- Strategy scales with future improvements (e.g., PBS, additional storage)

### Negative
- Requires discipline to maintain backups
- External storage introduces additional failure points
- No protection against simultaneous backup + host loss

## Relationship to Other Documents
- Recovery procedures: `RUNBOOKS/proxmox-host-recovery.md`
- VM roles and criticality: `LAB-MAP.md`
- Hypervisor choice: ADR-001
- VM separation strategy: ADR-002

## Notes
This strategy may be revisited if:
- A second host is introduced
- Storage architecture changes significantly
- Automation of backup verification is implemented
