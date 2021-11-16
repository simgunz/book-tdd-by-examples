from finance.currencies import Money


class Bank:
    def reduce(self, source, to):
        return source.reduce(to)
