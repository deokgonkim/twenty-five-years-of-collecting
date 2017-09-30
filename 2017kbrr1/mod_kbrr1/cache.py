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
