# Homelab Overview

## Physical Host
- Minisforum AI Pro
- Role: Hypervisor + GPU host

## Core VMs
- plex      → Media serving
- torrent   → Downloading
- scripts   → Automation / scrapers
- (planned) ai-core → Model inference only

## Design Rules
- No scraping on AI VMs
- No AI models on utility VMs
- One responsibility per VM