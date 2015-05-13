#!/usr/bin/env python3

def dynamic(func):
	cache = {}
	def dynamic_func(*args):
		if args not in cache:
			cache[args] = func(*args)
		return cache[args]
	return dynamic_func

@dynamic
def compositions(a, b): # a, b - numbers of objects of 2 types
	if a > b:
		return compositions(b, a)
	if a == 0:
		return 1
	return compositions(a - 1, b) + compositions(a, b - 1)
	
def main():
	moves_x, moves_y = 20, 20
	print(compositions(moves_x, moves_y))

main()
