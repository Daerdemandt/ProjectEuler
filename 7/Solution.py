#!/usr/bin/env python3
from itertools import islice

def primes():
	if hasattr(primes, "cache"):
		precounted_primes = primes.cache
	else:
		precounted_primes = []
		with open("Primes.txt") as pfile:
			precounted_primes = [int(line.strip()) for line in pfile]
		primes.cache = precounted_primes
	yield from precounted_primes

def main():
	index = 10001
	print(list(islice(primes(), index-1, index))[0])
	
main()
