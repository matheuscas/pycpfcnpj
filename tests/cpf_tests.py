import pytest
from pycpfcnpj import cpf

"""docstring for CPFTests"""


@pytest.fixture
def valid_cpf():
    return "11144477735"


@pytest.fixture
def masked_valid_cpf():
    return "111.444.777-35"


@pytest.fixture
def invalid_cpf():
    return "11144477736"


@pytest.fixture
def masked_invalid_cpf():
    return "111.444.777-36"


@pytest.fixture
def invalid_cpf_whitespaces():
    return "111444 77735"


@pytest.fixture
def invalid_cpf_with_alphabetic():
    return "111444A77735"


def test_validate_cpf_true(valid_cpf):
    assert cpf.validate(valid_cpf) == True


def test_validate_masked_cpf_true(masked_valid_cpf):
    assert cpf.validate(masked_valid_cpf) == True


def test_validate_cpf_false(invalid_cpf):
    assert cpf.validate(invalid_cpf) == False


def test_validate_masked_cpf_false(masked_invalid_cpf):
    assert cpf.validate(masked_invalid_cpf) == False


def test_validate_cpf_with_same_numbers():
    for i in range(10):
        assert cpf.validate("{0}".format(i) * 11) == False


def test_validate_cpf_unicode_true():
    assert cpf.validate(u"11144477735") == True


def test_validate_cpf_unicode_false():
    assert cpf.validate(u"11144477736") == False


def test_validate_masked_unicode_cpf_true():
    assert cpf.validate(u"111.444.777-35") == True


def test_validate_masked_unicode_cpf_false():
    assert cpf.validate(u"111.444.777-38") == False


def test_validate_cpf_with_whitespaces(invalid_cpf_whitespaces):
    assert cpf.validate(invalid_cpf_whitespaces) == False


def test_validate_cpf_with_alphabetic_characters(invalid_cpf_with_alphabetic):
    assert cpf.validate(invalid_cpf_with_alphabetic) == False
