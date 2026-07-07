"""Optimized pure-Python validation core.

This is the fallback used when the compiled ``_speedups`` extension is not
available for the current platform. It is a drop-in behavioural match for the
native implementation, but avoids redundant work (double ``.upper()``, per-digit
re-conversion, ``set()`` allocation, repeated punctuation stripping).

It is the single source of truth for the Python side: :mod:`pycpfcnpj.gen`
reuses :data:`CPF_W1`/:data:`CNPJ_W1`/... and :func:`_check_digit` from here
rather than keeping its own copy of the algorithm.
"""

from __future__ import annotations

from collections.abc import Sequence

CPF_W1 = (10, 9, 8, 7, 6, 5, 4, 3, 2)
CPF_W2 = (11, 10, 9, 8, 7, 6, 5, 4, 3, 2)
CNPJ_W1 = (5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2)
CNPJ_W2 = (6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2)

_PUNCT: dict[int, int | None] = str.maketrans("", "", ".-/")


def _check_digit(vals: Sequence[int], weights: Sequence[int]) -> int:
    total = 0
    for v, w in zip(vals, weights):
        total += v * w
    rest = total % 11
    return 0 if rest < 2 else 11 - rest


def _valid_cpf(s: str) -> bool:
    """Validate an already-punctuation-stripped CPF string."""
    if len(s) != 11 or not s.isdigit() or s == s[0] * 11:
        return False
    vals = [ord(c) - 48 for c in s]
    if vals[9] != _check_digit(vals, CPF_W1):
        return False
    return vals[10] == _check_digit(vals, CPF_W2)


def _valid_cnpj(s: str) -> bool:
    """Validate an already-punctuation-stripped CNPJ string (classic numeric or
    2026 alphanumeric format)."""
    s = s.upper()
    if len(s) != 14 or s == s[0] * 14:
        return False
    # The two check digits must always be numeric, even in the alphanumeric format.
    if not (s[12].isdigit() and s[13].isdigit()):
        return False
    vals: list[int] = []
    for c in s:
        if "0" <= c <= "9" or "A" <= c <= "Z":
            vals.append(ord(c) - 48)
        else:
            return False
    if vals[12] != _check_digit(vals, CNPJ_W1):
        return False
    return vals[13] == _check_digit(vals, CNPJ_W2)


def validate_cpf(cpf_number: str) -> bool:
    """Validate a CPF number (digits only, optional ``.``/``-`` punctuation)."""
    return _valid_cpf(cpf_number.translate(_PUNCT))


def validate_cnpj(cnpj_number: str) -> bool:
    """Validate a CNPJ number, both the classic numeric and the 2026
    alphanumeric formats (optional ``.``/``-``/``/`` punctuation)."""
    return _valid_cnpj(cnpj_number.translate(_PUNCT))


def validate(number: str) -> bool:
    """Facade: dispatch to CPF (cleaned length 11) or CNPJ (14).

    Punctuation is stripped once here and the already-clean string is handed to
    the internal validators, so there is no redundant re-cleaning.
    """
    s = number.translate(_PUNCT)
    n = len(s)
    if n == 11:
        return _valid_cpf(s)
    if n == 14:
        return _valid_cnpj(s)
    return False
