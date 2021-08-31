#!/usr/bin/env python3
""" Learning some Redis """
import redis
from typing import Callable, Optional, Union
import uuid


class Cache():
    """Cache class"""

    def __init__(self):
        """Set up cache obj"""
        self._redis = redis.Redis()
        self._redis.flushdb()


    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store the input data in
        Redis using the random key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key


    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """get data based on key, return data as original type using fn"""
        if fn:
            value = self._redis.get(key)
            return fn(value)
        return self._redis.get(key)


    def get_str(self, key: str) -> str:
        """Cast the key to str"""
        return self.get(key, str)


    def get_int(self, key: str) -> int:
        """Cast the key to int"""
        return self.get(key, int)
