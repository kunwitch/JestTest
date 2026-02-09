# test_jesttest.py
"""
Tests for JestTest module.
"""

import unittest
from jesttest import JestTest

class TestJestTest(unittest.TestCase):
    """Test cases for JestTest class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = JestTest()
        self.assertIsInstance(instance, JestTest)
        
    def test_run_method(self):
        """Test the run method."""
        instance = JestTest()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
