Project usage examples
===================================

Using pycnpfj.cnpfj
-------------------
.. code-block:: python
   :emphasize-lines: 3,5
	
	import pycnpfj.cnpfj as cnpfj

	valid_cpf = '11144477735'
	invalid_cpf = '11144477736'

	cnpfj.validate(valid_cpf)
	cnpfj.validate(invalid_cpf)

	valid_cnpj = '11444777000161'
	invalid_cnpj = '11444777000162'

	cnpfj.validate(valid_cnpj)
	cnpfj.validate(invalid_cnpj)

For pycnpfj.cnpfj it does not matter if the number is a CPF or CNPJ.
It's just validates!

Using pycnpfj.cpf
-----------------	
.. code-block:: python
   :emphasize-lines: 3,5

   import pycnpfj.cpf as cpf

   valid_cpf = '11144477735'
   invalid_cpf = '11144477736'

   cpf.validate(valid_cpf)
   cpf.validate(invalid_cpf)

In this case, only accepts CPF numbers. 
	
Using pycnpfj.cnpj
------------------	
.. code-block:: python
   :emphasize-lines: 3,5

   valid_cnpj = '11444777000161'
   invalid_cnpj = '11444777000162'

   cnpj.validate(valid_cnpj)
   cnpj.validate(invalid_cnpj)

In this case, only accepts CNPJ numbers.   