#!/usr/bin/env python3
""" Learning some pymongo """


def insert_school(mongo_collection, **kwargs):
    """
    Write a Python function that inserts a new
    document in a collection based on kwargs
    """
    return mongo_collection.insert(kwargs)


if __name__ == '__main__':
    insert_school(mongo_collection, **kwargs)
