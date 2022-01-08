import unittest
from pycpfcnpj import cpf, cnpj, mask


class FORMATTests(unittest.TestCase):
    """docstring for CPFTests"""

    def setUp(self):
        self.valid_cpf = '11144477735'
        self.invalid_cpf = '11144477736'
        self.invalid_cpf_str = '1234'
        self.valid_cnpj = '11444777000161'
        self.invalid_cnpj = '11444777000162'
        self.invalid_cnpj_str = '1234'

    def test_mask_valid_cpf(self):
        self.assertTrue(cpf.validate(mask.mask_cpf_cnpj(self.valid_cpf)))

    def test_mask_invalid_cpf(self):
        self.assertFalse(cpf.validate(mask.mask_cpf_cnpj(self.invalid_cpf)))

    def test_mask_invalid_cpf_str(self):
        self.assertTrue(mask.mask_cpf_cnpj(self.invalid_cpf_str) == '1234')

    def test_mask_valid_cnpj(self):
        self.assertTrue(cnpj.validate(mask.mask_cpf_cnpj(self.valid_cnpj)))

    def test_mask_invalid_cnpj(self):
        self.assertFalse(cnpj.validate(mask.mask_cpf_cnpj(self.invalid_cnpj)))

    def test_mask_invalid_cnpj_str(self):
        self.assertTrue(mask.mask_cpf_cnpj(self.invalid_cnpj_str) == '1234')


if __name__ == '__main__':
    unittest.main(verbosity=2)
