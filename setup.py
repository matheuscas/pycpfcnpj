import pathlib
from setuptools import setup

current_directory = pathlib.Path(__file__).parent

README = (current_directory / "README.md").read_text()

setup(
    name="pycpfcnpj",
    version="1.7.0",
    description="Python module for brazilian register numbers for persons (CPF) and companies (CNPJ).",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="cpf cnpj validation generation",
    url="https://github.com/matheuscas/pycpfcnpj",
    author="Matheus Cardoso",
    author_email="matheus.mcas@gmail.com",
    license="MIT",
    packages=["pycpfcnpj"],
    test_suite="nose.collector",
    tests_require=["nose"],
    zip_safe=False,
    long_description=README,
    long_description_content_type="text/markdown",
)
