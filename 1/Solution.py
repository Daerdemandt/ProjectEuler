#!/usr/bin/env python3

def multiples_of(numbers):
	def is_multiple(number):
		return any(number % divisor == 0 for divisor in numbers)
	value = 1
	while True:
		if is_multiple(value):
			yield value
		value += 1

def main():
	multiples_sum = 0
	for number in multiples_of((3,5)):
		if number >= 1000:
			break
		multiples_sum += number
	print(multiples_sum)
	
main()
