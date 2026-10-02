from pathlib import Path
import re, yaml
ROOT=Path(__file__).resolve().parents[1]

def test_manifest_core_open_gap_010_fields():
    m=yaml.safe_load((ROOT/'agent.yaml').read_text())
    assert m['spec_version']=='0.1.0'
    assert re.fullmatch(r'[a-z][a-z0-9-]*',m['name'])
    assert re.fullmatch(r'\d+\.\d+\.\d+',str(m['version']))
    assert isinstance(m['description'],str) and m['description']

def test_declared_skills_and_tools_are_real():
    m=yaml.safe_load((ROOT/'agent.yaml').read_text())
    for s in m['skills']: assert (ROOT/'skills'/f'{s}.md').exists()
    for t in m['tools']: assert (ROOT/'tools'/f'{t.replace("-","_")}.py').exists()

def test_no_known_unsupported_fields():
    m=yaml.safe_load((ROOT/'agent.yaml').read_text())
    for k in ['display_name','entrypoint','portability']: assert k not in m
