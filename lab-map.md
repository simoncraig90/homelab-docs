# Lab Map

This document provides a high-level map of the homelab environment.
It acts as a single source of truth for understanding VM roles,
criticality, and recovery priority.

This document is intentionally concise and focuses on *structure and intent*
rather than implementation detail.

---

## Physical Host

- Platform: Minisforum mini-PC
- Hypervisor: Proxmox VE
- Topology: Single-node host

This environment prioritises simplicity, clarity, and recoverability
over high availability.

---

## Virtual Machines

| VM Name     | Role            | Purpose                                      | Criticality | Backed Up |
|-------------|-----------------|----------------------------------------------|-------------|-----------|
| Media       | Production      | Media streaming and library management        | High        | Yes       |
| Torrent     | Production      | Download handling and ingestion               | High        | Yes       |
| Monitoring  | Infrastructure  | Metrics, dashboards, and observability        | Medium      | Yes       |
| Scripts     | Automation      | Background jobs, scripts, and schedulers      | Medium      | Yes       |
| AI-Core     | Experimental    | Local AI and inference experimentation        | Low         | No        |

VM names reflect *current operational reality*, not abstract roles.

---

## VM Roles

- **Production**
  - Services relied upon for daily use
  - Restored first after host failure

- **Automation**
  - Systems that perform background or scheduled work
  - Important, but not directly user-facing

- **Infrastructure**
  - Monitoring and visibility tooling
  - Useful during recovery, but not required for initial restore

- **Experimental**
  - Learning, testing, and rapidly changing workloads
  - Treated as disposable by design

---

## Criticality Levels

- **High**
  - Required for daily operation
  - Highest restore priority
  - Always included in external backups

- **Medium**
  - Important but non-blocking
  - Included in external backups

- **Low**
  - Non-essential or easily rebuilt
  - Excluded from backups by design

Criticality reflects *impact of loss*, not rebuild effort.

---

## Restore Priority

In the event of a host failure, recovery should proceed in the
following order:

1. Proxmox host
2. Media and Torrent VMs
3. Monitoring and Scripts VMs
4. AI-Core VM (only if required)

Detailed recovery steps are documented in:
`RUNBOOKS/proxmox-host-recovery.md`

---

## Backup Coverage Summary

- External backups are maintained for:
  - Media
  - Torrent
  - Monitoring
  - Scripts

- AI-Core is excluded intentionally
- Snapshots are used only for short-term rollback

The rationale for this approach is documented in:
`ARCHITECTURE/ADR-003-backup-and-recovery-strategy.md`

---

## Change Policy

- Any new VM must be added to this document
- Changes to VM role or criticality must be reflected here
- Architectural changes should be accompanied by a new ADR
- Minor configuration changes do not require updates

This document should remain stable, readable, and accurate over time.
