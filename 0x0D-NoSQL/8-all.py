#!/usr/bin/env python3
"""Learning some MongoDb with pymongo"""


def list_all(mongo_collection):
    """ Get all items in a collection
    if there are any, if not return
    an empty list
    """
    return mongo_collection.find() or []


if __name__ == '__main__':
    list_all(mongo_collection)
