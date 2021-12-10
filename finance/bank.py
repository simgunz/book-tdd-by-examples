class Bank:
    def reduce(self, source, to):
        return source.reduce(self, to)

    def rate(self, from_, to):
        rate = 1
        if from_ == "CHF" and to == "USD":
            rate = 2
        return rate
