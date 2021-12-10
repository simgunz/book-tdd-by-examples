class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self._currency = currency

    @staticmethod
    def dollar(amount):
        return Money(amount, "USD")

    @staticmethod
    def franc(amount):
        return Money(amount, "CHF")

    def __repr__(self):
        return "Money(%s, %s)" % (self.amount, self._currency)

    def __eq__(self, other):
        return self._currency == other.currency() and self.amount == other.amount

    def times(self, multiplier):
        return Money(self.amount * multiplier, self._currency)

    def currency(self):
        return self._currency

    def plus(self, addend):
        from finance.sum import Sum

        return Sum(self, addend)

    def reduce(self, to):
        if self.currency() == "CHF" and to == "USD":
            rate = 2
        else:
            rate = 1
        return Money(self.amount / rate, to)
