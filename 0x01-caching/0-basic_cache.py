#!/usr/bin/env python3
""" Basic dictionary"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache
    """
    def put(self, key, item):
        """ assign to the dictionary """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ get value """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
