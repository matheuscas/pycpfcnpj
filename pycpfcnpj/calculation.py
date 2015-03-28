DIVISOR = 11


def first_check_digit(number, weighs):
    """ This function calculates the first check digit to
        verify a cpf or cnpj vality.

        :param number: cpf or cnpj number to check the first
                       digit.  Only numbers.
        :type number: string
        :param weighs: weighs related to first check digit
                       calculation
        :type weighs: list of integers
        :returns: string -- the first digit

    """

    sum = 0
    for i in range(len(weighs)):
        sum = sum + int(number[i]) * weighs[i]
    rest_division = sum % DIVISOR
    if rest_division < 2:
        return '0'
    return str(11 - rest_division)


def second_check_digit(updated_number, weighs):
    """ This function calculates the second check digit to
        verify a cpf or cnpj vality.

        **This function must be called after the above.**

        :param updated_number: cpf or cnpj number with the
                               first digit.  Only numbers.
        :type number: string
        :param weighs: weighs related to second check digit calculation
        :type weighs: list of integers
        :returns: string -- the second digit

    """

    sum = 0
    for i in range(len(weighs)):
        sum = sum + int(updated_number[i]) * weighs[i]
    rest_division = sum % DIVISOR
    if rest_division < 2:
        return '0'
    return str(11 - rest_division)
