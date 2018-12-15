from Operations.Operation import Operation


class Minus(Operation):
    def __init__(self, x):
        self.substrahend = x

    def compute(self, result):
        return result - self.substrahend
