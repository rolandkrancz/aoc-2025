import unittest
import sys
import os

# Add parent src directory to path to import main
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from main import GetResult

class TestGetResult(unittest.TestCase):

    def test_simple_right(self):
        test_input = ["R50"]
        result = GetResult(test_input)
        self.assertEqual(result, 1)

    def test_simple_left(self):
        test_input = ["L50"]
        result = GetResult(test_input)
        self.assertEqual(result, 1)

    def test_overflow(self):
        test_input = ["R140", "R490", "L580"]
        result = GetResult(test_input)
        self.assertEqual(result, 1)

    def test_sample_from_aoc(self):
        test_input_path = os.path.join(os.path.dirname(__file__), "test_input.txt")
        with open(test_input_path, "r") as testinput:
            result = GetResult(testinput)
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()
