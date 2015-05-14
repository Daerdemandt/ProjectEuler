#!/usr/bin/env python3

def digits_sum(n):
	return sum(int(d) for d in list(str(n)))

def main():
	power = 1000
	print(digits_sum(2**power))

main()
