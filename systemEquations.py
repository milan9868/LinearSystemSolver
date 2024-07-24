from z3 import *


n = int(input("Unesite dimenziju sistema: "))
matrix = []
for i in range(n):
    numbers = input(f"Unesite koeficijente za {i}. jednacinu: ")
    numbers_parsed = [int(i) for i in numbers.split()]
    matrix.append(numbers_parsed)

print(matrix)


x, y, z = Ints('x y z')
variables = [x, y, z]
s = Solver()
for i in range(n):
    constraint = sum(a*b for a, b in zip(variables,matrix[i][:-1])) == matrix[i][-1]
    s.add(constraint)

if s.check() == sat:
    solutions = s.model()
    print(f"x = {solutions[x]}")
    print(f"y = {solutions[y]}")
    #print(f"z = {solutions[z]}")






