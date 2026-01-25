DIVISOR = 11

CPF_WEIGHTS = ((10, 9, 8, 7, 6, 5, 4, 3, 2),
              (11, 10, 9, 8, 7, 6, 5, 4, 3, 2))
CNPJ_WEIGHTS = ((5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2),
               (6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2))



def convert_alphanumeric_to_numeric_values(alphanumeric_string):
    """Converts alphanumeric characters to numeric values for CNPJ calculation.
    
    This function handles the new CNPJ format that includes letters and numbers.
    Letters are converted to numbers using ASCII value minus 48.
    is used to maintain compatibility with the existing weight system.
    
    :param alphanumeric_string: String containing numbers and letters
    :type alphanumeric_string: string
    :returns: list -- list of numeric values for calculation
    """
    result = []
    for char in alphanumeric_string.upper():
        if char.isdigit():
            result.append(int(char))
        elif char.isalpha():
            result.append(ord(char.upper()) - 48)
        else:
            raise ValueError(f"Invalid character '{char}' in CNPJ")
    return result


def calculate_first_digit(number):
    """ This function calculates the first check digit of a
        cpf or cnpj.

        :param number: cpf (length 9) or cnpj (length 12) 
            string to check the first digit. Can contain numbers and letters for new CNPJ format.
            For new CNPJ format: 8 positions (root) + 4 positions (establishment order) = 12 alphanumeric positions
        :type number: string
        :returns: string -- the first digit

    """
    # Convert alphanumeric to numeric values for calculation
    numeric_values = convert_alphanumeric_to_numeric_values(number)
    
    total = 0
    if len(numeric_values) == 9:
        weights = CPF_WEIGHTS[0]
    else:
        weights = CNPJ_WEIGHTS[0]

    for i in range(len(numeric_values)):
        total = total + numeric_values[i] * weights[i]
    rest_division = total % DIVISOR
    if rest_division < 2:
        return '0'
    return str(11 - rest_division)


def calculate_second_digit(number):
    """ This function calculates the second check digit of
        a cpf or cnpj.

        **This function must be called after the above.**

        :param number: cpf (length 10) or cnpj 
            (length 13) number with the first digit. Can contain numbers and letters for new CNPJ format.
            For new CNPJ format: 12 alphanumeric positions + 1 first digit = 13 positions
        :type number: string
        :returns: string -- the second digit

    """
    numeric_values = convert_alphanumeric_to_numeric_values(number)
    
    total = 0
    if len(numeric_values) == 10:
        weights = CPF_WEIGHTS[1]
    else:
        weights = CNPJ_WEIGHTS[1]

    for i in range(len(numeric_values)):
        total = total + numeric_values[i] * weights[i]
    rest_division = total % DIVISOR
    if rest_division < 2:
        return '0'
    return str(11 - rest_division)
