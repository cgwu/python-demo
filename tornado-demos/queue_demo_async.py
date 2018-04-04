#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tornado import gen
from tornado.ioloop import IOLoop
from tornado.queues import Queue

q = Queue(maxsize=2)

async def consumer():
    while True:
        item = await q.get()
        try:
            print('Doing work on %s' % item)
            await gen.sleep(0.01)
        finally:
            q.task_done()
'''
In Python 3.5, `Queue` implements the async iterator protocol, so
    ``consumer()`` could be rewritten as::
versionchanged:: 4.3
       Added ``async for`` support in Python 3.5.
'''
async def consumer_async():
    async for item in q:
        try:
            print('Doing work on %s' % item)
            yield gen.sleep(0.01)
        finally:
            q.task_done()

async def producer():
    for item in range(5):
        await q.put(item)
        print('Put %s' % item)

async def main():
    # Start consumer without waiting (since it never finishes).
    IOLoop.current().spawn_callback(consumer)
    #IOLoop.current().spawn_callback(consumer_async) # FAIL：不起作用
    await producer() # wait for producer to put all tasks
    await q.join()   # wait for consumer to finish all taks
    print('Done')

if __name__ == '__main__':
    try:
        IOLoop.current().run_sync(main)
    except:
        print('Except')

