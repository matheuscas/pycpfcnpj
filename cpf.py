import pycnpfj.calculation as calculation

def validate(cpf_number):
	first_cpf_weighs = [10,9,8,7,6,5,4,3,2]
	second_cpf_weighs = [11,10,9,8,7,6,5,4,3,2]
	first_part = cpf_number[:9]
	first_digit = cpf_number[9]
	second_digit = cpf_number[10]

	if first_digit == calculation.first_check_digit(first_part, first_cpf_weighs) and \
		second_digit == calculation.second_check_digit(cpf_number[:10],second_cpf_weighs):
		return True

	return False