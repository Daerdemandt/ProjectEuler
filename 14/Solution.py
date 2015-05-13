#!/usr/bin/env python3

def collatz_length(n, cache={1:1}):
	def next(n):
		if n % 2 == 0:
			return n / 2
		return 3 * n + 1
		
	if not n in cache:
		cache[n] = 1 + collatz_length(next(n))
	return cache[n]

def nrange(n):
	yield from range(1, n + 1)

def main():
	limit = 10**6
	print(max(nrange(limit), key=collatz_length))

main()
