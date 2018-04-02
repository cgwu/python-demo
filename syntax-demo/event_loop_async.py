#!/usr/bin/env python
# -*- coding: utf-8 -*-
from threading import Thread
import time
import asyncio

def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()

async def work_async(x):
    print('Async work {}'.format(x))
    await asyncio.sleep(x)
    print('Finished async work {}'.format(x))

start = time.time()
new_loop = asyncio.new_event_loop()
# 启动线程
t = Thread(target=start_loop, args=(new_loop,))
t.start()
print('TIME: {}'.format(time.time()-start))

asyncio.run_coroutine_threadsafe(work_async(6), new_loop)
asyncio.run_coroutine_threadsafe(work_async(3), new_loop)
print('main done')

