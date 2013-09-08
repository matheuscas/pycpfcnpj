DIVISOR = 11

def first_check_digit(number,weighs):
	sum = 0
	for i in range(len(weighs)):
		sum = sum + int(number[i]) * weighs[i]
	rest_division = sum % DIVISOR
	if rest_division < 2:
		return '0'
	return str(11 - rest_division)

def second_check_digit(updated_number, weighs):
	sum = 0
	for i in range(len(weighs)):
		sum = sum + int(updated_number[i]) * weighs[i]
	rest_division = sum % DIVISOR
	if rest_division < 2:
		return '0'
	return str(11 - rest_division)
