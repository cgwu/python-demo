#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tornado import gen
from tornado.ioloop import IOLoop

@gen.coroutine
def divide(x,y):
    return x/y

@gen.coroutine
def good_call():
    yield divide(1,0)

async def async_divide(x,y):
    await (x / y)

#IOLoop.current().spawn_callback(async_divide,1,0)
#IOLoop.current().run_sync(lambda: divide(1,1))
IOLoop.current().run_sync(lambda: async_divide(1,1))

