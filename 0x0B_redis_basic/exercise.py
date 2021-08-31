#!/usr/bin/env python3
""" Learning some Redis """
from functools import wraps
import redis
from typing import Callable, Optional, Union
import uuid


def count_calls(method: Callable) -> Callable:
    """Count number of times functions called"""
    @wraps(method)
    def count_calls_wrapper(self, *args) -> bytes:
        """Counts calls wrapped function makes"""
        self._redis.incr(method.__qualname__)
        return method(self, *args)

    return count_calls_wrapper


def call_history(method: Callable) -> Callable:
    """Store history of inputs/outputs for a function"""
    inputs = f"{method.__qualname__}:inputs"
    outputs = f"{method.__qualname__}:outputs"

    @wraps(method)
    def call_history_wrapper(self, *args) -> bytes:
        """Stores the history of inputs and outputs for a function"""
        self._redis.rpush(inputs, str(args))
        out = method(self, *args)
        self._redis.rpush(outputs, out)

        return out

    return call_history_wrapper


def replay(method: Callable) -> str:
    """Display the history of calls of a particular function"""
    name = method.__qualname__
    inputs = f"{name}:inputs"
    outputs = f"{name}:outputs"
    r = redis.Redis()
    data = r.get(name).decode('utf-8')
    input_list = r.lrange(inputs, 0, -1)
    output_list = r.lrange(outputs, 0, -1)

    print(f"{name} was called {data} times:")

    for ins, outs in zip(input_list, output_list):
        print(f"{name}(*{ins.decode('utf-8')}) -> {outs.decode('utf-8')}")


class Cache():
    """Cache class"""

    def __init__(self):
        """Set up cache obj"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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
