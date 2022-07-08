from multiprocessing.sharedctypes import Value
import pytest
from pycpfcnpj import cpfcnpj


"""docstring for CPFCNPJTests"""


@pytest.fixture
def valid_cpf():
    return "11144477735"


@pytest.fixture
def invalid_cpf():
    return "11144477736"


@pytest.fixture
def invalid_cpf_size():
    return "111444777"


@pytest.fixture
def invalid_cpf_whitespaces():
    return "111444 77735"


@pytest.fixture
def valid_cnpj():
    return "11444777000161"


@pytest.fixture
def invalid_cnpj():
    return "11444777000162"


@pytest.fixture
def invalid_cnpj_size():
    return "114447770001"


@pytest.fixture
def invalid_cnpj_whitespaces():
    return "11444 777000161"


@pytest.fixture
def invalid_cpf_with_alphabetic():
    return "111444A77735"


@pytest.fixture
def invalid_cnpj_with_alphabetic():
    return "11444d777000161"


@pytest.fixture
def mascared_valid_cpf():
    return "111.444.777-35"


@pytest.fixture
def mascared_invalid_cpf():
    return "111.444.777-36"


@pytest.fixture
def mascared_invalid_cpf_size():
    return "111.444.777"


@pytest.fixture
def mascared_valid_cnpj():
    return "11.444.777/0001-61"


@pytest.fixture
def mascared_invalid_cnpj():
    return "11.444.777/0001-62"


@pytest.fixture
def mascared_invalid_cnpj_size():
    return "114.447/7700-01"


def test_validate_cpf_true(valid_cpf):
    assert cpfcnpj.validate(valid_cpf) == True


def test_validate_cpf_false(invalid_cpf):
    assert cpfcnpj.validate(invalid_cpf) == False


def test_validate_unicode_cpf_tru():
    assert cpfcnpj.validate(u"11144477735") == True


def test_validate_cnpj_true(valid_cnpj):
    assert cpfcnpj.validate(valid_cnpj) == True


def test_validate_cnpj_false(invalid_cnpj):
    assert cpfcnpj.validate(invalid_cnpj) == False


def test_validate_unicode_cnpj_true():
    assert cpfcnpj.validate(u"11444777000161") == True


def test_wrong_cpf_size(invalid_cpf_size):
    assert cpfcnpj.validate(invalid_cpf_size) == False


def test_wrong_cnpj_size(invalid_cnpj_size):
    assert cpfcnpj.validate(invalid_cnpj_size) == False


def mascared_test_validate_cpf_true(mascared_valid_cpf):
    assert cpfcnpj.validate(mascared_valid_cpf) == True


def mascared_test_validate_cpf_false(mascared_invalid_cpf):
    assert cpfcnpj.validate(mascared_invalid_cpf) == False


def mascared_test_validate_cnpj_true(mascared_valid_cnpj):
    assert cpfcnpj.validate(mascared_valid_cnpj) == True


def mascared_test_validate_cnpj_false(mascared_invalid_cnpj):
    assert cpfcnpj.validate(mascared_invalid_cnpj) == False


def mascared_test_wrong_cpf_size(mascared_invalid_cpf_size):
    assert cpfcnpj.validate(mascared_invalid_cpf_size) == False


def mascared_test_wrong_cnpj_size(mascared_invalid_cnpj_size):
    assert cpfcnpj.validate(mascared_invalid_cnpj_size) == False


def test_validate_cnpj_with_whitespace(invalid_cnpj_whitespaces):
    assert cpfcnpj.validate(invalid_cnpj_whitespaces) == False


def test_validate_cpf_with_whitespace(invalid_cpf_whitespaces):
    assert cpfcnpj.validate(invalid_cpf_whitespaces) == False


def test_validate_cnpj_with_alphabetic_characters(invalid_cnpj_with_alphabetic):
    assert cpfcnpj.validate(invalid_cnpj_with_alphabetic) == False


def test_validate_cpf_with_alphabetic_characters(invalid_cpf_with_alphabetic):
    assert cpfcnpj.validate(invalid_cpf_with_alphabetic) == False
