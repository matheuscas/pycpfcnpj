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

    # TESTS FOR CPF DIGITS
    def test_cpf_calculate_first_digit_true(self):
        correct_first_digit = '3'
        self.assertEqual(correct_first_digit,
                         calc.calculate_first_digit(self.first_part_cpf_number))

    def test_cpf_calculate_first_digit_false(self):
        incorrect_first_digit = '6'
        self.assertNotEqual(incorrect_first_digit,
                            calc.calculate_first_digit(self.first_part_cpf_number))

    def test_cpf_calculate_second_digit_true(self):
        updated_cpf_number = self.first_part_cpf_number + \
            calc.calculate_first_digit(
                self.first_part_cpf_number)
        correct_second_digit = '5'
        self.assertEqual(correct_second_digit,
                         calc.calculate_second_digit(updated_cpf_number))

    def test_cpf_calculate_second_digit_false(self):
        updated_cpf_number = self.first_part_cpf_number + \
            calc.calculate_first_digit(
                self.first_part_cpf_number)
        incorrect_second_digit = '7'
        self.assertNotEqual(incorrect_second_digit,
                            calc.calculate_second_digit(updated_cpf_number))

    # TESTS FOR CNPJ DIGITS
    def test_cnpj_calculate_first_digit_true(self):
        correct_first_digit = '6'
        self.assertEqual(correct_first_digit,
                         calc.calculate_first_digit(self.first_part_cnpj_number))

    def test_cnpj_calculate_first_digit_false(self):
        correct_first_digit = '7'
        self.assertNotEqual(correct_first_digit,
                            calc.calculate_first_digit(self.first_part_cnpj_number))

    def test_cnpj_calculate_second_digit_true(self):
        correct_second_digit = '1'
        updated_cnpj_number = self.first_part_cnpj_number + \
            calc.calculate_first_digit(
                self.first_part_cnpj_number)
        self.assertEqual(correct_second_digit,
                         calc.calculate_second_digit(updated_cnpj_number))

    def test_cnpj_calculate_second_digit_false(self):
        correct_second_digit = '2'
        updated_cnpj_number = self.first_part_cnpj_number + \
            calc.calculate_first_digit(
                self.first_part_cnpj_number)
        self.assertNotEqual(correct_second_digit,
                            calc.calculate_second_digit(updated_cnpj_number))


if __name__ == '__main__':
    unittest.main(verbosity=2)
