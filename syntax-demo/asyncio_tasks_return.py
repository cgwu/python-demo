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
    #return await asyncio.gather(*tasks)
    return await asyncio.wait(tasks)

start = now()
loop = asyncio.get_event_loop()
#results = loop.run_until_complete(main())
#for result in results:
#    print('Task ret:', result)
done, pending = loop.run_until_complete(main())
for task in done:
    print('Task ret wait: ', task.result())
print('TIME:', now()-start)

