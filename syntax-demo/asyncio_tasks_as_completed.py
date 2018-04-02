#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import asyncio

now = lambda : time.time()

async def do_some_work(x):
    print("Waiting: ", x)
    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)

async def main():
    coroutine1 = do_some_work(1)
    coroutine2 = do_some_work(2)
    coroutine4 = do_some_work(4)

    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine4),
    ]
    # 一旦有任务完成，即输出，而不是等所有完成。
    for task in asyncio.as_completed(tasks):
        result = await task
        print('Task ret as_completed: ', result)

start = now()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
print('TIME:', now()-start)

