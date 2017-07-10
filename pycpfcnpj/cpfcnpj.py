from .compatible import clear_punctuation

from . import cpf
from . import cnpj


def validate(number):
    """This functions acts like a Facade to the other modules cpf and cnpj
       and validates either CPF and CNPJ numbers.
       Feel free to use this or the other modules directly.

       :param number: a CPF or CNPJ number. Clear number to have only numbers.
       :type number: string
       :return: Bool -- True if number is a valid CPF or CNPJ number.
                False if it is not or do not complain
                with the right size of these numbers.

    """
    clean_number = clear_punctuation(number)

    if len(clean_number) == 11:
        return cpf.validate(clean_number)
    elif len(clean_number) == 14:
        return cnpj.validate(clean_number)
    return False
