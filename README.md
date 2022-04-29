Pycpfcnpj
=======

Description
-----------
Python module for brazilian register numbers for persons (CPF) and companies (CNPJ). If want this validation in your web application, please check [my tiny web component](https://github.com/matheuscas/wc-input-cpf-cnpj) that does exactly that. ;)

**Python 3 ready!**

[![Build Status](https://travis-ci.org/matheuscas/pycpfcnpj.png?branch=master)](https://travis-ci.org/matheuscas/pycpfcnpj)
[![codecov](https://codecov.io/gh/matheuscas/pycpfcnpj/branch/master/graph/badge.svg)](https://codecov.io/gh/matheuscas/pycpfcnpj)
[![PyPI version](https://badge.fury.io/py/pycpfcnpj.svg)](https://badge.fury.io/py/pycpfcnpj)
![Python versions](https://img.shields.io/pypi/pyversions/pycpfcnpj)

#### Related projects
- [Pycnpj-crawler](https://github.com/matheuscas/pycnpj-crawler): Python module that crawls data for a given CNPJ on the government website of each state (please check the supported states).


### How to install
Now you can install this module with pip! Yeah! :D

```
pip install pycpfcnpj
```

### Quick Start
To use pycpfcnpj is simples like as every python module should be!

```python
from pycpfcnpj import cpfcnpj
cpf_number = '11144477735'
masked_cpf_number = '111.444.777-35'
cnpj_number = '11444777000161'
masked_cnpj_number = '11.444.777/0001-61'

print(cpfcnpj.validate(cpf_number))
print(cpfcnpj.validate(masked_cpf_number))
print(cpfcnpj.validate(cnpj_number))
print(cpfcnpj.validate(masked_cnpj_number))

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

Oh, and before I forget, you can generate, only and only for test purposes, a CPF or CNPJ number using the 'gen' module. Easy like above:

```python
from pycpfcnpj import gen
gen.cpf()
gen.cnpj()

Expected output:
>>> 49384063495
>>> 20788274885880
```

Also, you can generate CPF or CǸPJ with punctuation marks. :)

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

#### Projetos relacionados
- [Pycnpj-crawler](https://github.com/matheuscas/pycnpj-crawler)

### Como usar
```python
from pycpfcnpj import cpfcnpj
cpf_number = '11144477735'
masked_cpf_number = '111.444.777-35'
cnpj_number = '11444777000161'
masked_cnpj_number = '11.444.777/0001-61'

print(cpfcnpj.validate(cpf_number))
print(cpfcnpj.validate(masked_cpf_number))
print(cpfcnpj.validate(cnpj_number))
print(cpfcnpj.validate(masked_cnpj_number))

Expected output:
>>>True
>>>True
>>>True
>>>True
```

Simples assim! Você também pode usar os pacotes internos que tratam em separado os números de CPF e CNPJ. 
O módulo 'cpfcnpj' é um tipo de interface para os módulos mais específicos e se encarrega de saber quando você está passando um CPF ou um CNPJ.

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
1.7.1
- Fix for cpf/cnpjs containing special characters.

1.7.0
- Invalidates cpf/cnpjs containing non-numeric characters and spaces.

1.6.0
- Remove python 2.7 support
- Add python 3.8 support

1.1
- Handles CPF and CNPJ numbers with punctuation marks.

1.2
- Use `sys` rather than `six` to check python's version and keeps this project 100% free of dependencies.

1.3
- Generate CPF and CNPJ numbers with punctuation marks.

1.4
- Adding support to unicode values.

1.5
- Better CPF and CNPJ generation

1.5.1
- Use regex to remove punctuation


Log de mudanças
-----------
1.7.1
- Correção para cpf/cnpjs que contém caracteres especials.

1.7.0
- Invalida cpf/cnpjs que contém caracteres não numéricos e espaços.

1.6.0
- Remove suporte para python 2.7
- Adiciona suporte para python 3.8

1.1
- Trata números de CPF e CPNJ com sinais de pontuação

1.2
- Uso do `sys` em vez do `six` para verificar a versão do Python e evitando o uso de libs terceiras

1.3
- Gera números de CPF e CNPJ com pontuação.

1.4
- Suporte a unicode.

1.5
- Geração de CPF e CNPJ mais eficiente.

1.5.1
- Regex para remover a pontuação.
