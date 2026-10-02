from __future__ import annotations
from contracts.tool_contract import Tool, ToolError
from ._common import require, finite_number

SCHEMA = {"type":"object","required":["temperature_c","vibration_mm_s","operating_hours"],"properties":{}}

def validate(p):
    require(p, ["temperature_c", "vibration_mm_s", "operating_hours"])
    for k in ("temperature_c", "vibration_mm_s", "operating_hours"): finite_number(p[k], k)
    if p["operating_hours"] < 0: raise ToolError("invalid_value", "operating_hours cannot be negative")
    if p["vibration_mm_s"] < 0: raise ToolError("invalid_value", "vibration_mm_s cannot be negative")

def execute(p):
    t, v, h = float(p["temperature_c"]), float(p["vibration_mm_s"]), float(p["operating_hours"])
    temp_score = min(max((t - 40.0) / 60.0, 0.0), 1.0)
    vib_score = min(max(v / 10.0, 0.0), 1.0)
    age_score = min(h / 20000.0, 1.0)
    health = max(0.0, min(100.0, 100.0 * (1.0 - (0.45*temp_score + 0.40*vib_score + 0.15*age_score))))
    band = "good" if health >= 75 else "watch" if health >= 50 else "critical"
    return {"health_score": round(health,2), "health_band": band, "components":{"temperature":round(temp_score,3),"vibration":round(vib_score,3),"age":round(age_score,3)}}

TOOL = Tool("assess-asset-health", "Calculate a transparent equipment health score from operating indicators.", SCHEMA, validate, execute)
