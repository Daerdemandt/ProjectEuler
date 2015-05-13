#!/usr/bin/env python3
from itertools import takewhile
from math import sqrt

def primes():
	if hasattr(primes, "cache"):
		precounted_primes = primes.cache
	else:
		precounted_primes = []
		with open("Primes.txt") as pfile:
			precounted_primes = [int(line.strip()) for line in pfile]
		primes.cache = precounted_primes
	yield from precounted_primes
	# And now if this was not enough:
	def check_if_prime(number):
		stop_value = int(sqrt(number))
		for prime in precounted_primes:
			if number % prime == 0:
				return False
			if prime > stop_value:
				return True
				
	candidate = precounted_primes[-1] + 2
	while True:
		if check_if_prime(candidate):
			precounted_primes.append(candidate)
			yield candidate
		candidate += 2
		

def sum_limited(seq, limit):
	return sum(takewhile(lambda x: x < limit, seq))

def main():
	limit = 2 * 10**6
	print(sum_limited(primes(), limit))

main()
