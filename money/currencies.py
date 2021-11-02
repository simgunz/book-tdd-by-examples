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

    @abstractmethod
    def currency(self):
        pass


class Dollar(Money):
    def times(self, multiplier):
        return Dollar(self._amount * multiplier)

    def currency(self):
        return "USD"


class Franc(Money):
    def times(self, multiplier):
        return Franc(self._amount * multiplier)

    def currency(self):
        return "CHF"
