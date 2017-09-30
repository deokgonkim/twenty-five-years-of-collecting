#! -*- coding=utf-8 -*-

cacheSize = input("Cache size? ")
cities = input("Cities(Valid Python Expression) : ")

assert 0 <= cacheSize <= 30, "Cache Size is out of range(0-30)"

assert len(cities) < 100000, "City count exceeds limit(100,000)"
