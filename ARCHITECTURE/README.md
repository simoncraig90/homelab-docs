# Architecture

This directory contains documentation related to the overall design of the
homelab environment and the decisions that shape its structure.

The goal of this documentation is to capture *why* decisions were made,
not just *what* was implemented.

## Scope
Architecture documentation in this directory covers:
- High-level system design
- Major technology choices
- Workload separation and boundaries
- Trade-offs and constraints

Low-level configuration details and operational procedures are documented
elsewhere (see RUNBOOKS and AUTOMATION).

## Architecture Decision Records (ADRs)
Architectural decisions are recorded using Architecture Decision Records
(ADRs). Each ADR documents a single significant decision, the context in
which it was made, and the consequences of that decision.

ADRs are intended to be:
- Concise
- Stable over time
- Updated only when decisions are explicitly revisited

### Current ADRs
- ADR-001: Hypervisor Choice

## Diagrams
High-level diagrams related to system layout, network topology, and workload
separation may be included in this directory. Diagrams are kept intentionally
abstract and avoid implementation-specific detail where possible.

## Change Policy
Changes to architecture should result in:
- A new ADR, or
- An update that explicitly supersedes an existing ADR

Minor implementation changes do not require architectural documentation.
