#!/usr/bin/env python3

def triplets_limited(limit):
	for c in reversed(range(limit)):
		for b in range(1, c + 1):
			a = limit - c - b
			if 0 < a <= b:
				yield (a, b, c)

def is_pythagorean(a, b, c):
	return a*a + b*b == c*c

def main():
	r = [t for t in triplets_limited(1000) if is_pythagorean(*t)]
	print(r[0][0] * r[0][1] * r[0][2])	
	
main()
