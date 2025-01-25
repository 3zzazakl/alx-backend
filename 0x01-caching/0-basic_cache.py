#!/usr/bin/env python3
"""summary_line

Keyword arguments:
argument -- description
Return: return_description
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """summary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    def put(self, key, item):
        """summary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """summary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
