from abc import abstractmethod


class Money:
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    @staticmethod
    def dollar(amount):
        return Dollar(amount, "USD")

    @staticmethod
    def franc(amount):
        return Franc(amount, "CHF")

    def __repr__(self):
        return "Money(%s, %s)" % (self._amount, self._currency)

    def __eq__(self, other):
        return self._currency == other.currency() and self._amount == other._amount

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
        return Franc(self._amount * multiplier, self._currency)
