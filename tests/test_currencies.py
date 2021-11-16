import unittest

from finance.currencies import Money
from finance.bank import Bank
from finance.sum import Sum


class TestMoney(unittest.TestCase):
    def test_currency(self):
        self.assertEqual("USD", Money.dollar(1).currency())
        self.assertEqual("CHF", Money.franc(1).currency())

    def test_multiplication(self):
        five = Money.dollar(5)
        self.assertEqual(Money.dollar(10), five.times(2))
        self.assertEqual(Money.dollar(15), five.times(3))

    def test_equality(self):
        self.assertEqual(Money.dollar(5), Money.dollar(5))
        self.assertNotEqual(Money.dollar(5), Money.dollar(6))
        self.assertNotEqual(Money.dollar(5), Money.franc(5))

    def test_simple_addition(self):
        five = Money.dollar(5)
        sum = five.plus(five)
        bank = Bank()
        reduced = bank.reduce(sum, "USD")
        self.assertEqual(Money.dollar(10), reduced)

    def test_sum_returns_sum(self):
        five = Money.dollar(5)
        sum = five.plus(five)
        self.assertEqual(five, sum.augend)
        self.assertEqual(five, sum.addend)
