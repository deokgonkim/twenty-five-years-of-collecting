#! -*- coding=utf-8 -*-

import re


class CityNameValidator:
    def __init__(self, max_length = 20, re_pattern = r'^[a-zA-Z]*$'):
        self.max_length = max_length
        self.re_pattern = re_pattern

    def validate(self, city_name):
        if len(city_name) > self.max_length:
            raise BaseException("City name exceeds maximum length(%d)" % self.max_length)
        sr = re.search(re.compile(self.re_pattern), city_name)
        if not sr: raise BaseException("City name doesn't match rule.")
        return True

class CityStore:
    def __init__(self):
        self.cities = {}

    def insert(self, name, obj = None):
        self.cities[name] = obj if obj else name

    def select(self, name):
        if self.cities.has_key(name):
            return self.cities[name]

    def update(self, name, obj = None):
        self.cities[name] = obj if obj else name

    def delete(self, name):
        self.cities.pop(name)

class CitiStoreLRUCached:
    def __init__(self, store):
        """Must provide valid store.
        """
        self.metric_processing_time = 0
        self.metric_hit_count = 0
        self.metric_miss_count = 0
        self.metric_hit_time = 1
        self.metric_miss_time = 5

        self.cache_size = 0

        self.cache = []

        self.backend = store

    def set_cache_size(self, cache_size):
        self.cache_size = cache_size

    def get_city(self, name):
        pass

    def _compute_metric(self, is_hit):
        pass
