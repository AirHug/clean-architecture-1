from Operations.Operation import Operation


class Times(Operation):
    def __init__(self, x):
        self.multiplier = x

    def compute(self, result):
        return result * self.multiplier
