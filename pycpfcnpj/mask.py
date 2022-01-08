
from . import cpf
from . import cnpj


def mask_cpf_cnpj(cpf_cnpj: str):
    cpf_cnpj = "".join([x for x in f'{cpf_cnpj}'])

    if cpf.validate(cpf_cnpj):
        return f'{cpf_cnpj[:3]}.{cpf_cnpj[3:6]}.{cpf_cnpj[6:9]}-{cpf_cnpj[9:]}'
    elif cnpj.validate(cpf_cnpj):
        return f'{cpf_cnpj[:2]}.{cpf_cnpj[2:5]}.{cpf_cnpj[5:8]}/{cpf_cnpj[8:12]}-{cpf_cnpj[12:14]}'
    else:
        return cpf_cnpj
