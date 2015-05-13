#!/usr/bin/env python3
from math import log10, ceil

def read_number_strings():
	with open("Input.txt") as input_file:
		return [line.strip() for line in input_file]
		
def error_reserve(number_of_summands):
	return int(ceil(log10(number_of_summands) + 1)) # 1 = log10(9.999...)
	
def strip(strings, length):
	return [s[:length + error_reserve(len(strings))] for s in strings]

def main():
	length = 10
	summ = sum(int(s) for s in strip(read_number_strings(), length))
	print(str(summ)[:length])


main()
