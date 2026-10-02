"""Framework-independent tool contract."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Callable

@dataclass(frozen=True)
class ToolResult:
    ok: bool
    tool: str
    data: dict[str, Any] | None = None
    error: dict[str, Any] | None = None

class ToolError(Exception):
    def __init__(self, code: str, message: str):
        super().__init__(message)
        self.code = code
        self.message = message

@dataclass(frozen=True)
class Tool:
    name: str
    description: str
    input_schema: dict[str, Any]
    validator: Callable[[dict[str, Any]], None]
    executor: Callable[[dict[str, Any]], dict[str, Any]]

    def validate(self, payload: Any) -> None:
        if not isinstance(payload, dict):
            raise ToolError("invalid_type", "Tool input must be an object")
        self.validator(payload)

    def execute(self, payload: dict[str, Any]) -> ToolResult:
        try:
            self.validate(payload)
            return ToolResult(True, self.name, data=self.executor(payload))
        except ToolError as exc:
            return ToolResult(False, self.name, error={"code": exc.code, "message": exc.message})
        except Exception as exc:
            return ToolResult(False, self.name, error={"code": "execution_error", "message": str(exc)})
