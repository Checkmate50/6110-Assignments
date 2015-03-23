"""
Sudoku Problem Solver
Created by Dietrich Geisler
Python version 2.7
3/4/2015
"""

from z3 import *
import sys
import string
import math

def fileParser(fileName):
	"""
	Takes a fileName which links to a text file containing sudoku data
	Note that there are no restrictions on file extension
	Returns a 2-dimensional array containing all the known data for this sudoku puzzle
	"""
	
	f = open(fileName, 'r')
	length = len(string.split(f.readline()))
	if int(math.sqrt(length) + 0.5)**2 != length:
		print("Sudoku grid edges must be a perfect square")
		exit(0)
	f.seek(0)
	data = [[0]*length for i in range(length)]	#Get NxN array, where N is the size of the sudoku puzzle
	
	j = 0
	for line in f:
		i = 0
		splitResults = string.split(line)
		for char in splitResults:
			if char != '.':
				data[j][i] = int(char)
			i += 1
		j += 1
		
	f.close()
			
	return data, length

toParse = ""
if len(sys.argv) == 1:
	toParse = raw_input("Please provide the name of a sudoku puzzle file: ")
else:
	toParse = sys.argv[1]
data, length = fileParser(toParse)

s = Solver()
grid = [ [ Int("grid_%s_%s" % (i+1, j+1)) for j in range(length) ] for i in range(length) ]

for i in range(length):
	for j in range(length):
		if data[j][i] != 0:
			s.add(grid[j][i] == data[j][i])
		s.add(grid[j][i] <= length, grid[j][i] > 0)

for i in range(length):
	for j in range(length):
		for k in range(j + 1, length):
			s.add(grid[j][i] != grid[k][i]) #Columns
			s.add(grid[i][j] != grid[i][k]) #Rows
			pass

sqrtl = int(math.sqrt(length))
for i in range(0, length, sqrtl):
	for j in range(0, length, sqrtl):
		for row1 in range(sqrtl):
			for col1 in range(sqrtl):
				for row2 in range(sqrtl):
					for col2 in range(sqrtl):
						if row1 != row1 or col1 != col2:
							s.add(grid[col1 + i][row1 + j] != grid[col2 + i][row2 + j]) #Inner Squares		
		
if str(s.check()) != "sat":
	print "Sudoku puzzle is not satisfiable (solvable)"
	exit(0)
	
modelValues = string.split(str(s.model()), "\n")
for value in modelValues:
	data[int(value[6]) - 1][int(value[8]) - 1] = value[12]
print("")
for line in data:
	for item in line:
		print(str(item)),
	print("")