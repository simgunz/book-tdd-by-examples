class TestCase:
    def __init__(self, name) -> None:
        self.name = name


class WasRun(TestCase):
    def __init__(self, name) -> None:
        self.wasRun = None
        TestCase.__init__(self, name)

    def testMethod(self):
        self.wasRun = True

    def run(self):
        method = getattr(self, self.name)
        method()
