"""Generate syntactically valid CPF/CNPJ numbers — for test purposes only.

Digit calculation and weights are reused from :mod:`pycpfcnpj._core` so there is
a single implementation of the algorithm on the Python side.
"""

from __future__ import annotations

import random
import string

from ._core import CNPJ_W1, CNPJ_W2, CPF_W1, CPF_W2, _check_digit

# Alphabet for the 2026 alphanumeric CNPJ base positions (letters map to
# ``ord - 48`` exactly like validation expects).
_CNPJ_ALPHANUMERIC = string.ascii_uppercase + string.digits


def cpf() -> str:
    """Generate a valid, unmasked CPF number."""
    digits = [random.randint(0, 9) for _ in range(9)]
    d1 = _check_digit(digits, CPF_W1)
    d2 = _check_digit([*digits, d1], CPF_W2)
    return "".join(str(d) for d in (*digits, d1, d2))


def cnpj(alphanumeric: bool = False) -> str:
    """Generate a valid, unmasked CNPJ number.

    With ``alphanumeric=True`` the 12 base positions use the 2026 ``[0-9A-Z]``
    alphabet; the two check digits are always numeric.
    """
    alphabet = _CNPJ_ALPHANUMERIC if alphanumeric else string.digits
    base = [random.choice(alphabet) for _ in range(12)]
    vals = [ord(c) - 48 for c in base]
    d1 = _check_digit(vals, CNPJ_W1)
    d2 = _check_digit([*vals, d1], CNPJ_W2)
    return "".join(base) + f"{d1}{d2}"


def cpf_with_punctuation() -> str:
    """Generate a valid CPF number formatted as ``000.000.000-00``."""
    c = cpf()
    return f"{c[:3]}.{c[3:6]}.{c[6:9]}-{c[9:]}"


def cnpj_with_punctuation(alphanumeric: bool = False) -> str:
    """Generate a valid CNPJ number formatted as ``00.000.000/0000-00``."""
    c = cnpj(alphanumeric=alphanumeric)
    return f"{c[:2]}.{c[2:5]}.{c[5:8]}/{c[8:12]}-{c[12:]}"
