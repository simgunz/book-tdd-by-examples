from collections import namedtuple


Pair = namedtuple("Pair", ["from_", "to"])


class Bank:
    def __init__(self):
        self.rates = {}

    def reduce(self, source, to):
        return source.reduce(self, to)

    def addRate(self, from_: str, to: str, rate: int) -> None:
        pair = Pair(from_, to)
        self.rates[pair] = rate

    def rate(self, from_: str, to: str) -> int:
        pair = Pair(from_, to)
        return self.rates[pair]
