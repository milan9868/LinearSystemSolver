import z3
from z3 import Int, Solver


x = Int('x')
y = Int('y')
s = Solver()
s.add(x > 6)
s.add(y > 9)
s.add(x + y == 0)

if s.check() == z3.sat:
    model = s.model()
    print(f"x = {model[x]}")
    print(f"y = {model[y]}")
else:
    print("nema resenja")



