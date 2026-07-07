from ._backend import validate as _validate


def validate(number: str) -> bool:
    """This functions acts like a Facade to the other modules cpf and cnpj
    and validates either CPF and CNPJ numbers.
    Feel free to use this or the other modules directly.

    :param number: a CPF or CNPJ number. Clear number to have only numbers.
    :type number: string
    :return: Bool -- True if number is a valid CPF or CNPJ number.
             False if it is not or do not complain
             with the right size of these numbers.

    """
    return _validate(number)
