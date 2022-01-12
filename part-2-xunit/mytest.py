class TestCase:
    pass


class WasRun(TestCase):
    def __init__(self, name) -> None:
        self.wasRun = None
        self.name = name

    def testMethod(self):
        self.wasRun = True

    def run(self):
        method = getattr(self, self.name)
        method()
