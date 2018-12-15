from Operations.Operation import Operation

class Add(Operation):
    def __init__(self, x):
        self.addend = x

    def compute(self, result):
        return result + self.addend
