import unittest
from importlib.metadata import version

import pycpfcnpj


class VersionTests(unittest.TestCase):
    """Guard against __version__ drifting from the packaged metadata."""

    def test_version_is_non_empty_string(self):
        self.assertIsInstance(pycpfcnpj.__version__, str)
        self.assertTrue(pycpfcnpj.__version__)

    def test_version_matches_installed_metadata(self):
        # When the package is installed, __version__ must come from the
        # distribution metadata instead of a hardcoded (and stale) value.
        self.assertEqual(pycpfcnpj.__version__, version("pycpfcnpj"))
