from Operations.Operation import Operation


class Divide(Operation):
    def __init__(self, x):
        self.divisor = x

    def compute(self, result):
        return result / self.divisor
