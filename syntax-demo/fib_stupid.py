#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import random
import threading

def fib_stupid(n):
    index = 0
    a = 0
    b = 1
    while index < n:
        sleep_cnt = yield b
        print('{2}: index {1}: let me think {0} secs'.format(sleep_cnt, index, threading.currentThread()))
        time.sleep(sleep_cnt)
        a, b = b, a+b
        index += 1

def fib_stupid_copy(n):
    print('I am copy from stupid fib')
    yield from fib_stupid(n)
    print('Copy end')

print('-'*10 + 'test yield fib' + '-'*10)
#fibs = fib_stupid(5)
fibs = fib_stupid_copy(5)
fib_res = next(fibs)
while True:
    print(threading.currentThread(), fib_res)
    try:
        fib_res = fibs.send(random.uniform(0,0.5))
    except StopIteration:
        print('Stop Interation')
        break


