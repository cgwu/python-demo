#!/usr/bin/env python3
# -*- coding: utf-8 -*-
item_list = [3, "string1", 23, 14.0, "String2", 49, 64, 70]
for x in item_list:
    if not isinstance(x, int):
        continue
    if not x % 7:
        print("found an integer divisible by seven: %d" % x)
        break

