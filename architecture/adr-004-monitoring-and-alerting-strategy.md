# ADR-004: Monitoring and Alerting Strategy

## Status
Accepted

## Context
The homelab runs a single-node Proxmox environment with several VMs:

- **Media** – production, media streaming
- **Torrent** – production, download handling
- **Monitoring** – infrastructure, metrics and dashboards
- **Scripts** – automation, background jobs and schedulers
- **AI-Core** – experimental, local AI

Previous incidents (including host storage exhaustion) showed that
issues can develop gradually and only become visible once services
are already degraded. At the same time, the environment is operated
by a single person and cannot rely on constant manual inspection.

The monitoring and alerting strategy must:

- Give early warning of predictable failure modes
- Be simple enough to maintain
- Avoid excessive noise
- Fit a single-node, non-HA lab

## Problem Statement
Without a defined monitoring strategy, it is unclear:

- Which metrics are considered critical
- Which systems must be monitored vs. best-effort
- When and how alerts should be raised
- Which issues can safely be ignored

Ad-hoc dashboards alone are not sufficient for reliable operation.

## Options Considered

### Option 1: Dashboards Only (No Alerts)
- Grafana dashboards available for manual inspection
- No automated alerting
- Low operational overhead

**Rejected**: relies on the operator remembering to look at dashboards,
providing little protection against slow-burning issues.

---

### Option 2: Full Monitoring Stack with Complex Alerts
(e.g. Prometheus + Alertmanager + Loki + extensive rules)

- Rich observability and alerting
- Flexible routing and silencing
- Higher complexity and maintenance overhead

**Rejected for now**: more complexity than needed for a single-node lab,
risk of configuration drift and unused features.

---

### Option 3: Focused Monitoring with Targeted Alerts
- Monitor a small, critical set of host and VM metrics
- Define simple, high-value alerts
- Use existing Monitoring VM as the primary observability point

**Accepted**.

## Decision
A focused monitoring and alerting strategy is adopted:

- The **Monitoring** VM is the central observability node
- A small set of critical metrics is monitored with alerts
- Additional metrics may be collected for dashboards, but **not**
  all metrics will produce alerts

Monitoring prioritises **clarity and reliability** over completeness.

## Scope of Monitoring

### Host-Level (Proxmox)
Must be monitored:

- Disk usage of system and VM storage
- CPU usage (sustained high utilisation)
- Memory usage
- Host reachability

### VM-Level
For VMs: Media, Torrent, Monitoring, Scripts

- Basic availability (up/down)
- CPU and memory usage (sustained high utilisation)
- Disk usage for important data volumes where applicable

For AI-Core (experimental):

- Best-effort metrics only, no alerts required
- Issues are acceptable and expected

## Alerting Strategy

### What Triggers Alerts
Alerts are raised for:

- Host disk usage above defined thresholds
- Host or critical VMs unreachable
- Sustained high CPU or memory on the host
- Any condition that would materially impact Media, Torrent, Monitoring,
  or Scripts

### What Does Not Trigger Alerts
No alerts for:

- Experimental VM (AI-Core) issues
- Short-lived CPU spikes
- Minor, self-correcting fluctuations

This reduces alert fatigue and keeps attention on meaningful events.

### Alert Delivery
Alert delivery mechanisms should:

- Use a channel that will actually be seen (e.g. email, messaging app)
- Be simple to maintain
- Avoid complex routing until clearly needed

The specific delivery method can evolve without changing this ADR.

## Consequences

### Positive
- Clear understanding of which systems are monitored and why
- Early warning for host and critical VM issues
- Reduced risk of silent failures (e.g. disk exhaustion)
- Monitoring effort focused where it matters most

### Negative
- Not all possible issues will be detected automatically
- Experimental workloads may fail silently
- Some manual inspection is still required

## Relationship to Other Documents

- VM roles and criticality: `lab-map.md`
- Backup and recovery strategy: `architecture/adr-003-backup-and-recovery-strategy.md`
- Proxmox host recovery: `runbooks/proxmox-host-recovery.md`
- Backup verification: `runbooks/backup-verification.md`
- Incident record and analysis: `incidents/` and `postmortems/`

## Notes
This strategy may be revisited if:

- The environment grows beyond a single host
- A more advanced alerting pipeline is introduced
- Alert noise becomes a significant problem
