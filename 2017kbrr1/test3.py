#! -*- coding=utf-8 -*-

"""
Sample data and result
3 	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"] 	50
3 	["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"] 	21
2 	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"] 	60
5 	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"] 	52
2 	["Jeju", "Pangyo", "NewYork", "newyork"] 	16
0 	["Jeju", "Pangyo", "Seoul", "NewYork", "LA"] 	25
"""

from mod_kbrr1.cache import *

store = CityStore()
cache = CityStoreLRUCached(store)

cacheSize = input("Cache size? ")
cities = input("Cities(Valid Python Expression) : ")

assert 0 <= cacheSize <= 30, "Cache Size is out of range(0-30)"

assert len(cities) < 100000, "City count exceeds limit(100,000)"

for city in cities:
    store.insert(city)

cache.set_cache_size(cacheSize)

for city in cities:
    cache.get_city(city)

print(cache.get_metric())
