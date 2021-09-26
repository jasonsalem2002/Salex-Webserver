import numpy
from tabulate import tabulate

# insert the equation here (need to fix sqrt/ cos/ sin ...)

f = lambda x: x ** 3 -x -1


An = []
Bn = []
errors = []
Pn = []
FPn = []


def bisection(f, a, b, error):

    p = (a + b) / 2

    if numpy.abs(f(p)) < error:
        return p

    if numpy.sign(f(a)) == numpy.sign(f(p)):
        An.append(a), Bn.append(b)
        return bisection(f, p, b, error)

    elif numpy.sign(f(b)) == numpy.sign(f(p)):
        An.append(a), Bn.append(b)
        return bisection(f, a, p, error)

print("Ex 17 --> P14 = 1.32472")

tolerance = int(input("Enter the tolerance: "))

a = float(input("First num interval: "))
b = float(input("Second num interval: "))

for i in range(tolerance):
    eq = bisection(f, a, b, 1*10**(-i))
    errors.append(i)
    Pn.append(eq)
    FPn.append(f(eq))

table = zip(errors, An, Bn, Pn, FPn)
print(tabulate(table, headers=["Tolerance", "An", "Bn", "Pn", "F(Pn)"],  tablefmt="fancy_grid"))