import numpy as np
from tabulate import tabulate

def my_bisection(f, a, b, tol):
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception("The scalars a and b do not bound a root")  # get midpoint
    m = (a + b) / 2
    if np.abs(f(m)) < tol:
        return m
    elif np.sign(f(a)) == np.sign(f(m)):
        As.append(a)
        Bs.append(b)
        return my_bisection(f, m, b, tol)

    elif np.sign(f(b)) == np.sign(f(m)):
        As.append(a)
        Bs.append(b)
        return my_bisection(f, a, m, tol)

f = lambda x: (x+2) * (x+1) * (x) * ((x - 1)**3 ) * (x -2)

n = int(input("Error range: "))

headers=['Error', 'An', 'Bn', 'Pn', 'F(Pn)']
errors = []
Rs =[]
FRs = []
As =[]
Bs= []
j = 1
for i in range(n):
    r = my_bisection(f, -2.5, 3, j)
    errors.append(i)
    Rs.append(r)
    FRs.append(f(r))
    j = 1 * 10 ** (-i)
    # print(f"r{i} =", r, f"f(r{i}) =", f(r))

table = zip(errors, As, Bs, Rs, FRs)
print(tabulate(table, headers=headers, floatfmt=".20f"))