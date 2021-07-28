#!/usr/bin/env python3
"""
Create a class LFUCache that inherits from BaseCaching
and is a caching system:

* You must use self.cache_data - dictionary from the parent
  class BaseCaching
    - You can overload def __init__(self): but don’t forget
      to call the parent init: super().__init__()

* def put(self, key, item):
    - Must assign to the dictionary self.cache_data the item value
      for the key key.
    - If key or item is None, this method should not do anything.
    - If the number of items in self.cache_data is higher that
      BaseCaching.MAX_ITEMS:
          + you must discard  least frequenty used item (LFU algorithm)
          + you must print DISCARD: with the key discarded and
            following by a new line

* def get(self, key):
    - Must return the value in self.cache_data linked to key.
    - If key is None or if the key doesn’t exist in self.cache_data,
      return None.
"""
from base_caching import BaseCaching
from datetime import datetime


class LFUCache(BaseCaching):
    """
    This class will inherit self.cache_data from BaseCashing
    """
    def __init__(self):
        """
        Init from BaseCaching
        """
        super().__init__()
        self.cacheDict = {}

    def put(self, key, item):
        """
        Adds key value pairs to self.cache_data
        """
        if key is not None and item is not None:
            keyList = list(self.cache_data)[0:]
            if key in keyList:
                del self.cache_data[key]
                keyList.remove(key)
            if (len(keyList) + 1) > BaseCaching.MAX_ITEMS:
                lfu = min(self.cacheDict.values())
                for k, v in self.cacheDict.items():
                    if v is lfu:
                        remove = k
                self.cacheDict.pop(k)
                print("DISCARD: " + remove)
                del self.cache_data[remove]
            self.cache_data[key] = item
            keyList.append(key)
            self.cacheCache(key)

        else:
            pass

    def get(self, key):
        """
        Retrieves items from self.cache_data by key
        """
        keyList = list(self.cache_data)[0:]
        if key in keyList:
            self.put(key, self.cache_data[key])
            return self.cache_data[key]
        else:
            pass

    def cacheCache(self, key):
        """
        Maintains a dict of keys and their # of uses
        to check access for recently used
        """

        if key not in self.cacheDict.keys():
            self.cacheDict[key] = 1
        else:
            for k, v in self.cacheDict.items():
                if k is key:
                    self.cacheDict[k] = v + 1