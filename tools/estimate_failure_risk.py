from __future__ import annotations
from contracts.tool_contract import Tool, ToolError
from ._common import require, finite_number

SCHEMA = {"type":"object","required":["temperature_c","vibration_mm_s","recent_failures","maintenance_overdue_days"],"properties":{}}

def validate(p):
    require(p, ["temperature_c","vibration_mm_s","recent_failures","maintenance_overdue_days"])
    for k in ("temperature_c","vibration_mm_s","recent_failures","maintenance_overdue_days"): finite_number(p[k], k)
    if any(p[k] < 0 for k in ("vibration_mm_s","recent_failures","maintenance_overdue_days")): raise ToolError("invalid_value", "Counts and durations cannot be negative")

def execute(p):
    t,v,f,d = [float(p[k]) for k in ("temperature_c","vibration_mm_s","recent_failures","maintenance_overdue_days")]
    components={"temperature":min(max((t-50)/50,0),1),"vibration":min(v/12,1),"history":min(f/3,1),"overdue":min(d/30,1)}
    risk=100*(0.30*components["temperature"]+0.35*components["vibration"]+0.20*components["history"]+0.15*components["overdue"])
    band="high" if risk>=70 else "medium" if risk>=40 else "low"
    return {"risk_score":round(risk,2),"risk_band":band,"components":{k:round(v,3) for k,v in components.items()},"recommendation":"Inspect and schedule maintenance review" if band=="high" else "Continue monitoring" if band=="medium" else "Continue routine maintenance"}

TOOL=Tool("estimate-failure-risk","Estimate near-term failure risk using transparent weighted indicators.",SCHEMA,validate,execute)
