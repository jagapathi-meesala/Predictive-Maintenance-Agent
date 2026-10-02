# Rules

1. Reject malformed or missing required inputs.
2. Do not silently convert incompatible units.
3. Do not fabricate sensor readings, maintenance history, or failure labels.
4. Return structured errors for invalid requests.
5. Never expose environment secrets in outputs or logs.
6. File paths are never accepted as an implicit data source by domain tools.
7. Risk scores are analytical indicators, not guarantees.
8. A high-risk result requires human inspection before intervention.
