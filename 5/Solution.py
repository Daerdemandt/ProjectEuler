#!/usr/bin/env python3
from functools import reduce
from operator import mul

def primes():
	if hasattr(primes, "cache"):
		precounted_primes = primes.cache
	else:
		precounted_primes = []
		with open("Primes.txt") as pfile:
			precounted_primes = [int(line.strip()) for line in pfile]
		primes.cache = precounted_primes
	yield from precounted_primes

def prime_factors(n):
	if n < 2:
		raise StopIteration
	number = n
	for factor in primes():
		count = 0
		while number % factor == 0:
			count += 1
			number = number // factor
		yield (factor, count)
		if count > 0:
			if number == 1:
				raise StopIteration
	print("Not enough primes!")

def gcd(a,b):
	gcd_factors_tuples = (min(z[0], z[1], key=lambda x: x[1]) for z in zip(prime_factors(a), prime_factors(b)))
	gcd_factors = (f[0] ** f[1] for f in gcd_factors_tuples)
	return reduce(mul, gcd_factors)

def lcs(numbers):
	if len(numbers) == 1:
		return numbers[0]
	slicer = len(numbers) // 2
	a, b = lcs(numbers[:slicer]), lcs(numbers[slicer:])
	return a * b // gcd(a,b)

	
def main():
	number = 20
	print(lcs(range(2, 1 + number)))
	
main()
