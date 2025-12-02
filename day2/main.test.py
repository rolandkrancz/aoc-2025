import unittest
import sys
import os

from main import GetInvalidIds

class TestGetInvalidIds(unittest.TestCase):

    def test_dummy(self):
        result = GetInvalidIds()
        self.assertEqual(result, -1)

if __name__ == '__main__':
    unittest.main()
