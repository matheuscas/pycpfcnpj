from ._backend import validate_cnpj


def validate(cnpj_number: str) -> bool:
    """This function validates a CNPJ number.

    Delegates to the active backend (compiled Rust extension when available,
    optimized pure-Python otherwise). Supports both the classic numeric format
    and the 2026 alphanumeric format, with or without punctuation.

    :param cnpj_number: a CNPJ number to be validated. Can contain numbers and letters.
    :type cnpj_number: string
    :return: Bool -- True for a valid number, False otherwise.

    """
    return validate_cnpj(cnpj_number)
