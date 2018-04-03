#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
https://blog.csdn.net/kittyboy0001/article/details/21552693
'''
from urllib.parse import urljoin, urldefrag, urlsplit
url = 'schema://net_loc/path;params?query#fragment'
pure_url, frag = urldefrag(url)
print(url)
print(pure_url)
print(frag)
ret = urlsplit(url)
print(ret,type(ret))


