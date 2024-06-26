#!/usr/bin/env python3
""" MRU caching """
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache """
    def __init__(self):
        super().__init__()
        self.history = []

    def put(self, key, item):
        """ mru """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS\
                 and key not in self.cache_data:
                print(f'DISCARD: {self.history[-1]}')
                self.cache_data.pop(self.history[-1])
                del self.history[-1]
            if key in self.history:
                del self.history[self.history.index(key)]
            self.history.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ get key value """
        if key is None or key not in self.cache_data:
            return None
        else:
            del self.history[self.history.index(key)]
            self.history.append(key)
            return self.cache_data[key]
