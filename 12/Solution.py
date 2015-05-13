#!/usr/bin/env python3
from itertools import count, accumulate, dropwhile
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
	if n == 1:
		yield (1, 0)
		raise StopIteration
	if n < 2:
		raise StopIteration
	number = n
	for factor in primes():
		count = 0
		while number % factor == 0:
			count += 1
			number = number // factor
		if count > 0:
			yield (factor, count)
			if number == 1:
				raise StopIteration
	print("Not enough primes!")
	
def triangle_numbers():
	yield from accumulate(count(1))

def divisorcount(n):
	return reduce(mul, (f[1] + 1 for f in prime_factors(n)))
	
def main():
	divisors_number = 500
	def few_divisors(n):
		return divisorcount(n) <= divisors_number
	for t in dropwhile(few_divisors, triangle_numbers()):
		print(t)
		break
		
main()
