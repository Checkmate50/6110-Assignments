"""
Sudoku Problem Solver
Created by Dietrich Geisler
Python version 2.7
3/4/2015
"""

from z3 import *
import sys
import string

def fileParser(fileName):
	"""
	Takes a fileName which links to a text file containing sudoku data
	Note that there are no restrictions on file extension
	Returns a 2-dimensional array containing all the known data for this sudoku puzzle
	"""
	
	f = open(fileName, 'r')
	length = len(string.split(f.readline()))
	f.seek(0)
	data = [[0]*length for i in range(length)]	#Get NxN array, where N is the size of the sudoku puzzle
	
	j = 0
	for line in f:
		i = 0
		splitResults = string.split(line)
		for char in splitResults:
			data[j][i] = char
			i += 1
		j += 1
		
	f.close()
			
	return data, length
	
data, length = fileParser(sys.argv[1])

for line in data:
	for item in line:
		print(str(item)),
	print("")

s = Solver()
grid = [ [ Int("grid_%s_%s" % (i+1, j+1)) for j in range(length) ] for i in range(length) ]

for i in range(length):
	for j in range(length):
		if data[j][i] != '.':
			s.add(grid[j][i] == Int(data[j][i]))

for i in range(length):
	for j in range(i + 1, length):
		if data[j][i] != '.':
			s.add(grid[j][i] == Int(data[j][i]))
			
print(s)			
s.check()
print(s.model())



