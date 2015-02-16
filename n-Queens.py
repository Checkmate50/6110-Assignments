'''
This program generates the solution to the n-queens problem for the given integer input
That is, this program outputs a solution to the problem for an nxn board to a text file

Created by Dietrich Geisler
Last edited:  1/28/14
'''

import sys
import select
import subprocess

def getRow(row, size):
	"""
	Requires the row and the size of the board
	Returns a string CNF expression representing the XOR of the given row
	Ex) For the call (1, 2), this would return "1 2 0\n-1 -2 0\n"
	"""

	toReturn = ""
	
	for i in range(row, row + size):
		toReturn += str(i) + " "
		
	toReturn += "0\n"
	
	for i in range (row, row + size):
		for j in range (i + 1, row + size):
			toReturn += "-" + str(i) + " -" + str(j) + " 0\n"
	
	return toReturn;

def getRank(rank, size):
	"""
	Requires the rank and the size of the board
	Returns a string CNF expression representing the XOR of the given rank
	Ex) For the call (1, 2), this would return "1 3 0\n-1 -3 0\n"
	"""
	
	toReturn = ""
	
	i = rank
	while i < (size ** 2 + 1):
		toReturn += str(i) + " "
		i += size
		
	toReturn += "0\n"
	
	i = rank
	j = rank + size
	while i < (size ** 2 + 1):
		while j < (size ** 2 + 1):
			toReturn += "-" + str(i) + " -" + str(j) + " 0\n"
			j += size
		i += size
		j = i + size
	
	return toReturn;
	
def getRightDiagonal(point, size):
	"""
	Requires an 'index' to start at and the size of the board
	Returns a string CNF representing the XOR of the diagonal extending from the given point to the lower-right of the board
	Ex) For the call (1, 2), this would return "1 4 0\n-1 -4 0\n"
	"""
	
	toReturn = ""
	
	i = point
	j = i + size + 1
	while i < (size ** 2 + 1):
		while j < (size ** 2 + 1):
			if j % size == 1:
				break
			toReturn += "-" + str(i) + " -" + str(j) + " 0\n"
			j += size + 1
		i += size + 1
		j = i + size + 1
		if i % size == 1:
				break
				
	return toReturn
	
def getLeftDiagonal(point, size):
	"""
	Requires an 'index' to start at and the size of the board
	Returns a string CNF representing the XOR of the diagonal extending from the given point to the lower-right of the board
	Ex) For the call (1, 2), this would return "1 4 0\n-1 -4 0\n"
	"""
	
	toReturn = ""
	
	i = point
	j = i + size - 1
	while i < (size ** 2 + 1):
		while j < (size ** 2 + 1):
			if j % size == 0:
				break
			toReturn += "-" + str(i) + " -" + str(j) + " 0\n"
			j += size - 1
		i += size - 1
		j = i + size - 1
		if i % size == 0:
				break
				
	return toReturn

n = sys.argv[1]
n = int(n)

if (not isinstance(n, int)):
	print("Invalid input.  Correct input is 'n-Queens.py integer' where integer is some integer");
	exit(0);
	
if n <= 0:
	print("Invalid input.  Correct input is 'n-Queens.py integer' where integer is some positive integer");
	exit(0);
	
s = "" #contains the data we need to write to our cnf file
#Put cnf data for each rank and row into s
for i in [j * n + 1 for j in range(n)]:
	s += str(getRow(i, n))
for i in range(1, n + 1):
	s += str(getRank(i, n))
	
for i in range (1, n + 1):
	s += str(getRightDiagonal(i, n))
	s += str(getLeftDiagonal(i, n))
	
for i in [j * n + 1 for j in range(1, n)]:
	s += str(getRightDiagonal(i, n))
	s += str(getLeftDiagonal(i + n - 1, n))
	
f = open("data.cnf", 'w')
f.write("p cnf " + str(n**2) + "\n")
f.write(s)

f.close()

subprocess.call("./minisat_static data.cnf sat.txt", shell = True)

f = open("sat.txt", 'r')
fo = open("output.txt", 'w')
select.select([f],[],[])
if f.readline()	== "UNSAT":
	exit(0)

results = f.readline().split()

i = 0

for token in results:
	if token[0] == '-':
		fo.write(".")
	elif token[0] != "0":
		fo.write("X")
	i += 1
	if i == n:
		fo.write("\n")
		i = 0