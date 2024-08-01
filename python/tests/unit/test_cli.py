"""The unit tests."""

import unittest
import sys

import myapp.cli


class TestCli(unittest.TestCase):
    """Test the cli."""

    def test_simple_addition(self):
        """Test the simple_addition() method."""
        self.assertEqual(myapp.cli.simple_addition(1), 2)

    def test_simple_multiplication(self):
        """Test the simple_multiplication() method."""
        self.assertEqual(myapp.cli.simple_multiplication(2), 4)

    def test_parse_commandline(self):
        """Test the commandline parser."""
        with unittest.mock.patch.object(sys, "argv", ["myapp", "2"]):
            options = myapp.cli.parse_commandline()
            self.assertEqual(int(options.N), 2)
