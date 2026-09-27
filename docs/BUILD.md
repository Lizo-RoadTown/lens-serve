# lens-serve — directions for building yourself out

This is not a spec. It orients you: how decomposition works, which piece you are,
where the source is, and the constraints that hold. You derive what to build by
working the source.

## 1. You figure out what to build — from the source

This repo was **not** handed a specification of what to build. What this module
actually does, and how, is derived by **deliberately working the original source**.
A repo cannot understand its piece from the outside. No outside agent here walked the
real build — nothing in this file was written with friction against the actual source,
so treat nothing here as authoritative. It is a starting orientation, not a plan to
execute.

## 2. How decomposition works

The Lens uses a **nearly-decomposable architecture**: modules have tight coupling
*internally* and loose coupling *across boundaries*. They meet only on well-defined
interfaces — a shared bus (the schema) — and otherwise stay out of each other's
internals. The full method lives in the `decomposition` skill in the lens-core repo
(`skills/decomposition/SKILL.md`). Read it; don't restate it from memory.

## 3. Your piece + the fragment map

**Your piece:** lens-serve is the **read side** — read-only access over `verified`,
exposed as a query API and an MCP interface so people and agents can ask the verified
library questions. You never write the pipeline tables.

**The fragment map** — all the pieces and how they meet on the shared bus:

- **lens-core** — defines the shared schema (the bus) + module composition + launcher.
- **lens-ingest** — writes `candidates` + `sources`.
- **lens-review** — reads `candidates`, writes `decisions` + `verified`.
- **lens-serve** — reads `verified` (API + MCP).
- **lens-observe** — reads activity, writes/serves signals.

Coordinate only through the shared schema. Stay in your piece; don't absorb a sibling's
work.

## 4. The source — go work it

The original source is **PROVES** (read-only) — the system The Lens was decomposed
from. A map of it lives in lens-core `docs/decomposition/proves/process-log.md`.

The parts relevant to your piece, **as places to START looking** (not a spec to copy):

- PROVES `mcp-server/src/proves_mcp/server.py` — read tools.
- PROVES `mcp-server/src/proves_mcp/db.py` — read-only queries.

Read the actual source, understand how it really works, and derive what this module
should be. Where any sketch here conflicts with the source or your own investigation,
**the source and your investigation win.** Then write down what you learned.

## 5. Structural constraints that hold regardless

- The database connection is **injected via `LENS_DB_URL`**, never hardcoded.
- Read only from the schema defined in lens-core (you read `verified`); never write the
  pipeline tables.
- Avoid the PROVES anti-patterns: parsing LLM prose as control flow; hardcoded
  `sys.path`; inline DB-URL.

## 6. Record as you go

Append here what you learned, what you needed, and what's still missing. Also write it
to loom-memory scoped to `lens-serve`. This log is capture-before-loss.
