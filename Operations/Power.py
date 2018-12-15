from Operations.Operation import Operation

class Power(Operation):
    def __init__(self, x):
        self.power = x

    def compute(self, result):
        return result ** self.power
