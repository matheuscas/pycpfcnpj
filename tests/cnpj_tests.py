import unittest
from pycpfcnpj import cnpj


class CNPJTests(unittest.TestCase):
    """docstring for CNPJTests"""
    def setUp(self):
        self.valid_cnpj = '11444777000161'
        self.invalid_cnpj = '11444777000162'

    def test_validate_cnpj_true(self):
        self.assertTrue(cnpj.validate(self.valid_cnpj))

    def test_validate_cnpj_false(self):
        self.assertFalse(cnpj.validate(self.invalid_cnpj))
        for i in range(10):
            self.assertFalse(cnpj.validate(
                '{0}'.format(i) * 14
            ))

if __name__ == '__main__':
    unittest.main(verbosity=2)
