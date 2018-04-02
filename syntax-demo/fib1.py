#!/usr/bin/env python
# -*- coding: utf-8 -*-
def fib(n):
    index = 0
    a = 0
    b = 1
    while index < n:
        yield b
        a, b = b, a+b
        index += 1

print('-'*10 + 'test yield fib' + '-'*10)
for f in fib(20):
    print(f)

