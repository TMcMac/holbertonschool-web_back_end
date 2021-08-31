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
        key = str(uuid.uuid(4))
        self._redis.set(key, data)
        return key
