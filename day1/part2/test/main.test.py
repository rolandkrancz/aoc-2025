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

    def test_overflow_right(self):
        test_input = ["R500"]
        result = GetResult(test_input)
        self.assertEqual(result, 5)

    def test_overflow_left(self):
        test_input = ["L200"]
        result = GetResult(test_input)
        self.assertEqual(result, 2)
    
    def test_overflow_right_lands_on_zero(self):
        test_input = ["R250"]
        result = GetResult(test_input)
        self.assertEqual(result, 3)

    def test_overflow_left_lands_on_zero(self):
        test_input = ["L250"]
        result = GetResult(test_input)
        self.assertEqual(result, 3)

    def test_sample_from_aoc(self):
        test_input_path = os.path.join(os.path.dirname(__file__), "test_input.txt")
        with open(test_input_path, "r") as testinput:
            result = GetResult(testinput)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()
