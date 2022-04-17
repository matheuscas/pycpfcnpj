from . import calculation as calc
from . import compatible as compat


def validate(cpf_number: str) -> bool:
    """This function validates a CPF number.

    This function uses calculation package to calculate both digits
    and then validates the number.

    :param cpf_number: a CPF number to be validated.  Only numbers.
    :type cpf_number: string
    :return: Bool -- True for a valid number, False otherwise.

    """

    _cpf: str = compat.clear_punctuation(cpf_number)

    if (len(_cpf) != 11 or
       len(set(_cpf)) == 1):
        return False

    first_part: str = _cpf[:9]
    second_part: str = _cpf[:10]
    first_digit: str = _cpf[9]
    second_digit: str = _cpf[10]

    if (first_digit == calc.calculate_first_digit(first_part) and
       second_digit == calc.calculate_second_digit(second_part)):
        return True

    return False
