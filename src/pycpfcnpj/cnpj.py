from . import calculation as calc
from . import compatible as compat


@compat.check_special_characters
def validate(cnpj_number):
    """This function validates a CNPJ number.

    This function uses calculation package to calculate both digits
    and then validates the number. Supports both old format (numbers only)
    and new format (numbers and letters).

    :param cnpj_number: a CNPJ number to be validated. Can contain numbers and letters.
    :type cnpj_number: string
    :return: Bool -- True for a valid number, False otherwise.

    """

    _cnpj = compat.clear_punctuation(cnpj_number)

    if len(_cnpj) != 14 or len(set(_cnpj)) == 1:
        return False

    if not _cnpj[-2:].isdigit():
        return False

    first_part = _cnpj[:12]
    second_part = _cnpj[:13]
    first_digit = _cnpj[12]
    second_digit = _cnpj[13]

    if first_digit == calc.calculate_first_digit(
        first_part
    ) and second_digit == calc.calculate_second_digit(second_part):
        return True

    return False
