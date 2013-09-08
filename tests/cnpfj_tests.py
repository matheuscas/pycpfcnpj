import sys
#sys.path.insert(0,'..')
import unittest
import pycnpfj.cnpfj as cnpfj

class CNPFJTests(unittest.TestCase):
	"""docstring for CNPFJTests"""
	def setUp(self):
		self.valid_cpf = '11144477735'
		self.invalid_cpf = '11144477736'
		self.invalid_cpf_size = '111444777'
		self.valid_cnpj = '11444777000161'
		self.invalid_cnpj = '11444777000162'
		self.invalid_cnpj_size = '114447770001'

	def test_validate_cpf_true(self):
		self.assertTrue(cnpfj.validate(self.valid_cpf))

	def test_validate_cpf_false(self):
		self.assertFalse(cnpfj.validate(self.invalid_cpf))

	def test_validate_cnpj_true(self):
		self.assertTrue(cnpfj.validate(self.valid_cnpj))

	def test_validate_cnpj_false(self):
		self.assertFalse(cnpfj.validate(self.invalid_cnpj))

	def test_wrong_cpf_size(self):
		self.assertFalse(cnpfj.validate(self.invalid_cpf_size))

	def test_wrong_cnpj_size(self):
		self.assertFalse(cnpfj.validate(self.invalid_cnpj_size))


if __name__ == '__main__':
    unittest.main(verbosity=2)
