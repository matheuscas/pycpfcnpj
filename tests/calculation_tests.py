import pytest
import pycpfcnpj.calculation as calc


@pytest.fixture
def first_part_cpf_number():
    return '111444777'


@pytest.fixture
def first_part_cnpj_number():
    return '114447770001'

# TESTS FOR CPF DIGITS


def test_cpf_calculate_first_digit_true(first_part_cpf_number):
    correct_first_digit = '3'
    assert correct_first_digit == calc.calculate_first_digit(
        first_part_cpf_number)


def test_cpf_calculate_first_digit_false(first_part_cpf_number):
    incorrect_first_digit = '6'
    assert incorrect_first_digit != calc.calculate_first_digit(
        first_part_cpf_number)


def test_cpf_calculate_second_digit_true(first_part_cpf_number):
    updated_cpf_number = first_part_cpf_number + \
        calc.calculate_first_digit(
            first_part_cpf_number)
    correct_second_digit = '5'
    assert correct_second_digit == calc.calculate_second_digit(
        updated_cpf_number)


def test_cpf_calculate_second_digit_false(first_part_cpf_number):
    updated_cpf_number = first_part_cpf_number + \
        calc.calculate_first_digit(
            first_part_cpf_number)
    incorrect_second_digit = '7'
    assert incorrect_second_digit != calc.calculate_second_digit(
        updated_cpf_number)

# TESTS FOR CNPJ DIGITS


def test_cnpj_calculate_first_digit_true(first_part_cnpj_number):
    correct_first_digit = '6'
    assert correct_first_digit == calc.calculate_first_digit(
        first_part_cnpj_number)


def test_cnpj_calculate_first_digit_false(first_part_cnpj_number):
    correct_first_digit = '7'
    assert correct_first_digit != calc.calculate_first_digit(
        first_part_cnpj_number)


def test_cnpj_calculate_second_digit_true(first_part_cnpj_number):
    correct_second_digit = '1'
    updated_cnpj_number = first_part_cnpj_number + \
        calc.calculate_first_digit(
            first_part_cnpj_number)
    assert correct_second_digit == calc.calculate_second_digit(
        updated_cnpj_number)


def test_cnpj_calculate_second_digit_false(first_part_cnpj_number):
    correct_second_digit = '2'
    updated_cnpj_number = first_part_cnpj_number + \
        calc.calculate_first_digit(
            first_part_cnpj_number)
    assert correct_second_digit != calc.calculate_second_digit(
        updated_cnpj_number)
