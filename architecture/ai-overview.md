# AI Architecture Overview

## Purpose
Document how AI workloads are structured in the homelab to avoid sprawl,
dependency conflicts, and undocumented behaviour.

## Design Principles
- One responsibility per VM
- AI assists decision-making; it does not directly control infrastructure
- All AI services are callable via API

## Planned Components
- ai-core
  - Role: Local model inference only
  - No scraping, no cron jobs, no automation logic

- ai-agents
  - Role: Decision-making and orchestration
  - Calls ai-core via API
  - Reads/writes structured memory

- data-ingest
  - Role: Scraping and data collection
  - No AI calls
