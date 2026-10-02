from core.agent_core import ToolRegistry
from tools.assess_asset_health import TOOL

def test_register_and_discover():
    reg=ToolRegistry(); reg.register(TOOL)
    assert reg.discover()==['assess-asset-health']

def test_duplicate_registration():
    reg=ToolRegistry(); reg.register(TOOL)
    try: reg.register(TOOL)
    except ValueError as exc: assert 'already registered' in str(exc)
