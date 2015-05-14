#!/usr/bin/env python3

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

def divisors(n):
	pf = tuple(prime_factors(n))
	def gen_divisors(max_factors):
		if max_factors == 0:
			yield 1
			raise StopIteration
		factor = pf[max_factors - 1]
		for div in gen_divisors(max_factors - 1):
			for i in range(factor[1] + 1):
				yield (factor[0] ** i) * div
	yield from (div for div in gen_divisors(len(pf)) if div < n)

def dynamic(func):
	cache = {}
	def dynamic_func(*args):
		if args not in cache:
			cache[args] = func(*args)
		return cache[args]
	return dynamic_func

@dynamic
def divisors_sum(n):
	return sum(divisors(n))

def is_amicable(n):
	return n == divisors_sum(divisors_sum(n)) and not is_perfect(n)

def is_perfect(n):
	return n == divisors_sum(n)

def nrange(n):
	yield from range(1, n + 1)

def main():
	limit = 10000
	print(sum(n for n in nrange(limit) if is_amicable(n)))


main()

