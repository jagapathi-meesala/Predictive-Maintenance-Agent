# Agent Instructions

Use `agent.yaml` as the capability manifest and `SOUL.md` as the identity definition. Load only the skills relevant to the requested maintenance analysis.

All domain calculations are deterministic Python implementations. Validate inputs first, execute one registered tool at a time, and return structured JSON-compatible dictionaries. Treat risk and health outputs as decision support rather than guaranteed machine states.
