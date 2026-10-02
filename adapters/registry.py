from .portable_adapter import RegistryAdapter, SUPPORTED_ADAPTERS


def build_adapter_registry(tool_registry):
    return {name: RegistryAdapter(name, tool_registry) for name in SUPPORTED_ADAPTERS}
