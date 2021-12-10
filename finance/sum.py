from finance.currencies import Money
from finance.bank import Bank


class Sum:
    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend

    def reduce(self, bank: Bank, to: str) -> Money:
        amount = (
            self.augend.reduce(bank, to).amount + self.addend.reduce(bank, to).amount
        )
        return Money(amount, to)
