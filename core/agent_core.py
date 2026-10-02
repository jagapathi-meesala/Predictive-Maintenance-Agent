from __future__ import annotations
from contracts.tool_contract import Tool, ToolResult, ToolError
from tools import TOOLS

class ToolRegistry:
    def __init__(self): self._tools={}
    def register(self, tool: Tool):
        if tool.name in self._tools: raise ValueError(f"Tool already registered: {tool.name}")
        self._tools[tool.name]=tool
    def discover(self): return sorted(self._tools)
    def get(self,name):
        if name not in self._tools: raise ToolError("tool_not_found", f"Unknown tool: {name}")
        return self._tools[name]
    def execute(self,name,payload): return self.get(name).execute(payload)

class AgentCore:
    def __init__(self, registry=None):
        self.registry=registry or ToolRegistry()
        if not registry:
            for tool in TOOLS: self.registry.register(tool)
    def capabilities(self): return self.registry.discover()
    def run(self, tool_name, payload): return self.registry.execute(tool_name,payload)
