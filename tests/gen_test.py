import pytest
from pycpfcnpj import gen, cpf, cnpj


"""docstring for GenerateCPFTest"""


@pytest.fixture
def masked_valid_cpf():
    return gen.cpf_with_punctuation()


def test_validate_masked_cnpj_true(masked_valid_cpf):
    assert cpf.validate(masked_valid_cpf) == True


def test_valif_cpf_without_mask_true(masked_valid_cpf):
    cpf_result = (masked_valid_cpf.replace(".", "")).replace("-", "")
    assert cpf.validate(cpf_result) == True


"""docstring for GenerateCNPJTest"""


@pytest.fixture
def masked_valid_cnpj():
    return gen.cnpj_with_punctuation()


def test_validate_masked_cnpj_true(masked_valid_cnpj):
    assert cnpj.validate(masked_valid_cnpj) == True


def test_valid_cnpj_without_mask_true(masked_valid_cnpj):
    cnpj_result = (masked_valid_cnpj.replace(".", "")).replace("-", "")
    assert cnpj.validate(cnpj_result) == True
