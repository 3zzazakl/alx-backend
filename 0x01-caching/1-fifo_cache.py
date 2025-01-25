#!/usr/bin/env python3
"""summary_line

Keyword arguments:
argument -- description
Return: return_description
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """summary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    def __init__(self):
        """summary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """summary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.queue.remove(key)
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    first = self.queue.pop(0)
                    del self.cache_data[first]
                    print("DISCARDING {}".format(first))
                self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """summary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
