#!/usr/bin/env python3

def is_palindrome(number):
	s = str(number)
	l = len(s)
	return all(s[i] == s[l - i - 1] for i in range(l//2))

def main():
	current_maximum = 0
	for i in range(999, 99, -1):
		min_j = max(current_maximum // i, 99)
		for j in range(999, min_j, -1):
			if is_palindrome(i * j):
				current_maximum = i * j
				break
	print(current_maximum)
	
main()
