import pycnpfj.calculation as calculation

def validate(cnpj_number):
	"""This function validates a CNPJ number.

	This function uses calculation package to calculate both digits
	and then validates the number.

	:param cnpj_number: a CNPJ number to be validated.  Only numbers.
	:type cnpj_number: string
	:return: Bool -- True for a valid number, False otherwise.

	"""

	first_cnpj_weighs = [5,4,3,2,9,8,7,6,5,4,3,2]
	second_cnpj_weighs = [6,5,4,3,2,9,8,7,6,5,4,3,2]
	first_part = cnpj_number[:12]
	first_digit = cnpj_number[12]
	second_digit = cnpj_number[13]

	if first_digit == calculation.first_check_digit(first_part, first_cnpj_weighs) and \
		second_digit == calculation.second_check_digit(cnpj_number[:13],second_cnpj_weighs):
		return True

	return False
