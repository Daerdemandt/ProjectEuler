#!/usr/bin/env python3
from functools import reduce
from operator import mul

def read_digits():
	with open("Input.txt") as input_file:
		return (int(i) for i in list(''.join(line.strip() for line in input_file)))

def main():
	depth = 13
	digits = list(read_digits())
	def get_product(index):
		return reduce(mul, digits[index: index + depth])
	print(max(get_product(i) for i in range(len(digits) - depth + 1)))
		
main()
