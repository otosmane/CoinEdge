# test_coinedge.py
"""
Tests for CoinEdge module.
"""

import unittest
from coinedge import CoinEdge

class TestCoinEdge(unittest.TestCase):
    """Test cases for CoinEdge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CoinEdge()
        self.assertIsInstance(instance, CoinEdge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CoinEdge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
