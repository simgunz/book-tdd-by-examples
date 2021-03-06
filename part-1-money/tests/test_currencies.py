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

    def test_reduce_sum(self):
        sum = Sum(Money.dollar(3), Money.dollar(4))
        bank = Bank()
        result = bank.reduce(sum, "USD")
        self.assertEqual(Money.dollar(7), result)

    def test_reduce_money(self):
        bank = Bank()
        result = bank.reduce(Money.dollar(1), "USD")
        self.assertEqual(Money.dollar(1), result)

    def test_reduce_money_different_currency(self):
        bank = Bank()
        bank.addRate("CHF", "USD", 2)
        result = bank.reduce(Money.franc(2), "USD")
        self.assertEqual(Money.dollar(1), result)

    def test_identity_rate(self):
        bank = Bank()
        self.assertEqual(1, bank.rate("USD", "USD"))

    def test_mixed_addition(self):
        fiveBucks = Money.dollar(5)
        tenFrancs = Money.franc(10)
        bank = Bank()
        bank.addRate("CHF", "USD", 2)
        result = bank.reduce(fiveBucks.plus(tenFrancs), "USD")
        self.assertEqual(Money.dollar(10), result)

    def test_money_plus_sum(self):
        fiveBucks = Money.dollar(5)
        tenFrancs = Money.franc(10)
        bank = Bank()
        bank.addRate("CHF", "USD", 2)
        result = bank.reduce(Sum(fiveBucks, tenFrancs).plus(fiveBucks), "USD")
        self.assertEqual(Money.dollar(15), result)

    def test_sum_times(self):
        fiveBucks = Money.dollar(5)
        tenFrancs = Money.franc(10)
        bank = Bank()
        bank.addRate("CHF", "USD", 2)
        sum = Sum(fiveBucks, tenFrancs).times(2)
        result = bank.reduce(sum, "USD")
        self.assertEqual(Money.dollar(20), result)
