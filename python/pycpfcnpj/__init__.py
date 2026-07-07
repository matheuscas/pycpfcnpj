"""pycpfcnpj — Brazilian CPF/CNPJ register-number validation.

Validation runs on a compiled Rust core when a wheel is available for the
platform, transparently falling back to an optimized pure-Python implementation
otherwise (see :mod:`pycpfcnpj._backend`).
"""

from importlib.metadata import PackageNotFoundError, version

from ._backend import BACKEND, validate, validate_cnpj, validate_cpf

try:
    __version__ = version("pycpfcnpj")
except PackageNotFoundError:  # running from a source tree without an install
    __version__ = "0.0.0"

__all__ = ["BACKEND", "validate", "validate_cpf", "validate_cnpj", "__version__"]
