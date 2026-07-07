from ._backend import validate_cpf


def validate(cpf_number: str) -> bool:
    """This function validates a CPF number.

    Delegates to the active backend (compiled Rust extension when available,
    optimized pure-Python otherwise). Accepts numbers with or without the
    ``.``/``-`` punctuation.

    :param cpf_number: a CPF number to be validated.
    :type cpf_number: string
    :return: Bool -- True for a valid number, False otherwise.

    """
    return validate_cpf(cpf_number)
