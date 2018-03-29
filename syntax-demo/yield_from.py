#!/usr/bin/env python
# -*- coding: utf-8 -*-
def lazy_range(up_to):
    """Generator to return the sequence of integers from 0 to up_to, exclusive."""
    index = 0
    def gratuitous_refactor():
        nonlocal index
        while index < up_to:
            yield index
            index += 1
    yield from gratuitous_refactor()

def bottom():
    # Returning the yield lets the value that goes up the call stack to come right back down.
    return (yield 42)

def middle():
    return (yield from bottom())

def top():
    return (yield from middle())



if __name__ == '__main__':
    for x in lazy_range(5):
        print(x)

    print('-- Get the generator --')
    gen = top()
    value = next(gen)
    print(value)
    try:
        value = gen.send(value*2)
    except StopIteration as exc:
        print('exception: StopIteration: ', exc)
        value = exc.value
    print(value)

