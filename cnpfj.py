import pycnpfj.cpf as cpf
import pycnpfj.cnpj as cnpj

def validate(number):
	"""Validation function for cpf and cnpj brazilian numbers
	   'number' must be a string containing only numbers
	"""
	if len(number) == 11:
		return cpf.validate(number)
	elif len(number) == 14:
		return cnpj.validate(number)
	return False