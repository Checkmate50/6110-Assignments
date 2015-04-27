#x^3yz + 2y^4z^2 - 7xy^5z = 6

#Using python 2.7

from z3 import *

s = Solver()
x = Int('x');
y = Int('y');
z = Int('z');

s.add(x*x*x*y*z + 2*y*y*y*y*z*z - 7*x*y*y*y*y*y*z == 6)

print(s)

print(s.check())
print(s.model())