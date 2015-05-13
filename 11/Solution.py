#!/usr/bin/env python3
from functools import reduce
from operator import mul

def read_grid():
	with open("Input.txt") as input_file:
		return [[int(num) for num in line.split()] for line in input_file]

def max_horisontal(grid, depth):
	row_length = len(grid[0])
	def rowmax(i):
		def get_product(index):
			return reduce(mul, grid[i][index: index + depth])
		return max(get_product(i) for i in range(row_length - depth + 1))
	return max(rowmax(i) for i in range(len(grid)))

def transpose(grid):
	return [list(x) for x in zip(*grid)]

def tilt(grid, direction):
	l = len(grid)
	if direction == 'Right':
		return [(l - i - 1) * [0] + grid[i] + [0] * i for i in range(l)]
	if direction == 'Left':
		return [i * [0] + grid[i] + [0] * (l - i - 1) for i in range(l)]
		
def rcurry(func, param):
	return lambda x: func(x, param)

def directional_maxes(grid, depth):
	maxes = {}
	t, tr, tl, = transpose, rcurry(tilt, 'Right'), rcurry(tilt, 'Left')
	measure = rcurry(max_horisontal, depth)
	maxes['Horisontal'] = measure(grid)
	maxes['Vertical'] = measure(t(grid))
	maxes['Diagonal1'] = measure(t(tl(grid)))
	maxes['Diagonal2'] = measure(t(tr(grid)))
	return maxes

def main():
	grid = read_grid()
	depth = 4
	print(max(directional_maxes(grid, depth).values()))

main()
