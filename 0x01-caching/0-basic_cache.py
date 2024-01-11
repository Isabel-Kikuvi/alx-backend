#!/usr/bin/env python3
"""
A class BasicCache that inherits from BaseCaching and is a caching system
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """_BasicCache class that inherits from BaseCaching"""

    def __init__(self):
        """initializa the class"""
        super().__init__()

    def put(self, key, item):
        """adds items in the cache"""
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
