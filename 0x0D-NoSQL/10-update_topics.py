#!/usr/bin/env python3
""" Practicing pymongo """


def update_topics(mongo_collection, name, topics):
    """
    Write a Python function that changes all
    topics of a school document based on the name
    """
    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})


if __name__ == '__main__':
    update_topics(mongo_collection, name, topics)
