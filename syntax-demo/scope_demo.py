#!/usr/bin/env python
# -*- coding: utf-8 -*-
#var1 = 'hello 世界'
def func1():
    print('func1', var1)


name = 'foo man'
def f1():
    print(name)
def f2():
    name='eric'
    f1()

if __name__ == '__main__':
    var1 = 'hello 中国'
    name = 'foo woman'
    print(var1)
    func1()
    print('-'*10)
    f2()


