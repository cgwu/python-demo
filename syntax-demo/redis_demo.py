#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
pip install redis
参考:
https://www.cnblogs.com/wang-yc/p/5693288.html
redis是一个key-value存储系统，和Memcache类似，它支持存储的value类型相对更多，包括string(字符串)，list(链表)，set(集合)，zset(有序集合)，hash(哈希类型)。这些数据类型都支持push/pop，add/remove及取交集并集和差集及更丰富的操作，而且这些操作都是原子性的。在次基础上，redis支持各种不同方式的排序，与memcached一样，为了保证效率，数据都是缓冲在内存中。区别是redis会周期性的把更新的数据写入磁盘或把修改操作写入追加的记录文件，并且在此基础上实现了master-slave(主从)同步。
　　备注：默认redis有16个数据库，即db0~db15， 一般存取数据如果不指定库的话，默认都是存在db0中。

redis提供两个类Redis和StrictRedis, StrictRedis用于实现大部分官方的命令，Redis是StrictRedis的子类，用于向后兼用旧版本。
"""
import redis
#r = redis.Redis(host='192.168.1.5', port=6379)
#r = redis.StrictRedis(host='192.168.1.5', port=6379, db=0)
r = redis.StrictRedis(host='192.168.1.5', port=6379, db=0, decode_responses=True)
r.set('foo','hello world bar中国')
ret = r.get('foo')
print(ret, type(ret))

