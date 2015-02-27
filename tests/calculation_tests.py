import sys
import unittest

if sys.version[0] == '2':
	from pycpfcnpj import calculation as calc
else:
	import os
	import inspect
	currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
	parentdir = os.path.dirname(currentdir)
	sys.path.insert(0,parentdir)
	import pycpfcnpj.calculation as calc


class CalculationTests(unittest.TestCase):

    """docstring for CalculationTests"""

    def setUp(self):
        self.first_part_cpf_number = '111444777'
        self.first_part_cnpj_number = '114447770001'
        self.first_cpf_weighs = [10, 9, 8, 7, 6, 5, 4, 3, 2]
        self.second_cpf_weighs = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
        self.first_cnpj_weighs = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        self.second_cnpj_weighs = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    # TESTS FOR CPF DIGITS
    def test_cpf_first_check_digit_true(self):
        correct_first_digit = '3'
        self.assertEqual(correct_first_digit,
                         calc.first_check_digit(self.first_part_cpf_number, self.first_cpf_weighs))

    def test_cpf_first_check_digit_false(self):
        incorrect_first_digit = '6'
        self.assertNotEqual(incorrect_first_digit,
                            calc.first_check_digit(self.first_part_cpf_number, self.first_cpf_weighs))

    def test_cpf_second_check_digit_true(self):
        updated_cpf_number = self.first_part_cpf_number + \
            calc.first_check_digit(
                self.first_part_cpf_number, self.first_cpf_weighs)
        correct_second_digit = '5'
        self.assertEqual(correct_second_digit,
                         calc.second_check_digit(updated_cpf_number, self.second_cpf_weighs))

    def test_cpf_second_check_digit_false(self):
        updated_cpf_number = self.first_part_cpf_number + \
            calc.first_check_digit(
                self.first_part_cpf_number, self.first_cpf_weighs)
        incorrect_second_digit = '7'
        self.assertNotEqual(incorrect_second_digit,
                            calc.second_check_digit(updated_cpf_number, self.second_cpf_weighs))

    # TESTS FOR CNPJ DIGITS
    def test_cnpj_first_check_digit_true(self):
        correct_first_digit = '6'
        self.assertEqual(correct_first_digit,
                         calc.first_check_digit(self.first_part_cnpj_number, self.first_cnpj_weighs))

    def test_cnpj_first_check_digit_false(self):
        correct_first_digit = '7'
        self.assertNotEqual(correct_first_digit,
                            calc.first_check_digit(self.first_part_cnpj_number, self.first_cnpj_weighs))

    def test_cnpj_second_check_digit_true(self):
        correct_second_digit = '1'
        updated_cnpj_number = self.first_part_cnpj_number + \
            calc.first_check_digit(
                self.first_part_cnpj_number, self.first_cnpj_weighs)
        self.assertEqual(correct_second_digit,
                         calc.second_check_digit(updated_cnpj_number, self.second_cnpj_weighs))

    def test_cnpj_second_check_digit_false(self):
        correct_second_digit = '2'
        updated_cnpj_number = self.first_part_cnpj_number + \
            calc.first_check_digit(
                self.first_part_cnpj_number, self.first_cnpj_weighs)
        self.assertNotEqual(correct_second_digit,
                            calc.second_check_digit(updated_cnpj_number, self.second_cnpj_weighs))


if __name__ == '__main__':
    unittest.main(verbosity=2)
