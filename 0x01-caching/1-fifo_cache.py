#!/usr/bin/env python3
""" FIFO caching """
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ fifo add"""
        if key is not None and item is not None:
            self.cache_data.update({key: item})
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                top = list(self.cache_data.keys())[0]
                del self.cache_data[top]
                print(f'DISCARD: {top}')

    def get(self, key):
        """ return the value of key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
