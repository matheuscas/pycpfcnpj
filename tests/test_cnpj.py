import unittest

from pycpfcnpj import cnpj


class CNPJTests(unittest.TestCase):
    """docstring for CNPJTests"""

    def setUp(self):
        self.valid_cnpj = "11444777000161"
        self.masked_valid_cnpj = "11.444.777/0001-61"
        self.invalid_cnpj = "11444777000162"
        self.masked_invalid_cnpj = "11.444.777/0001-62"
        self.invalid_cnpj_whitespaces = "11444 777000161"
        self.invalid_cnpj_with_alphabetic = "11444d777000161"
        self.invalid_cnpj_with_special_character = "+5575999769162"

        self.valid_alphanumeric_cnpj = "12ABC34501DE35"
        self.invalid_alphanumeric_dv = "12ABC34501DE36"
        self.invalid_letters_in_verifier = ["12ABC34501DEA5", "12ABC34501DE3A",]
        self.invalid_alphanumeric_characters = ["12ABC34501DE@5", "12ABC34501DE 5",]
        self.invalid_alphanumeric_length = ["12ABC34501DE3", "12ABC34501DE350",]

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
            self.assertFalse(cnpj.validate("{0}".format(i) * 14))

    def test_validate_cnpj_with_whitespaces(self):
        self.assertFalse(cnpj.validate(self.invalid_cnpj_whitespaces))

    def test_validate_cnpj_with_alphabetic_characters(self):
        self.assertFalse(cnpj.validate(self.invalid_cnpj_with_alphabetic))

    def test_validate_cnpj_with_special_characters(self):
        self.assertFalse(cnpj.validate(self.invalid_cnpj_with_special_character))

    def test_validate_alphanumeric_cnpj_true(self):
        self.assertTrue(cnpj.validate(self.valid_alphanumeric_cnpj))

    def test_validate_alphanumeric_invalid_dv(self):
        self.assertFalse(cnpj.validate(self.invalid_alphanumeric_dv))

    def test_validate_alphanumeric_letters_in_verifier(self):
        for cnpj_number in self.invalid_letters_in_verifier:
            self.assertFalse(cnpj.validate(cnpj_number))

    def test_validate_alphanumeric_invalid_characters(self):
        for cnpj_number in self.invalid_alphanumeric_characters:
            self.assertFalse(cnpj.validate(cnpj_number))

    def test_validate_alphanumeric_invalid_length(self):
        for cnpj_number in self.invalid_alphanumeric_length:
            self.assertFalse(cnpj.validate(cnpj_number))
