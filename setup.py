import os

from setuptools import setup, find_packages


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

setup(
      name='pycpfcnpj',
      packages=find_packages(exclude=['tests*']),
      version='1.0',
      description='Python module for brazilian register numbers for persons (CPF) and companies (CNPJ).',
      author='Matheus Cardoso',
      author_email='matheus.mcas@gmail.com',
      url='https://github.com/matheuscas/pycpfcnpj',
      license='MIT',
      download_url='https://github.com/matheuscas/pycpfcnpj/tarball/1.0',
      keywords=['cnpj','cpj','validation','generation','validacao','geracao'],
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: Portuguese',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ]
)