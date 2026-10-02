from core.agent_core import AgentCore

def test_reject_non_object():
    r=AgentCore().run('assess-asset-health', [])
    assert not r.ok and r.error['code']=='invalid_type'

def test_missing_required_field():
    r=AgentCore().run('assess-asset-health', {'temperature_c':50})
    assert not r.ok and r.error['code']=='missing_required'

def test_negative_value_rejected():
    r=AgentCore().run('assess-asset-health', {'temperature_c':50,'vibration_mm_s':-1,'operating_hours':10})
    assert not r.ok and r.error['code']=='invalid_value'

def test_nan_rejected():
    r=AgentCore().run('estimate-failure-risk', {'temperature_c':float('nan'),'vibration_mm_s':1,'recent_failures':0,'maintenance_overdue_days':0})
    assert not r.ok and r.error['code']=='invalid_number'
