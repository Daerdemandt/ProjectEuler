#!/usr/bin/env python3

def read_triangle():
	with open("Input.txt") as tfile:
		return [[int(n) for n in line.strip().split()] for line in tfile]

triangle = read_triangle()

def dynamic(func):
	cache = {}
	def dynamic_func(*args):
		if args not in cache:
			cache[args] = func(*args)
		return cache[args]
	return dynamic_func

@dynamic
def max_path(row, index):
	assert row < len(triangle) and index < len(triangle[row])
	if row + 1 == len(triangle):
		return triangle[row][index]
	return triangle[row][index] + max(max_path(row + 1, index), max_path(row + 1, index + 1))

def main():
	print(max_path(0,0))

main()
