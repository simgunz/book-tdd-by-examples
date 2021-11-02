from abc import ABC, abstractmethod


class Money(ABC):
    def __init__(self, amount):
        self._amount = amount

    @staticmethod
    def dollar(amount):
        return Dollar(amount)

    @staticmethod
    def franc(amount):
        return Franc(amount)

    def __eq__(self, dollar):
        return self._amount == dollar._amount and isinstance(self, dollar.__class__)

    def currency(self):
        return self._currency


class Dollar(Money):
    def __init__(self, amount):
        super().__init__(amount)
        self._currency = "USD"

    def times(self, multiplier):
        return Dollar(self._amount * multiplier)


class Franc(Money):
    def __init__(self, amount):
        super().__init__(amount)
        self._currency = "CHF"

    def times(self, multiplier):
        return Money.franc(self._amount * multiplier)
