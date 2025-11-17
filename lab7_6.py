"""
Unit tests for the greet function in lab7_5.py.
"""

import unittest
from lab7_5 import greet
from io import StringIO
import sys

class TestGreet(unittest.TestCase):
    def test_greet_output(self):
        """Test that greet prints the correct message."""
        captured_output = StringIO()
        sys.stdout = captured_output
        greet("John")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Hello, John!")

if __name__ == "__main__":
    unittest.main()


#python -m unittest test_lab7_6.py