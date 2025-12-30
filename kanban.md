# 🧠 Homelab Kanban

> Rule: maximum **2 items** in "IN PROGRESS" at any time.

---

## BACKLOG
- Proxmox recovery documentation
- Backup strategy (VMs + host)
- External USB backups
- Scalping VM restructure
- Local AI VM
- Password / secrets vault
- Kubernetes learning cluster
- Network topology diagram
- Configure Dicord webhook to monitor backups. silent for sucess. Ping on failure.
- Review naming convention for backups
- Create alerts for failed backups, silent alert for succesful backups
- Expose Jellyfin to internet for remote access
---

## TODO
- Decide backup tooling (rsync / borg / PBS)
- Add Prometheus host labels
- Evaluate Jellyfin playback (local + remote)-
- Troubleshoot backups not replicating to CIFS share

---

## IN PROGRESS


---

## DONE
- kanban.md created
- Created github structure for documentation
- Install Jellyfin on Plex VM (Tested playback, subtitles, audio, access to media library)
- Fix Jellyfin duplicates and library paths
- Mirror Radarr automation rules into Sonarr
- Backups of VM created in Proxmox (local). Retain 1 hourly 1 daily 1 monthly
- Backups replicated to Windows desktop PC on LAN via CIFS share