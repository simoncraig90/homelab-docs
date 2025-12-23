# Backup Verification Runbook

## Purpose
This runbook documents the process used to verify that backups are
**actually restorable**, not just present.

The goal is to ensure confidence in the backup and recovery strategy by
regularly performing controlled test restores.

This runbook complements:
- `ARCHITECTURE/ADR-003-backup-and-recovery-strategy.md`
- `RUNBOOKS/proxmox-host-recovery.md`

---

## Scope

Covered:
- Verification of VM backups via test restores
- Validation of VM boot, network, and core services
- Safe testing without impacting production workloads

Not covered:
- Continuous automated restore testing
- Full disaster simulations involving all VMs at once

---

## Preconditions / Assumptions

- External VM backups exist and are accessible
- The Proxmox host is healthy
- Sufficient temporary storage is available for a test restore
- Testing is performed during a low-impact period

---

## Verification Strategy Overview

Backup verification is performed by:
1. Selecting a representative VM
2. Restoring it into a **temporary test VM**
3. Booting and validating basic functionality
4. Deleting the test VM after verification

This approach balances confidence with operational safety.

---

## VM Selection Policy

### Regular Verification
At least one VM from each criticality tier should be tested periodically.

Recommended rotation:
- **Production**: Media or Torrent
- **Medium**: Monitoring or Scripts

### Exclusions
- **AI-Core** is excluded from verification
  - It is experimental and excluded from backups by design

---

## Phase 1: Prepare for Verification

1. Confirm no critical maintenance or upgrades are in progress.
2. Review available backup timestamps.
3. Select a recent backup that represents a realistic recovery point.
4. Note the original VMID and name.

Record the test in a simple log or note:
- Date
- VM selected
- Backup timestamp used

---

## Phase 2: Restore Backup to a Test VM

### Restore Procedure (Generic)

Using the Proxmox UI:
1. Navigate to the backup storage
2. Select the VM backup
3. Choose **Restore**
4. Restore as a **new VM** (do not overwrite production)
5. Assign a temporary VMID
6. Adjust VM name to include a suffix, e.g.:
   - `Media-restore-test`
   - `Torrent-restore-test`

Do **not** connect restored VMs to production automation or external services.

---

## Phase 3: Validation Checks

Perform the following checks on the restored VM.

### 1. Boot Verification
- VM boots without errors
- No kernel panics or immediate crashes

### 2. Network Verification
- VM receives network connectivity
- No IP conflicts with production systems
- External connectivity is not required unless relevant

### 3. Service Verification
Perform lightweight checks only:
- Core services start successfully
- No immediate fatal errors in logs

Examples:
- `systemctl --failed`
- Application-specific health checks (read-only)

### 4. Data Presence
- Expected data volumes are mounted
- Data directories exist and are readable

Deep functional testing is **not required** for verification.

---

## Phase 4: Verification Outcome

### Successful Verification
A verification is considered successful if:
- The VM boots
- Core services start
- Data is present

Record:
- Verification date
- Backup timestamp
- Result: **PASS**

### Failed Verification
If verification fails:
1. Capture error messages
2. Do **not** attempt repeated fixes
3. Record failure details
4. Open an incident entry in `INCIDENTS/`

Failures should result in:
- Investigation
- Backup strategy review
- Potential ADR update if systemic

---

## Phase 5: Cleanup

1. Power off the restored test VM
2. Delete the test VM and associated disks
3. Confirm no orphaned storage remains
4. Verify production VMs were not impacted

Cleanup is mandatory to avoid false confidence or storage exhaustion.

---

## Frequency Guidelines

Suggested minimum cadence:
- Production VM: quarterly
- Medium-criticality VM: biannually
- After major storage or backup changes: immediate test

This cadence is intentionally conservative and realistic.

---

## Relationship to Other Documents

- Backup rationale: `ARCHITECTURE/ADR-003-backup-and-recovery-strategy.md`
- Full recovery procedure: `RUNBOOKS/proxmox-host-recovery.md`
- VM roles and criticality: `LAB-MAP.md`

---

## Improvement Backlog

Future improvements may include:
- Automated restore validation
- Dedicated test storage pool
- Periodic full recovery simulations
- Backup integrity checks prior to restore

This runbook should evolve as the environment grows.
