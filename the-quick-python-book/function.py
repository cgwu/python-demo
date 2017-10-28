#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def funct1(x, y, z):
    value = x + 2 * y + z ** 2
    return value if value > 0 else 0

print(funct1(3,4,2))
print(funct1(-3,-4,2))


