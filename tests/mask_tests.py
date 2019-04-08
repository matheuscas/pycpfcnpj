import unittest

from pycpfcnpj.mask import cpf_mask, cnpj_mask


class MaskCPFTest(unittest.TestCase):
    def test_mask_cpf(self):
        cpf = '70597084050'
        self.assertEqual(cpf_mask(cpf), '705.970.840-50')


class MaskCNPJTest(unittest.TestCase):
    def test_mask_cnpj(self):
        cnpj = '16039776000155'
        self.assertEqual(cnpj_mask(cnpj), '16.039.776/0001-55')
