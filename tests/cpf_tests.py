import unittest
import pycpfcnpj.cpf as cpf


class CPFTests(unittest.TestCase):
	"""docstring for CPFTests"""

	def setUp(self):
		self.valid_cpf = '11144477735'
		self.invalid_cpf = '11144477736'

	def test_validate_cpf_true(self):
		self.assertTrue(cpf.validate(self.valid_cpf))

	def test_validate_cpf_false(self):
		self.assertFalse(cpf.validate(self.invalid_cpf))

if __name__ == '__main__':
    unittest.main(verbosity=2)
