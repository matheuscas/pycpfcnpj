Project usage examples
===================================

Using pycpfcnpj.cpfcnpj
-------------------
.. code-block:: python
   :emphasize-lines: 3,5
	
	import pycpfcnpj.cpfcnpj as cpfcnpj

	valid_cpf = '11144477735'
	invalid_cpf = '11144477736'

	cpfcnpj.validate(valid_cpf)
	cpfcnpj.validate(invalid_cpf)

	valid_cnpj = '11444777000161'
	invalid_cnpj = '11444777000162'

	cpfcnpj.validate(valid_cnpj)
	cpfcnpj.validate(invalid_cnpj)

For pycpfcnpj.cpfcnpj it does not matter if the number is a CPF or CNPJ.
It's just validates!

Using pycpfcnpj.cpf
-----------------	
.. code-block:: python
   :emphasize-lines: 3,5

   import pycpfcnpj.cpf as cpf

   valid_cpf = '11144477735'
   invalid_cpf = '11144477736'

   cpf.validate(valid_cpf)
   cpf.validate(invalid_cpf)

In this case, only accepts CPF numbers. 
	
Using pycpfcnpj.cnpj
------------------	
.. code-block:: python
   :emphasize-lines: 3,5

   valid_cnpj = '11444777000161'
   invalid_cnpj = '11444777000162'

   cnpj.validate(valid_cnpj)
   cnpj.validate(invalid_cnpj)

In this case, only accepts CNPJ numbers.   