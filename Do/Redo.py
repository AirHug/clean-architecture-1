from Do.Do import Do


class Redo(Do):
    def __init__(self, x):
        self.step = x

    def do(self, calculate):
        if (calculate.step + self.step) > len(calculate.logs):
            return len(calculate.logs)
        else:
            return calculate.step + self.step
