import string
import random
from . import cpf as cpf_module
from . import cnpj as cnpj_module


def cpf():
    cpf_ramdom = ''.join(random.choice(string.digits) for i in range(11))
    while not cpf_module.validate(cpf_ramdom):
        cpf_ramdom = ''.join(random.choice(string.digits) for i in range(11))
    return cpf_ramdom


def cnpj():
    cnpj_ramdom = ''.join(random.choice(string.digits) for i in range(14))
    while not cnpj_module.validate(cnpj_ramdom):
        cnpj_ramdom = ''.join(random.choice(string.digits) for i in range(14))
    return cnpj_ramdom


def cpf_with_punctuation():
	cpf_ramdom = cpf()
	return '{}.{}.{}-{}'.format(cpf_ramdom[:3], cpf_ramdom[3:6], cpf_ramdom[6:9], cpf_ramdom[9:])


def cnpj_with_punctuation():
	cnpj_ramdom = cnpj()
	return '{}.{}.{}/{}-{}'.format(cnpj_ramdom[:2], cnpj_ramdom[2:5], cnpj_ramdom[5:8], cnpj_ramdom[8:12], cnpj_ramdom[12:])