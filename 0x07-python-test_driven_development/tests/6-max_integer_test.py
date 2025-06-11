import unittest

max_integer = __import__('6-max_integer').max_integer

class TestForMaxInteger(unittest.TestCase):
    def test_if_listempty(self):
        self.assertEqual(max_integer([]), None)
