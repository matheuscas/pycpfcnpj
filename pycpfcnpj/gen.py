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
