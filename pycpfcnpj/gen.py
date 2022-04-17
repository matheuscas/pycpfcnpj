import string
import random
from . import calculation as calc
from . import cpf as cpf_module
from . import cnpj as cnpj_module


def cpf() -> str:
    cpf_ramdom: str = ''.join(random.choice(string.digits) for i in range(9))
    cpf_ramdom += calc.calculate_first_digit(cpf_ramdom)
    cpf_ramdom += calc.calculate_second_digit(cpf_ramdom)
    return cpf_ramdom


def cnpj() -> str:
    cnpj_ramdom: str = ''.join(random.choice(string.digits) for i in range(12))
    cnpj_ramdom += calc.calculate_first_digit(cnpj_ramdom)
    cnpj_ramdom += calc.calculate_second_digit(cnpj_ramdom)
    return cnpj_ramdom


def cpf_with_punctuation() -> str:
	cpf_ramdom: str = cpf()
	return '{}.{}.{}-{}'.format(cpf_ramdom[:3], cpf_ramdom[3:6], cpf_ramdom[6:9], cpf_ramdom[9:])


def cnpj_with_punctuation() -> str:
	cnpj_ramdom: str = cnpj()
	return '{}.{}.{}/{}-{}'.format(cnpj_ramdom[:2], cnpj_ramdom[2:5], cnpj_ramdom[5:8], cnpj_ramdom[8:12], cnpj_ramdom[12:])