#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pickle
file = open("state.dump", 'wb')
str1 = "Hello中国"
pickle.dump(str1, file)
d = 3.1415
pickle.dump(d, file)
lst = [1,'hello世输送',{'key':'val',1:2}, {'a',123}, (1,3.14,'foo')]
pickle.dump(lst, file)
file.close()
print('done')

