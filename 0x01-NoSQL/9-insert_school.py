#!/usr/bin/env
'''task 9
'''


def insert_school(mongo_collection, **kwargs):
    '''inserting a kwarg into a collection
    '''
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
