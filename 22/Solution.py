#!/usr/bin/env python3
from string import ascii_uppercase

def read_names():
	with open("Input.txt") as input_file:
		return input_file.readline().strip().replace('"', '').split(',')

def name_score(name):
	def letter_score(char):
		return 1 + ascii_uppercase.index(char)
	return sum(letter_score(char) for char in name.upper())

def main():
	sorted_names = sorted(read_names())
	print(sum((i + 1) * name_score(sorted_names[i]) for i in range(len(sorted_names))) )

main()	
