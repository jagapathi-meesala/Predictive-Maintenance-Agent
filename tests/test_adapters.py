from adapters import build_adapter_registry
from core.agent_core import AgentCore

def test_all_target_adapter_names():
    names=build_adapter_registry(AgentCore().registry).keys()
    assert set(names)=={'openai-sdk','crewai','claude-code','lyzr'}

def test_adapter_invocation():
    adapters=build_adapter_registry(AgentCore().registry)
    response=adapters['openai-sdk'].invoke(type('R',(),{'tool':'assess-asset-health','input':{'temperature_c':40,'vibration_mm_s':0,'operating_hours':0}})())
    assert response.ok
