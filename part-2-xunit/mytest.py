class TestCase:
    def __init__(self, name) -> None:
        self.name = name

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()
        return TestResult()


class WasRun(TestCase):
    def __init__(self, name) -> None:
        self.wasRun = None
        TestCase.__init__(self, name)

    def setUp(self):
        self.wasRun = None
        self.log = "setUp "

    def testMethod(self):
        self.wasRun = True
        self.log += "testMethod "

    def tearDown(self):
        self.log += "tearDown "


class TestResult:
    def __init__(self):
        self.runCount = 1

    def summary(self):
        return f"{self.runCount} run, 0 failed"
