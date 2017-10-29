#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pickle
file = open("state.dump", 'rb')
str1 = pickle.load(file)
d = pickle.load(file)
lst = pickle.load(file)
file.close()
print(str1,d,lst)
print('done')

