#!/usr/bin/env python3
from calendar import weekday, day_name

def count_sundays(year):
	sunday = list(day_name).index('Sunday')
	return sum(weekday(year, month, 1) == sunday for month in range(1, 13))

def main():
	print(sum(count_sundays(year) for year in range(1901, 2001)))

main()

