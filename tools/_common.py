from __future__ import annotations
from contracts.tool_contract import ToolError


def require(payload, fields):
    missing = [f for f in fields if f not in payload]
    if missing:
        raise ToolError("missing_required", "Missing required fields: " + ", ".join(missing))


def finite_number(value, field):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ToolError("invalid_number", f"{field} must be numeric")
    if value != value or value in (float("inf"), float("-inf")):
        raise ToolError("invalid_number", f"{field} must be finite")
    return float(value)
