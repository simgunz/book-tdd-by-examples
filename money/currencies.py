from abc import ABC, abstractmethod


class Money(ABC):
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    @staticmethod
    def dollar(amount):
        return Dollar(amount, "USD")

    @staticmethod
    def franc(amount):
        return Franc(amount, "CHF")

    def __eq__(self, other):
        return self._amount == other._amount and type(self) == type(other)

    @abstractmethod
    def times(self, multiplier):
        pass

    def currency(self):
        return self._currency


class Dollar(Money):
    def times(self, multiplier):
        return Money(self._amount * multiplier, self._currency)


class Franc(Money):
    def times(self, multiplier):
        return Money(self._amount * multiplier, self._currency)
