from Calculator import Calculator
from Operations.Add import Add
from Operations.Minus import Minus
from Operations.Times import Times
from Operations.Divide import Divide
from Operations.Power import Power
from Do.Redo import Redo
from Do.Undo import Undo

calculator = Calculator(13)
# 20 10 80 4 64
calculator.compute(Add(7)) \
    .compute(Minus(10)) \
    .compute(Times(8)) \
    .compute(Divide(20)) \
    .compute(Power(3))
print(calculator.getResult())
calculator.do(Undo(2))
calculator.compute(Minus(2))
print(calculator.getResult())
calculator.do(Redo(1))
print(calculator.getResult())
