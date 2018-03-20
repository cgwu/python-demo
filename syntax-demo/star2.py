#!/usr/bin/env python
def foo(x, *args):
    print(x)
    print(args)

def  foo2(x, y=1, *args):
    print(x)
    print(y)
    print(args)

def foo3(x,y,z):
    print(x)
    print(y)
    print(z)

def foo4(x, **kwargs):
    print(x)
    print(kwargs)

def foo5(x, *args, **kwargs):
    print(x)
    print(args)
    print(kwargs)

if __name__ == '__main__':
    foo(1,2,3,4,5)
    foo2(1,2,3,4,5)
    foo3(*(1,2,3))
    print('**kwargs')
    foo4(1, y=1,a=2,b=3,c=4)
    print('*args, **kwargs')
    foo5(1, 2,3,4, y=1,a=2,b=3,c=4)
    print('foo3 **kwargs')
    foo3(**{'z':3, 'y':2, 'x':1})


