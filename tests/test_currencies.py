import unittest

from money.currencies import Money, Franc


class TestDollar(unittest.TestCase):
    def test_multiplication(self):
        five = Money.dollar(5)
        self.assertEqual(Money.dollar(10), five.times(2))
        self.assertEqual(Money.dollar(15), five.times(3))

    def test_equality(self):
        self.assertEqual(Money.dollar(5), Money.dollar(5))
        self.assertNotEqual(Money.dollar(5), Money.dollar(6))
        self.assertNotEqual(Money.dollar(5), Franc(5))


class TestFranc(unittest.TestCase):
    def test_multiplication(self):
        five = Franc(5)
        self.assertEqual(Franc(10), five.times(2))
        self.assertEqual(Franc(15), five.times(3))

    def test_equality(self):
        self.assertEqual(Franc(5), Franc(5))
        self.assertNotEqual(Franc(5), Franc(6))
