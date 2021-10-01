class Money:
    def __init__(self, amount):
        self._amount = amount


class Dollar(Money):
    def times(self, multiplier):
        return Dollar(self._amount * multiplier)

    def __eq__(self, dollar):
        return self._amount == dollar._amount


class Franc(Money):
    def times(self, multiplier):
        return Franc(self._amount * multiplier)

    def __eq__(self, dollar):
        return self._amount == dollar._amount
