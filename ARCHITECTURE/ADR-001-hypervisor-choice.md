# ADR-001: Hypervisor Choice

## Status
Accepted

## Context
A single physical host is used to run multiple workloads with different
stability, performance, and risk profiles, including:

- Always-on media services
- Automation and background jobs
- Monitoring and observability tooling
- Experimental and learning workloads

The environment requires:
- Strong VM isolation
- Snapshot and backup support
- Reasonable performance on consumer-grade hardware
- A manageable operational footprint for a single operator

## Options Considered

### Option 1: Proxmox VE
- KVM-based virtualization
- Web-based management interface
- Native snapshotting and backup integration
- Supports containers and VMs
- Active community and documentation

### Option 2: VMware ESXi (Free / Licensed)
- Mature enterprise hypervisor
- Strong performance and ecosystem
- Licensing limitations for backups and automation
- Reduced long-term viability for non-commercial use

### Option 3: Bare Metal Linux with libvirt
- Maximum flexibility
- Minimal abstraction
- Higher operational complexity
- Requires building management, backups, and tooling manually

## Decision
Proxmox VE was selected as the hypervisor for this environment.

## Rationale
Proxmox provides a strong balance between:
- Isolation and flexibility
- Ease of management
- Snapshot and backup capabilities
- Community support and documentation

It allows rapid iteration and experimentation while still supporting
production-style workflows such as recovery procedures and incident response.

## Consequences

### Positive
- Clear separation of workloads via VMs
- Simple snapshot and rollback operations
- Centralized management through a web UI
- Supports future automation (API, Terraform, Ansible)

### Negative
- Higher overhead than container-only solutions
- Requires learning Proxmox-specific concepts
- Single-host design remains a point of failure

## Notes
This decision may be revisited if:
- The environment expands to multiple hosts
- Hardware capabilities change significantly
- Operational requirements evolve beyond a single-node setup
