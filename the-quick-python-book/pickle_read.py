#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
将数据结构保存到文件，可再读入
'''
import pickle, pprint
file = open("state.dump", 'rb')
str1 = pickle.load(file)
d = pickle.load(file)
lst = pickle.load(file)
file.close()
print(str1,d,lst)
pprint.pprint(lst)
print('done')

