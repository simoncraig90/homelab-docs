# Proxmox Host Recovery Runbook

## Purpose
This runbook documents the procedure to recover the Proxmox host and restore
critical VMs after a catastrophic host failure (e.g., hardware failure, disk
failure, or non-bootable host).

It is written for a single-node Proxmox environment and prioritizes:
- restoring core services quickly
- preserving data integrity
- minimizing guesswork under pressure

## Scope
Covered:
- Rebuilding the Proxmox host from scratch
- Restoring VM configuration and disks from backups
- Verifying services after restore

Not covered:
- High availability (HA) clusters
- Multi-host failover
- Complex storage migrations

## Preconditions / Assumptions
- Backups exist (e.g., Proxmox Backup Server, external storage, or offline backups)
- VM disk storage and backup locations are documented in `LAB-MAP.md`
- Any required install media and licenses are available
- Network basics are known (gateway, DHCP/static approach, DNS)

## Definitions
- **Host**: the Proxmox VE hypervisor running on the physical Minisforum machine
- **Backup source**: where VM backups are stored (PBS / external disk / NAS)
- **Critical VMs**: minimum set required to restore core services

---

## Recovery Strategy Overview

### Phase 1: Stabilize the host
1. Confirm hardware is functional (power, disk presence, RAM seating).
2. Reinstall Proxmox VE.
3. Restore baseline networking.
4. Attach storage and backup sources.

### Phase 2: Restore critical services
1. Restore the most critical VMs first (networking-dependent services last).
2. Validate each VM before moving on.
3. Restore less critical VMs after core services are stable.

---

## Phase 0: Incident Notes (do this before changing anything)
If the host is partially alive, collect facts before reinstallation:

- What failed? (disk, bootloader, networking, config, etc.)
- What was the last known good change?
- What errors are shown on console?
- Capture photos/screenshots of error messages.

Record a short incident entry in `INCIDENTS/` (even if incomplete).

---

## Phase 1: Rebuild the Proxmox Host

### 1. Install Proxmox VE
1. Download the latest Proxmox VE ISO (official source).
2. Boot the host from USB installer.
3. Install Proxmox on the intended OS disk.

Notes:
- Prefer a clean install over “repair” for predictable recovery.
- Use a hostname consistent with existing documentation.

### 2. Initial Host Access
1. Log in on the host console.
2. Confirm the web UI is reachable from the LAN.
3. Apply updates:
   - `apt update`
   - `apt full-upgrade`

### 3. Restore Baseline Networking
Goal: reach a state where:
- the host has LAN access
- you can reach the Proxmox web UI
- the host can reach the backup source

Document your network approach in `LAB-MAP.md`:
- DHCP vs static IP
- bridge name(s) used for VMs
- any VLANs (if used)

### 4. Reattach Storage
Depending on your setup, restore storage for VM disks:
- local disk(s)
- ZFS pool (if used)
- LVM-thin storage (if used)
- external storage (if used)

Confirm storage appears in:
- Proxmox UI → Datacenter → Storage
- `lsblk` / `pvs` / `vgs` / `lvs` (as relevant)

---

## Phase 2: Restore From Backups

### 1. Connect Backup Source
If using Proxmox Backup Server (PBS):
- Add PBS storage target in Proxmox UI
- Confirm backups are visible

If using external disk:
- Mount disk
- Add as a storage target in Proxmox
- Confirm backup files are accessible

### 2. Restore Order (Recommended)
Restore VMs in this order (adjust to your lab):
1. **Core services** (authentication not required)
2. **Media** (if used daily)
3. **Auto**
