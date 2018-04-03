#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
timedalte 是datetime中的一个对象，该对象表示两个时间的差值
构造函数：datetime.timedelta(days=0, seconds=0,  milliseconds=0, microseconds=0, minutes=0, hours=0, weeks=0)
其中参数都是可选，默认值为0
'''
from datetime import date,datetime, timedelta
print(timedelta.max)
print(timedelta(days = 1, hours=23,minutes=59,seconds=59,milliseconds=997,microseconds=998))
print(timedelta.min)
print(timedelta.resolution)
print(timedelta(1))
print(timedelta(1).total_seconds())
now = datetime.now()
nextday = now + timedelta(days=1)
yesterday = now + timedelta(days=-1)
print(yesterday,now,nextday)


