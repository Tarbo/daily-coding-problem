"""
@author: Okwudili Ezeme
@date: 2019-02-12
This problem was asked by Google.

Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:

set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item, then it should also remove the least recently used item.
get(key): gets the value at key. If no such key exists, return null.
Each operation should run in O(1) time.
"""
from collections import OrderedDict


class LRU:
    "LRU cache implementation using O(1) time complexity"

    def __init__(self, size):
        self.size = size
        self.cache = OrderedDict()

    def set(self, key, value):
        try:
            _ = self.cache[key]
            self.cache.move_to_end(key)
        except KeyError:
            if len(self.cache) >= self.size:
                _, _ = self.cache.popitem(last=False)
            self.cache[key] = value

    def get(self, key):
        try:
            val = self.cache.pop(key)
            self.cache[key] = val
            return val
        except KeyError:
            return None


if __name__ == "__main__":
    lru = LRU(5)
    lru.set('score', 10)
    print(lru.get('scor'))
