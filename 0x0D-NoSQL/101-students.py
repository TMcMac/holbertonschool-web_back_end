#!/usr/bin/env python3
""" MongoDBpractice"""


def top_students(mongo_collection):
    """
    a Python function that returns all
    students sorted by average score
    """
    average_score = mongo_collection.aggregate([
        {'$unwind': {'path': '$topics'}},
        {'$group': {'_id': '$_id',
                    'name': {'$first': '$name'},
                    'averageScore': {'$avg': '$topics.score'}}},
        {'$sort': {'averageScore': -1}}
    ])

    return average_score
