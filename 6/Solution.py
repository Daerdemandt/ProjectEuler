#!/usr/bin/env python3

def nrange(n):
	yield from range(1, n + 1)

def main():
	limit = 100
	squares_sum = sum(n*n for n in nrange(limit))
	sum_squared = sum(nrange(limit)) ** 2
	print(sum_squared - squares_sum)
	
main()
