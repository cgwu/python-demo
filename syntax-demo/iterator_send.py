#!/usr/bin/env python
# -*- coding: utf-8 -*-

def jumping_range(up_to):
    """
    Generator for the sequence of integers from 0 to up_to, exclusive.
    Sending a value into the generator will shift the sequence by that amount.
    """
    index = 0
    while index < up_to:
        jump = yield index
        if jump is None:
            jump = 1
        index += jump

if __name__ == '__main__':
    iterator = jumping_range(10)
    print(next(iterator)) # 0
    print(next(iterator)) # 1
    print('send',iterator.send(2)) # 3, iter前进2个位置，返回值为上一位置值
    print(next(iterator)) # 4
    print(next(iterator)) # 5
    print('send',iterator.send(-1)) # 4, iter后退一个位置
    for x in iterator: # 5,6,7,8,9
        print(x)

