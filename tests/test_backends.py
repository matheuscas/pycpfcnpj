"""Exercise both validation backends (pure-Python ``_core`` and the compiled
Rust ``_speedups``) in a single test run.

The parametrized battery asserts each backend's behaviour on known edge cases;
the differential fuzz asserts the two backends agree on random inputs, so the
native and fallback paths can never silently diverge.
"""

import random
import string

import pytest
from pycpfcnpj import _core, gen

BACKENDS = [pytest.param(_core, id="python")]
try:
    from pycpfcnpj import _speedups

    BACKENDS.append(pytest.param(_speedups, id="rust"))
    HAS_RUST = True
except ImportError:  # pragma: no cover - only on platforms without a wheel
    _speedups = None
    HAS_RUST = False


@pytest.fixture(params=BACKENDS)
def backend(request):
    return request.param


VALID_CPF = ["11144477735", "111.444.777-35"]
INVALID_CPF = [
    "11144477736",  # wrong check digit
    "111.444.777-36",
    "111444777",  # too short
    "111444A77735",  # letter
    "*55759997&9",  # special chars
    "111444 77735",  # whitespace
]

VALID_CNPJ = [
    "11444777000161",
    "11.444.777/0001-61",
    "12ABC34501DE35",  # 2026 alphanumeric
    "12abc34501de35",  # lowercase normalizes
]
INVALID_CNPJ = [
    "11444777000162",  # wrong check digit
    "12ABC34501DE36",  # wrong alphanumeric dv
    "12ABC34501DEA5",  # letter in verifier
    "12ABC34501DE@5",  # special char
    "12ABC34501DE3",  # too short
    "11444d777000161",  # letter makes it 15 chars
    "11444 777000161",  # whitespace
]


@pytest.mark.parametrize("value", VALID_CPF)
def test_cpf_valid(backend, value):
    assert backend.validate_cpf(value)
    assert backend.validate(value)


@pytest.mark.parametrize("value", INVALID_CPF)
def test_cpf_invalid(backend, value):
    assert not backend.validate_cpf(value)


def test_cpf_all_same_digits(backend):
    for i in range(10):
        assert not backend.validate_cpf(str(i) * 11)


@pytest.mark.parametrize("value", VALID_CNPJ)
def test_cnpj_valid(backend, value):
    assert backend.validate_cnpj(value)
    assert backend.validate(value)


@pytest.mark.parametrize("value", INVALID_CNPJ)
def test_cnpj_invalid(backend, value):
    assert not backend.validate_cnpj(value)


def test_cnpj_all_same_digits(backend):
    for i in range(10):
        assert not backend.validate_cnpj(str(i) * 14)


def test_facade_dispatch(backend):
    assert backend.validate("11144477735")  # cpf
    assert backend.validate("11444777000161")  # cnpj
    assert not backend.validate("111444777")  # neither length
    assert not backend.validate("")


@pytest.mark.skipif(not HAS_RUST, reason="native _speedups extension not built")
def test_native_matches_pure_fuzz():
    random.seed(20260706)
    alphabet = string.ascii_letters + string.digits + "./-"
    samples = []
    for _ in range(5000):
        samples += [
            gen.cpf(),
            gen.cnpj(),
            gen.cnpj(alphanumeric=True),
            gen.cpf_with_punctuation(),
            gen.cnpj_with_punctuation(),
            gen.cnpj_with_punctuation(alphanumeric=True),
        ]
    for _ in range(20000):
        length = random.choice([9, 10, 11, 12, 13, 14, 15])
        samples.append("".join(random.choice(alphabet) for _ in range(length)))
    samples += ["1" * 11, "0" * 14, "12ABC34501DE35", "12ABC34501DEA5", ""]

    for s in samples:
        assert _core.validate(s) == _speedups.validate(s), s
        assert _core.validate_cpf(s) == _speedups.validate_cpf(s), s
        assert _core.validate_cnpj(s) == _speedups.validate_cnpj(s), s
