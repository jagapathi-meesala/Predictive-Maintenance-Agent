"""Environment-only runtime configuration."""
from __future__ import annotations
import os


def _float_env(name: str) -> float | None:
    value = os.getenv(name)
    if value is None or value.strip() == "":
        return None
    try:
        return float(value)
    except ValueError as exc:
        raise ValueError(f"{name} must be numeric") from exc


def get_settings() -> dict[str, object]:
    return {
        "log_level": os.getenv("PMA_LOG_LEVEL", "INFO"),
        "risk_high_threshold": _float_env("PMA_RISK_HIGH_THRESHOLD"),
        "anomaly_z_threshold": _float_env("PMA_ANOMALY_Z_THRESHOLD"),
    }
