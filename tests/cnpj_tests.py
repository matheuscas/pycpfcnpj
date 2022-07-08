import pytest
from pycpfcnpj import cnpj


"""docstring for CNPJTests"""


@pytest.fixture
def valid_cnpj():
    return "11444777000161"


@pytest.fixture
def masked_valid_cnpj():
    return "11.444.777/0001-61"


@pytest.fixture
def invalid_cnpj():
    return "11444777000162"


@pytest.fixture
def masked_invalid_cnpj():
    return "11.444.777/0001-62"


@pytest.fixture
def invalid_cnpj_whitespaces():
    return "11444 777000161"


@pytest.fixture
def invalid_cnpj_with_alphabetic():
    return "11444d777000161"


def test_validate_cnpj_true(valid_cnpj):
    assert cnpj.validate(valid_cnpj) == True


def test_validate_masked_cnpj_true(masked_valid_cnpj):
    assert cnpj.validate(masked_valid_cnpj) == True


def test_validate_cnpj_false(invalid_cnpj):
    assert cnpj.validate(invalid_cnpj) == False


def test_validate_masked_cnpj_false(invalid_cnpj):
    assert cnpj.validate(invalid_cnpj) == False


def test_validate_cnpj_with_same_numbers():
    for i in range(10):
        assert cnpj.validate("{0}".format(i) * 14) == False


def test_validate_cnpj_with_whitespaces(invalid_cnpj_whitespaces):
    assert cnpj.validate(invalid_cnpj_whitespaces) == False


def test_validate_cnpj_with_alphabetic_characters(invalid_cnpj_with_alphabetic):
    assert cnpj.validate(invalid_cnpj_with_alphabetic) == False
