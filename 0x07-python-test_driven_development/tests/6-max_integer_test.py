import unittest

def sqrt(x):
    if x < 0:
        raise ValueError("Must be a number greater than Zero")
    for y in range(100):
        if y ** 2 == x:
            return y


class TestingSqrtFunction(unittest.TestCase):
    def test_for_valuerror(self):
        with self.assertRaises(ValueError):
            sqrt(-1)
    def test_sqrt(self):
        self.assertEqual(sqrt(4), 2)


if __name__ == '__main__':
    unittest.main()