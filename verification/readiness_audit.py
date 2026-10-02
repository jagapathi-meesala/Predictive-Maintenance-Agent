from __future__ import annotations
from pathlib import Path
import re
import yaml

ROOT=Path(__file__).resolve().parents[1]
REQUIRED_FILES=["agent.yaml","SOUL.md","README.md","AGENTS.md","DUTIES.md","RULES.md","EXPLAINABILITY.md",".env.example",".gitignore","requirements.txt","pytest.ini"]
REQUIRED_DIRS=["adapters","config","contracts","core","skills","tools","tests","verification"]

def sentence_count(text): return len(re.findall(r"(?<=[.!?])\s+", text.strip())) + (1 if text.strip() else 0)

def audit():
    errors=[]
    for f in REQUIRED_FILES:
        if not (ROOT/f).is_file(): errors.append(f"missing file: {f}")
    for d in REQUIRED_DIRS:
        if not (ROOT/d).is_dir(): errors.append(f"missing directory: {d}")
    p=ROOT/"EXPLAINABILITY.md"
    if p.exists():
        text=p.read_text()
        required=["## Inputs and Data Sources","## Decision and Reasoning","## Limits and Constraints"]
        for heading in required:
            if text.count(heading)!=1: errors.append(f"required heading count != 1: {heading}")
        for forbidden in ["## Inputs","## Decision","## Limits"]:
            if re.search(r"^" + re.escape(forbidden) + r"$", text, flags=re.MULTILINE): errors.append(f"conflicting heading: {forbidden}")
        for heading in required:
            start=text.index(heading)+len(heading)
            next_heading=text.find("\n## ", start)
            section=text[start:] if next_heading==-1 else text[start:next_heading]
            if sentence_count(section)<2: errors.append(f"section needs two sentences: {heading}")
    try:
        manifest=yaml.safe_load((ROOT/"agent.yaml").read_text())
        for key in ("spec_version","name","version","description"): 
            if key not in manifest: errors.append(f"manifest missing: {key}")
        if manifest.get("spec_version")!="0.1.0": errors.append("spec_version must be 0.1.0")
        if not re.fullmatch(r"[a-z][a-z0-9-]*", manifest.get("name","")): errors.append("invalid agent name")
        if not re.fullmatch(r"\d+\.\d+\.\d+", str(manifest.get("version",""))): errors.append("invalid semantic version")
        for skill in manifest.get("skills",[]):
            if not (ROOT/"skills"/f"{skill}.md").is_file(): errors.append(f"missing declared skill: {skill}")
        for tool in manifest.get("tools",[]):
            if not (ROOT/"tools"/f"{tool.replace('-','_')}.py").is_file(): errors.append(f"missing declared tool: {tool}")
    except Exception as exc: errors.append(f"manifest parse failure: {exc}")
    return errors

if __name__=="__main__":
    errors=audit()
    if errors:
        print("READINESS AUDIT: FAIL")
        print("\n".join(f"- {e}" for e in errors))
        raise SystemExit(1)
    print("READINESS AUDIT: PASS")
