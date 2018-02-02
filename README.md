Pycpfcnpj
=======

Description
-----------
Python module for brazilian register numbers for persons (CPF) and companies (CNPJ).

**Python 3 ready!**

[![Build Status](https://travis-ci.org/matheuscas/pycpfcnpj.png?branch=master)](https://travis-ci.org/matheuscas/pycpfcnpj)
[![codecov](https://codecov.io/gh/matheuscas/pycpfcnpj/branch/master/graph/badge.svg)](https://codecov.io/gh/matheuscas/pycpfcnpj)
[![PyPI version](https://badge.fury.io/py/pycpfcnpj.svg)](https://badge.fury.io/py/pycpfcnpj)

### How to install
Now you can install this module with pip! Yeah! :D

```
pip install pycpfcnpj
```

### Quick Start
To use pycpfcnpj is simples like as every python module shoud be!

```python
from pycpfcnpj import cpfcnpj
cpf_number = '11144477735'
masked_cpf_number = '111.444.777-35'
cnpj_number = '11444777000161'
masked_cnpj_number = '11.444.777/0001-61'

print cpfcnpj.validate(cpf_number)
print cpfcnpj.validate(masked_cpf_number)
print cpfcnpj.validate(cnpj_number)
print cpfcnpj.validate(masked_cnpj_number)

Expected output:
>>>True
>>>True
>>>True
>>>True
```
Simple like that. =)

You can use, as well, the cpf and cnpj packages. The cpfcnpj is like a Facade to the other modules. Make yourself confortable.

Oh, fork and contribute either if you want to.

Obs.: There is no dependencies. 

Oh, and before I forget, You can generate, only and only for test purposes, a CPF or CNPJ number using the 'gen' module. Easy like above:

```python
from pycpfcnpj import gen
gen.cpf()
gen.cnpj()

Expected output:
>>> 49384063495
>>> 20788274885880
```

And you also can generate CPF or CǸPJ with punctuation marks. :)

```python
from pycpfcnpj import gen
gen.cpf_with_punctuation()
gen.cnpj_with_punctuation()

Expected output:
>>> 048.891.866-97
>>> 63.212.638/0361-35
```

Have fun!

In portuguese:
--------------

Módulo python para validar números de CPF e CNPJ.

### Como instalar:
Agora você pode instalar o pycpfcnpj usando o pip!\m/

```
pip install pycpfcnpj
```

### Como usar
```python
from pycpfcnpj import cpfcnpj
numero_cpf = '11144477735'
numero_cpf_mascara = '111.444.777-35'
numero_cnpj = '11444777000161'
numero_cnpj_mascara = '11.444.777/0001-61'

print cpfcnpj.validate(numero_cpf)
print cpfcnpj.validate(numero_cpf_mascara)
print cpfcnpj.validate(numero_cnpj)
print cpfcnpj.validate(numero_cnpj_mascara)

Expected output:
>>>True
>>>True
>>>True
>>>True
```

Simples assim! Você também pode usar os pacotes internos que tratam em separado os números de CPF e CNPJ. O módulo 'cpfcnpj' é um tipo de interface para os módulos mais especificos e se encarrega de saber quando você está passando um CPF ou um CNPJ. 

Fique à vontade em contribuir com o projeto ou da maneira que quiser. Ah, sim: pure python (sem dependências ;) ).

Ah, e antes que eu me esqueça, você pode gerar, só e apenas somente para fins de teste, um número de CPF ou CNPJ utilizando o módulo 'gen'. Fácil como acima:

```python
from pycpfcnpj import gen
gen.cpf()
gen.cnpj()

Expected output:
>>> 49384063495
>>> 20788274885880
```

E você também pode gerar CPF ou CNPJ com pontuação :)

```python
from pycpfcnpj import gen
gen.cpf_with_punctuation()
gen.cnpj_with_punctuation()

Expected output:
>>> 048.891.866-97
>>> 63.212.638/0361-35
```


Divirta-se!

Changelog
-----------

1.1
- Handles CPF and CNPJ numbers with punctuation marks (Trata números de CPF e CPNJ com sinais de pontuação)

1.2
- Use `sys` rather than `six` to check python's version and keeps this project 100% free of dependencies.

1.3
- Generate CPF and CNPJ numbers with punctuation marks.
