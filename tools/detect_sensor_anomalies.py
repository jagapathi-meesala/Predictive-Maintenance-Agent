from __future__ import annotations
from statistics import mean, pstdev
from contracts.tool_contract import Tool, ToolError
from ._common import require

SCHEMA={"type":"object","required":["readings"],"properties":{}}

def validate(p):
    require(p,["readings"])
    if not isinstance(p["readings"], list) or len(p["readings"]) < 3: raise ToolError("invalid_value","readings must contain at least three numbers")
    for x in p["readings"]:
        if isinstance(x,bool) or not isinstance(x,(int,float)): raise ToolError("invalid_number","All readings must be numeric")

def execute(p):
    xs=[float(x) for x in p["readings"]]; mu=mean(xs); sd=pstdev(xs)
    if sd==0: return {"mean":mu,"stddev":0.0,"anomalies":[],"method":"population z-score","note":"No variation detected"}
    threshold=float(p.get("z_threshold",3.0))
    if threshold<=0: raise ToolError("invalid_value","z_threshold must be positive")
    anomalies=[{"index":i,"value":x,"z_score":round((x-mu)/sd,3)} for i,x in enumerate(xs) if abs((x-mu)/sd)>threshold]
    return {"mean":round(mu,4),"stddev":round(sd,4),"anomalies":anomalies,"method":"population z-score","threshold":threshold}

TOOL=Tool("detect-sensor-anomalies","Detect statistical outliers in an ordered sensor-reading window.",SCHEMA,validate,execute)
