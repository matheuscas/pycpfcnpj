Pycnpfj
=======

Description
-----------
Python module for brazilian register numbers for persons (CPF) and companies (CNPJ).

[![Build Status](https://travis-ci.org/matheuscas/pycnpfj.png?branch=master)](https://travis-ci.org/matheuscas/pycnpfj)
[![Coverage Status](https://coveralls.io/repos/matheuscas/pycnpfj/badge.png)](https://coveralls.io/r/matheuscas/pycnpfj)

###Quick Start
To use pycnpfj is simples like as every python module shoud be!

```python
from pycnpfj import cnpfj
cpf_number = '11144477735'
cnpj_number = '11444777000161'
print cnpfj.validate(cpf_number)
print cnpfj.validate(cnpj_number)

Expected output:
>>>True
>>>True
```
Simple like that. =)

You can use, as well, the cpf and cnpj packages. The cnpfj is like a Facade to the other modules. Make yourself confortable.

Oh, fork and contribute either if you want to.

Obs.: There is no dependencies.  


