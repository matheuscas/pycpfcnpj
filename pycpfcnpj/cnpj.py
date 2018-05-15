from . import calculation as calc
from . import compatible as compat


def validate(cnpj_number):
    """This function validates a CNPJ number.

    This function uses calculation package to calculate both digits
    and then validates the number.

    :param cnpj_number: a CNPJ number to be validated.  Only numbers.
    :type cnpj_number: string
    :return: Bool -- True for a valid number, False otherwise.

    """

    _cnpj = compat.clear_punctuation(cnpj_number)

    if (len(_cnpj) != 14 or
       len(set(_cnpj)) == 1):
        return False

    first_part = _cnpj[:12]
    second_part = _cnpj[:13]
    first_digit = _cnpj[12]
    second_digit = _cnpj[13]

    if (first_digit == calc.calculate_first_digit(first_part) and
       second_digit == calc.calculate_second_digit(second_part)):
        return True

    return False
