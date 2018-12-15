class Calculator:
    def __init__(self, num):
        self.num = num
        self.step = 0
        self.logs = []

    def getResult(self):
        result = self.num
        index = 1
        for log in self.logs:
            if index <= self.step:
                result = log.compute(result)
                index += 1
            else:
                break
        return result

    def compute(self, operation):
        self.logs = self.logs[0:self.step]
        self.step += 1
        self.logs.append(operation)
        return self

    def do(self, do):
        self.step = do.do(self)
