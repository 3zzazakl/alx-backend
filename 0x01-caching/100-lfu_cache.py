#!/usr/bin/python3
"""summary_line

Keyword arguments:
argument -- description
Return: return_description
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
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
        self.freq_map = {}
        self.order_map = {}

    def put(self, key, item):
        """summary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.freq_map[key] += 1
            self.order_map[self.freq_map[key]].append(key)
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            self._evict_lfu_item()

        self.cache_data[key] = item
        self.freq_map[key] = 1
        if 1 not in self.order_map:
            self.order_map[1] = []
        self.order_map[1].append(key)

    def get(self, key):
        """summary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        if key is None or key not in self.cache_data:
            return None

        self.freq_map[key] += 1
        self.order_map[self.freq_map[key]].append(key)
        return self.cache_data[key]

    def _evict_lfu_item(self):
        """summary_line

        Keyword arguments:
        argument -- description
        Return: return_description
        """
        min_freq = min(self.freq_map.values())
        lfu_keys = self.order_map[min_freq]
        key_to_evict = lfu_keys.pop()

        del self.cache_data[key_to_evict]
        del self.freq_map[key_to_evict]

        print(f"DISCARD: {key_to_evict}")
