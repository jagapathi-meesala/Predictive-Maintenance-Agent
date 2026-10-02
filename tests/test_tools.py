from tools import TOOLS
from core.agent_core import AgentCore

def test_three_tools_exist(): assert len(TOOLS)==3

def test_risk_high_signal():
    r=AgentCore().run('estimate-failure-risk', {'temperature_c':100,'vibration_mm_s':12,'recent_failures':3,'maintenance_overdue_days':30})
    assert r.ok and r.data['risk_band']=='high'

def test_anomaly_detection():
    r=AgentCore().run('detect-sensor-anomalies', {'readings':[10,10,10,100], 'z_threshold':1.5})
    assert r.ok and r.data['anomalies'][0]['index']==3

def test_anomaly_constant_window():
    r=AgentCore().run('detect-sensor-anomalies', {'readings':[4,4,4]})
    assert r.ok and r.data['anomalies']==[]
