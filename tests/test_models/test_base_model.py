#!/usr/bin/python3
"""Unittests for BaseModel class.
"""
import unittest
from models.base_model import BaseModel
import pep8
from datetime import datetime


class BaseModelTest(unittest.TestCase):
    """Unittests for Basemodel class.
    """
    def setup(self):
        """Setting up an instance for testing.
        """
        self.base = BaseModel()

    def delet(self):
        """
        Deleting the instance after testing.
        """
        del self.base

    def test_pep8(self):
        """Testing pep8 compliance.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0, "\
            Found code style errors (and warnings).")

    def test_documentation(self):
        """Testing for docstrings in module, class and methods.
        """
        self.assertTrue(len(BaseModel.__doc__) >= 1)
        self.assertTrue(len(BaseModel.__init__.__doc__) >= 1)


if __name__ == "__main__":
    unittest.main()

