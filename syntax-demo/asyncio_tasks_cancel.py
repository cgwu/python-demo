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
coroutine1 = do_some_work(1)
coroutine2 = do_some_work(2)
coroutine4 = do_some_work(4)

tasks = [
    asyncio.ensure_future(coroutine1),
    asyncio.ensure_future(coroutine2),
    asyncio.ensure_future(coroutine4),
]
loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(asyncio.wait(tasks))
except KeyboardInterrupt as e:
    print('所有任务:',asyncio.Task.all_tasks())
    for task in asyncio.Task.all_tasks():
        print('取消任务:',task.cancel())
    loop.stop()
    #loop.run_forever()
finally:
    loop.close()

print('TIME:', now()-start)

