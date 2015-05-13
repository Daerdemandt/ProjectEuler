#!/usr/bin/env python3
from itertools import takewhile

def fibonacci_numbers():
	previous = 0
	result = 1
	while True:
		previous, result = result, previous + result
		yield result

def even_fibonacci_numbers():
	for number in fibonacci_numbers():
		if number % 2 == 0:
			yield number

def sumwhile(predicate, seq):
	return sum(takewhile(predicate, seq))
			
def main():
	limit = 4 * 10**6
	print(sumwhile(lambda x: x < limit, even_fibonacci_numbers()))
	
main()
