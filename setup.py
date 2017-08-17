from setuptools import setup

setup(name='pycpfcnpj',
      version='1.1',
      description='Python module for brazilian register numbers for persons (CPF) and companies (CNPJ).',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.6',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='cpf cnpj validation generation',
      url='https://github.com/matheuscas/pycpfcnpj',
      author='Matheus Cardoso',
      author_email='matheus.mcas@gmail.com',
      license='MIT',
      install_requires=[
          'six==1.10.0'
      ],
      packages=['pycpfcnpj'],
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)
