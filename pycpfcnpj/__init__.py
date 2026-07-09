from importlib.metadata import PackageNotFoundError, version

__author__ = 'Matheus Cardoso'
try:
    __version__ = version("pycpfcnpj")
except PackageNotFoundError:  # package is not installed
    __version__ = "0.0.0.dev0"
