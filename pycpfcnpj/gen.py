import string
import random
from . import cpf as cpf_module
from . import cnpj as cnpj_module


def put_mask(number, mask):
    new_number = ''

    first = 0
    for last, signal in mask:
        new_number += number[first:last] + signal
        first = last

    return new_number + number[last:]


def cpf(mask=False):
    cpf_ramdom = ''.join(random.choice(string.digits) for i in range(11))
    while not cpf_module.validate(cpf_ramdom):
        cpf_ramdom = ''.join(random.choice(string.digits) for i in range(11))

    if mask:
        return put_mask(cpf_ramdom, ((3, '.'), (6, '.'), (9, '-')))

    return cpf_ramdom


def cnpj(mask=False):
    cnpj_ramdom = ''.join(random.choice(string.digits) for i in range(14))
    while not cnpj_module.validate(cnpj_ramdom):
        cnpj_ramdom = ''.join(random.choice(string.digits) for i in range(14))

    if mask:
        return put_mask(cnpj_ramdom, ((2, '.'), (5, '.'), (8,'/'), (12, '-')))

    return cnpj_ramdom
