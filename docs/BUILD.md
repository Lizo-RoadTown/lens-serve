# lens-serve — build-out plan (self-directed)

This is lens-serve's own plan for working itself out. Work top-down; check items off
and append what you learned. Precedent to consult (not to copy as identity): the decomposition method +
PROVES run log in the lens-core repo (github.com/Lizo-RoadTown/lens-core —
`docs/decomposition/proves/process-log.md` and `skills/decomposition/SKILL.md`),
the PROVES source itself (read-only), and the PROVES spine
`staging_extractions → validation_decisions → core_entities`.

## What lens-serve must become

- [ ] **1. A read layer over `verified`.** Read-only access to the verified library —
  never touch the pipeline tables.
- [ ] **2. A query API.** Serve queries over `verified` to callers.
- [ ] **3. An MCP server.** Expose read tools (search / get / list) so agents can
  query the verified library the same way people do.
- [ ] **4. The `serve` CLI.** Stands up the API + MCP interface.
- [ ] **5. Tests.** Read layer (mocked/temp DB), query API, MCP tool contracts.
  Mirror the stdlib + pytest style of `tapestry-cli`.

### Migrate-from (precedent, generalize — do not copy as identity)
- PROVES `mcp-server/` — already the cleanest standalone module:
  - `server.py` read tools: `search_knowledge`, `get_entity`, `list_entities`.
  - `db.py` read-only `SELECT`s.
- Make source URLs / registry **injected config**, not baked identity.

## What you own vs. don't
Own: read/query over `verified`. Do NOT implement any pipeline writes — no intake,
review, promotion, or observe here. lens-serve is read-only over verified.

## Record as you go
Append here: what you built, what you needed, what's missing, what you had to decide.
Also write it to loom-memory scoped to `lens-serve`. This log is capture-before-loss.
