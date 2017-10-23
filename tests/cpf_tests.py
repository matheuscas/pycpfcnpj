import unittest

from pycpfcnpj import cpf
from pycpfcnpj.gen import cpf as gen_cpf
from pycpfcnpj.gen import put_mask


class CPFTests(unittest.TestCase):
    """docstring for CPFTests"""

    def setUp(self):
        self.valid_cpf = '11144477735'
        self.masked_valid_cpf = '111.444.777-35'
        self.invalid_cpf = '11144477736'
        self.masked_invalid_cpf = '111.444.777-36'

    def test_validate_cpf_true(self):
        self.assertTrue(cpf.validate(self.valid_cpf))

    def test_validate_masked_cpf_true(self):
        self.assertTrue(cpf.validate(self.masked_valid_cpf))

    def test_validate_cpf_false(self):
        self.assertFalse(cpf.validate(self.invalid_cpf))

    def test_validate_masked_cpf_false(self):
        self.assertFalse(cpf.validate(self.masked_invalid_cpf))

    def test_validate_cpf_with_same_numbers(self):
        for i in range(10):
            self.assertFalse(cpf.validate(
                '{0}'.format(i) * 11
            ))

    def test_put_mask_cpf(self):
        with_mask = put_mask(self.valid_cpf, ((3, '.'), (6, '.'), (9, '-')))
        self.assertEqual(with_mask, self.masked_valid_cpf)

    def test_gen_cpf_with_default_mask_tag(self):
        cpf = gen_cpf()
        self.assertEqual(len(cpf), 11)
        self.assertTrue(cpf.isdigit())

    def test_gen_cpf_with_mask(self):
        cpf = gen_cpf(mask=True)
        self.assertEqual(len(cpf), 14)
        self.assertFalse(cpf.isdigit())


if __name__ == '__main__':
    unittest.main(verbosity=2)
