#! -*- coding=utf-8 -*-

import re
from datetime import datetime


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


class CityStoreLRUCached:
    """원래는, CityStore를 확장해서, 대체 가능해야 할텐데, 우선은,
    따로 사용하는 것으로 구현해 본다.
    """
    def __init__(self, store):
        """Must provide valid store.
        """
        self.metric_processing_time = 0
        self.metric_hit_count = 0
        self.metric_miss_count = 0
        self.metric_hit_time = 1
        self.metric_miss_time = 5

        self.cache_size = 0

        """
        self.cache
          : key - 도시명, value - 도시객체(문제상 도시명과 동일)
        self.cache_lac
          : key - 도시명, value - 최종 접근 시간 ( datetime.now().isoformat() )
        self.cache_hit
          : key - 도시명, value - hit count
        """
        self.cache = {}
        self.cache_lac = {}
        self.cache_hit = {}

        self.store = store

    def set_cache_size(self, cache_size):
        self.cache_size = cache_size

    def get_city(self, name):
        """먼저 캐시에서 name이 있는지 확인하고, 있으면, lac, hit 업데이트하고 반환한다.
        캐시에 name이 없으면, store에서 꺼내고, _put_city한다.
        """

        hit = self.cache.has_key(name)

        if hit:
            city = self.cache[name]
            self.cache_lac[name] = datetime.now().isoformat()
            self.cache_hit[name] += 1
        else:
            city = self.store.select(name)
            if not city: raise BaseException("There is no such item")
            self._put_city(name, city)

        self._compute_metric(hit)
        return city

    def _put_city(self, name, obj):
        """LRU 정책에 따라, 가장 덜 쓴 객체를 제거하고?
        새로 들어온 객체를 캐시에 넣는다?
        (LRU 스펙을 읽어보지도 않고 구현한다.)
        """
        if self.cache_size == 0:
            return None
        if len(self.cache.keys()) == self.cache_size:
            def cmp_lac(item1, item2):
                return cmp(item1[1], item2[1])
            cache_sorted_by_lac = sorted(self.cache_lac.items(), cmp = cmp_lac)
            tobe_removed, city = cache_sorted_by_lac[0]

            self.cache.pop(tobe_removed)
            self.cache_lac.pop(tobe_removed)
            self.cache_hit.pop(tobe_removed)

        self.cache[name] = obj
        self.cache_lac[name] = datetime.now().isoformat()
        self.cache_hit[name] = 1

    def _compute_metric(self, is_hit):
        pass
