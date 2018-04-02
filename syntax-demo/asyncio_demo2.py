#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import asyncio

now = lambda : time.time()

async def do_some_work(x):
    print("Waiting: ", x)
    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)

start = now()
coroutine = do_some_work(2)

loop = asyncio.get_event_loop()
#task = asyncio.ensure_future(coroutine)
task = loop.create_task(coroutine)
print(task)
# Blocking call which return when the do_some_work() coroutinme is done.
#loop.run_until_complete(coroutine)
loop.run_until_complete(task)
print(task)
print(isinstance(task,asyncio.Future))

print('Task ret: {}'.format(task.result()))
print('TIME:', now()-start)

