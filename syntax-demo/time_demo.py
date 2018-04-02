#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
tm = time.time()
print("time.time(): %f" % tm)
print("localtime:", time.localtime(tm))
print("asctime:", time.asctime(time.localtime(tm)))
print("strftime:", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(tm)))

