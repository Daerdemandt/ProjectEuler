#!/usr/bin/env python3

def primes():
	precounted_primes = []
	with open("Primes.txt") as primesfile:
		precounted_primes = [int(line.strip()) for line in primesfile]
	yield from precounted_primes

def prime_factors(n):
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
	print("Not enogh primes!")
	
def main():
	number = 600851475143
	print(list(prime_factors(number))[-1][0])

main()
	
