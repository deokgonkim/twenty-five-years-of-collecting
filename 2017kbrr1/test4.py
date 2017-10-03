#! -*- coding=utf-8 -*-

"""
Sample data and result
n	t	m	timetable				answer
1 	1 	5 	["08:00", "08:01", "08:02", "08:03"] 	"09:00"
2 	10 	2 	["09:10", "09:09", "08:00"] 	"09:09"
2 	1 	2 	["09:00", "09:00", "09:00", "09:00"] 	"08:59"
1 	1 	5 	["00:01", "00:01", "00:01", "00:01", "00:01"] 	"00:00"
1 	1 	1 	["23:59"] 	"09:00"
10 	60 	45 	["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"] 	"18:00"
"""

n = input("Enter count of shuttle bus? ")
t = input("Enter time interval of shuttle bus? ")
m = input("Enter vacancy count of shuttle bus? ")

timetable = input("Enter crew's arrival timetable(Valid Phthon Expression)? ")

assert 0 < n <= 10, "Shuttle Bus count exceeds limit(1~10)"
assert 0 < t <= 60, "Shuttle Bus time interval is invalid(1~60)"
assert 0 < m <= 45, "Shuttle Bus vacancy count is invalid(1~45)"

assert 0 < len(timetable) <= 2000, "Crew count is invalid(1~2000)"

from mod_kbrr1.shuttle import *

supplier = BusSupplier(5)

agency = BusAgency()
agency.set_bus_supplier(supplier)

agency.schedule_bus("09:00", 2, 1)

agency.guess_last_bus()
