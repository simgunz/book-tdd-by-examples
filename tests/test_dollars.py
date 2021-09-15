import unittest

from money.dollar import Dollar


class TestDollar(unittest.TestCase):
    def test_multiplication(self):
        five = Dollar(5)
        product = five.times(2)
        self.assertEqual(10, product.amount)
        product = five.times(3)
        self.assertEqual(15, product.amount)

    def test_equality(self):
        self.assertEqual(Dollar(5), Dollar(5))
        self.assertNotEqual(Dollar(5), Dollar(6))
