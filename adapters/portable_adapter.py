"""Small framework-neutral adapter interface; no vendor SDK dependency."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Protocol

@dataclass(frozen=True)
class AdapterRequest:
    tool: str
    input: dict[str, Any]

@dataclass(frozen=True)
class AdapterResponse:
    ok: bool
    payload: dict[str, Any]

class Adapter(Protocol):
    framework: str
    def invoke(self, request: AdapterRequest) -> AdapterResponse: ...

class RegistryAdapter:
    def __init__(self, framework: str, registry: Any):
        self.framework = framework
        self._registry = registry

    def invoke(self, request: AdapterRequest) -> AdapterResponse:
        result = self._registry.execute(request.tool, request.input)
        return AdapterResponse(result.ok, result.data if result.ok else {"error": result.error or {}})

SUPPORTED_ADAPTERS = ("openai-sdk", "crewai", "claude-code", "lyzr")
