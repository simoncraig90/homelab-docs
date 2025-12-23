# ADR-002: VM Separation Strategy

## Context
Multiple workloads with different stability and risk profiles
are hosted on the same physical machine.

## Decision
Workloads are separated into distinct VMs based on purpose:
production, automation, experimental.

## Consequences
- Improved fault isolation
- Slightly higher management overhead