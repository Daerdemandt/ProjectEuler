#!/usr/bin/env python3
from math import factorial

def digits_sum(n):
	return sum(int(char) for char in str(n))

def main():
	number = 100
	print(digits_sum(factorial(number)))

main()
