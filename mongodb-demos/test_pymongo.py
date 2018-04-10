#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from: http://api.mongodb.com/python/current/tutorial.html
# ref:  https://docs.mongodb.com/ecosystem/drivers/python/

import pymongo
import datetime
from pymongo import MongoClient
import pprint
from bson.objectid import ObjectId

client = MongoClient('localhost',32768)
db = client.tutorial
post = {"author": "Mike",
        "text": "我的中文post",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}
posts = db.posts
# 插入
post_id = posts.insert_one(post).inserted_id
print('post_id', post_id)
# print('collection_names', db.collections_names(include_system_collections=False)) #ERROR

# 读取
pprint.pprint(posts.find_one())
pprint.pprint(posts.find_one({'author':'Mike'}))
pprint.pprint(posts.find_one({'_id':'5acc6c102cbdfd15d6bafa8b'})) # None
pprint.pprint(posts.find_one({'_id':ObjectId('5acc6c102cbdfd15d6bafa8b')})) # Found
pprint.pprint(posts.find_one({'_id': post_id}))

# 批量插入
new_posts = [{"author": "Mike",
     "text": "Another post!",
     "tags": ["bulk", "insert"],
     "date": datetime.datetime(2009, 11, 12, 11, 14)},
    {"author": "Eliot",
     "title": "MongoDB is fun",
     "text": "and pretty easy too!",
     "date": datetime.datetime(2009, 11, 10, 10, 45)}]
result = posts.insert_many(new_posts)
pprint.pprint(result.inserted_ids)

for post in posts.find():
    pprint.pprint(post)

# 查找数量
print('post count:',posts.count())
print('post count:',posts.find({'author':'Mike'}).count())

# Range Queries
print('-'* 10)
d = datetime.datetime(2009,11,12,12)
for post in posts.find({'date': {'$lt':d}}):
    pprint.pprint(post)

# Indexing
result = db.profiles.create_index([('user_id', pymongo.ASCENDING)], unique=True)
pprint.pprint(sorted(list(db.profiles.index_information())))

user_profiles = [
    {'user_id': 214, 'name': 'Luke'},
    {'user_id': 215, 'name': 'Ziltoid'}]
result = db.profiles.insert_many(user_profiles)
pprint.pprint(result.inserted_ids)

