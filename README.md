# Predictive Maintenance Agent

A framework-independent OpenGAP-style agent for transparent equipment health assessment, failure-risk screening, and sensor anomaly detection.

## Architecture
`agent.yaml` declares the agent identity, skills, and tools. `core/` provides a dynamic registry and execution core; `contracts/` defines the framework-independent tool interface; `tools/` contains deterministic domain implementations; `adapters/` exposes a small common invocation interface for OpenAI SDK, CrewAI, Claude Code, and Lyzr integration without importing their SDKs.

## Installation
Create an isolated Python environment and install `requirements.txt` with pip. The runtime itself uses Python standard-library functionality for domain calculations.

## Configuration
Runtime settings are read from environment variables in `config/settings.py`. No API keys, passwords, tokens, or production credentials are committed.

## Tools
- `assess-asset-health`: normalized 0-100 health assessment.
- `estimate-failure-risk`: transparent 0-100 risk screening.
- `detect-sensor-anomalies`: population z-score outlier detection.

## Skills
- `predictive-maintenance`
- `asset-health-assessment`
- `failure-risk-analysis`

## Usage
Instantiate `core.agent_core.AgentCore`, inspect `capabilities()`, and call `run(tool_name, payload)`. The result follows the common `ToolResult` contract.

## Testing
Run `pytest -q` from the repository root. The suite covers tools, contracts, registry behavior, adapters, security, documentation, and manifest checks.

## Portability
The core does not depend on an AI framework. Adapter interfaces are provided for OpenAI SDK, CrewAI, Claude Code, and Lyzr, but this repository does not claim that external SDK integrations have been end-to-end tested.

## Limitations
The domain formulas are deterministic screening heuristics, not calibrated production models. They do not establish a guaranteed failure probability or remaining useful life and should not directly control safety-critical equipment.
