# INCIDENT: <short title>

Date: 2025-12-09
Systems: Torrent VM / Plex VM
Severity: High
Status: Closed

## Symptoms
- VM became slow
- apt commands failed
- Plex/Radarr errors

## Impact
- Media services disrupted
- VM partially unusable

## Root Cause
- Root filesystem filled by downloads/logs

## Fix
```bash
df -h
du -sh /*
rm -rf /var/log/<something>
'''