class WasRun:
    def __init__(self, name) -> None:
        self.wasRun = False

    def testMethod(self):
        self.wasRun = True

    def run(self):
        self.testMethod()
