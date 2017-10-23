import unittest

from pycpfcnpj import cnpj
from pycpfcnpj.gen import cnpj as gen_cnpj
from pycpfcnpj.gen import put_mask


class CNPJTests(unittest.TestCase):
    """docstring for CNPJTests"""
    def setUp(self):
        self.valid_cnpj = '11444777000161'
        self.masked_valid_cnpj = '11.444.777/0001-61'
        self.invalid_cnpj = '11444777000162'
        self.masked_invalid_cnpj = '11.444.777/0001-62'

    def test_validate_cnpj_true(self):
        self.assertTrue(cnpj.validate(self.valid_cnpj))

    def test_validate_masked_cnpj_true(self):
        self.assertTrue(cnpj.validate(self.masked_valid_cnpj))

    def test_validate_cnpj_false(self):
        self.assertFalse(cnpj.validate(self.invalid_cnpj))

    def test_validate_masked_cnpj_false(self):
        self.assertFalse(cnpj.validate(self.invalid_cnpj))

    def test_validate_cnpj_with_same_numbers(self):
        for i in range(10):
            self.assertFalse(cnpj.validate(
                '{0}'.format(i) * 14
            ))

    def test_put_mask_cnpj(self):
        with_mask = put_mask(
            self.valid_cnpj,
            ((2, '.'), (5, '.'), (8,'/'), (12, '-'))
        )
        self.assertEqual(with_mask, self.masked_valid_cnpj)

    def test_gen_cnpf_with_default_mask_tag(self):
        cnpj = gen_cnpj()
        self.assertEqual(len(cnpj), 14)
        self.assertTrue(cnpj.isdigit())

    def test_gen_cnpj_with_mask(self):
        cnpj = gen_cnpj(mask=True)
        self.assertEqual(len(cnpj), 18)
        self.assertFalse(cnpj.isdigit())


if __name__ == '__main__':
    unittest.main(verbosity=2)
