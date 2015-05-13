#!/usr/bin/env python3
from math import log10, ceil

def read_number_strings():
	with open("Input.txt") as input_file:
		return [int(line.strip()) for line in input_file]

def main():
	length = 10
	summ = sum(int(s) for s in read_number_strings())
	print(str(summ)[:length])

main()
