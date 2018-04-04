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

print('url join test:', urljoin('http://www.tornadoweb.org/en/stable/guide/','../../abc.html'))
print('url join test:', urljoin('http://www.tornadoweb.org/en/stable/guide/','./efg.html'))
# 若为绝对路径，直接返回第二个参数
print('url join test:', urljoin('http://www.tornadoweb.org/en/stable/guide/','https://www.baidu.com/'))

