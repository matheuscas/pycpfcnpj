"""Selects the validation backend.

Prefers the compiled Rust extension (``_speedups``) when a wheel is available
for the platform; otherwise falls back to the optimized pure-Python core so the
package always works, even installed from sdist without a Rust toolchain.

Set the environment variable ``PYCPFCNPJ_PUREPYTHON=1`` to force the pure-Python
core even when the native extension is installed (useful for benchmarking and
debugging).
"""

import os

# Pure-Python core is always importable and acts as the baseline / fallback.
from ._core import validate, validate_cnpj, validate_cpf

BACKEND = "python"

if os.environ.get("PYCPFCNPJ_PUREPYTHON") not in ("1", "true", "True"):
    try:
        from . import _speedups  # type: ignore[attr-defined]

        validate_cpf = _speedups.validate_cpf
        validate_cnpj = _speedups.validate_cnpj
        validate = _speedups.validate
        BACKEND = "rust"
    except ImportError:  # pragma: no cover - exercised on platforms without a wheel
        pass

__all__ = ["validate_cpf", "validate_cnpj", "validate", "BACKEND"]
