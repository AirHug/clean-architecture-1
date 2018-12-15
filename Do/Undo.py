from Do.Do import Do


class Undo(Do):
    def __init__(self, x):
        self.step = x

    def do(self, calculate):
        if (calculate.step - self.step) <= 0:
            return 0
        else:
            return calculate.step - self.step
