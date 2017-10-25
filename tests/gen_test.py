import unittest
from pycpfcnpj import gen, cpf, cnpj

class GenerateCPFTest(unittest.TestCase):
	"""docstring for GenerateCPFTest"""
	def setUp(self):
		self.masked_valid_cpf = gen.cpf_with_punctuation()

	def test_validate_masked_cnpj_true(self):
		self.assertTrue(cpf.validate(self.masked_valid_cpf))

	def test_valif_cpf_without_mask_true(self):
		cpf_result =(self.masked_valid_cpf.replace(".","")).replace("-","")
		self.assertTrue(cpf.validate(cpf_result))


class GenerateCNPJTest(unittest.TestCase):
	"""docstring for GenerateCNPJTest"""
	def setUp(self):
		self.masked_valid_cnpj = gen.cnpj_with_punctuation()

	def test_validate_masked_cnpj_true(self):
		self.assertTrue(cnpj.validate(self.masked_valid_cnpj))

	def test_valid_cnpj_without_mask_true(self):
		cnpj_result =(self.masked_valid_cnpj.replace(".","")).replace("-","")
		self.assertTrue(cnpj.validate(cnpj_result))