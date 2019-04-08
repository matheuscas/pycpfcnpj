import random
import string

from . import calculation as calc
from .mask import cpf_mask, cnpj_mask


def cpf():
    cpf_ramdom = ''.join(random.choice(string.digits) for i in range(9))
    cpf_ramdom += calc.calculate_first_digit(cpf_ramdom)
    cpf_ramdom += calc.calculate_second_digit(cpf_ramdom)
    return cpf_ramdom


def cnpj():
    cnpj_ramdom = ''.join(random.choice(string.digits) for i in range(12))
    cnpj_ramdom += calc.calculate_first_digit(cnpj_ramdom)
    cnpj_ramdom += calc.calculate_second_digit(cnpj_ramdom)
    return cnpj_ramdom


def cpf_with_punctuation():
    cpf_ramdom = cpf()

    return cpf_mask(cpf_ramdom)


def cnpj_with_punctuation():
    cnpj_ramdom = cnpj()

    return cnpj_mask(cnpj_ramdom)
