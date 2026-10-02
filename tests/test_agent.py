from core.agent_core import AgentCore

def test_capabilities_are_dynamic_and_declared():
    agent=AgentCore()
    assert agent.capabilities()==['assess-asset-health','detect-sensor-anomalies','estimate-failure-risk']

def test_health_execution():
    r=AgentCore().run('assess-asset-health', {'temperature_c':50,'vibration_mm_s':2,'operating_hours':1000})
    assert r.ok and 0 <= r.data['health_score'] <= 100

def test_unknown_tool_error():
    try: AgentCore().run('missing-tool', {})
    except Exception as exc: assert 'Unknown tool' in str(exc)
