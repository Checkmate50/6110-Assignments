"""
Some simple floating point testbenches for z3
All tests should result in at least 30 solutions
Formulas recommended by Alexey Solovyev
Code written by Dietrich Geisler
Code last modified 3/29/2015
Python Version 2.7
"""

from z3 import *
import re
from fractions import Fraction

def output(model, variables):
	
	ofile = file("simple_results.txt", 'a')
	ofile.write(str(model) + "\n")
	iterations = 29
	
	while (str(model.check()) == "sat" and iterations >= 0):
		ofile.write(str(model.model()))
		if (iterations % 5 == 0):
			ofile.write("\n")
		else:
			ofile.write(" \t")
			
		values = map(Fraction, re.findall(r'\d+[/]?\d*', str(model.model()))) #Get all integer values from the model
		for i in range(len(variables)):
			s.add(variables[i] != values[i]) #Remove previous solution from available solutions
		iterations -= 1
		
	ofile.write(str(29 - iterations) + " results generated successfully\n\n")

clearer = file("simple_results.txt", 'w') #Clears the file before use
s = Solver()

t = Real('t')
s.add(t >= 0)
s.add(t <= 999)
s.add((t / (t + 1)) >= 0)
s.add((t / (t + 1)) <= 1.0)
output(s, [t])

s = Solver()

x = Real('x')
y = Real('y')
s.add(x >= 1.001)
s.add(x <= 2)
s.add(y >= 1.001)
s.add(y <= 2)
s.add((x * y - 1) / ((x * y) * (x * y) - 1) >= .2)
s.add((x * y - 1) / ((x * y) * (x * y) - 1) <= .5)
output(s, [x, y])

s = Solver()

x0 = Real('x0')
x1 = Real('x1')
x2 = Real('x2')
s.add(x0 >= 1)
s.add(x0 <= 2)
s.add(x1 >= 1)
s.add(x1 <= 2)
s.add(x2 >= 1)
s.add(x2 <= 2)
s.add((((x0 + x1) - x2) + ((x1 + x2) - x0)) + ((x2 + x0) - x1)  >= 3)
s.add((((x0 + x1) - x2) + ((x1 + x2) - x0)) + ((x2 + x0) - x1)  <= 6)
output(s, [x0, x1, x2])

"""
3) sum3_bounds.smt2
The following inequality over double precision floating-point numbers is 
encoded:

Forall x0, x1, x2, 1.0 <= x0, x1, x2 <= 2.0
    ==> 3.0 <= (((x0 + x1) - x2) + ((x1 + x2) - x0)) + ((x2 + x0) - x1) 
<= 6.0
"""