#!/usr/bin/env python3

def text_repr(n):
	if n >= 1000:
		result = text_repr(n // 1000) + ' thousand'
		if n % 1000 > 0:
			result += ' ' + text_repr(n % 1000)
		return result

	if n >= 100:
		result = text_repr(n // 100) + ' hundred'
		if n % 100 > 0:
			result += ' and ' + text_repr(n % 100)
		return result

	if n >= 20:
		result = 'zero ten twenty thirty forty fifty sixty seventy eighty ninety'.split()[n // 10]
		if n % 10 > 0:
			result += '-' + text_repr(n % 10)
		return result
	return 'zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()[n]
	
def nrange(n):
	yield from range(1, n + 1)
		
def letters(string):
	return len(string.replace(' ', '').replace('-', ''))

def main():
	limit = 1000
	print(sum(letters(text_repr(i)) for i in nrange(limit)))

main()
