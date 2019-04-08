def cpf_mask(value):
    return '{}.{}.{}-{}'.format(value[:3], value[3:6], value[6:9], value[9:])


def cnpj_mask(value):
    return '{}.{}.{}/{}-{}'.format(value[:2], value[2:5], value[5:8],
                                   value[8:12], value[12:])
