#!/usr/bin/env python
# -*- coding: utf-8 -*-
# from: http://python.jobbole.com/87541/
import asyncio
import functools

async def do_some_work(x): pass
async def do_some_work2(x):
    print('Waiting ' + str(x))
    await asyncio.sleep(x)
    print('Done ' + str(x))
    return 'foo result' + str(x)

def done_callback(ft):
    print('Done callback: ', ft)

def done_callback2(loop, ft):
    loop.stop()
    print('Done callback2: ', ft)

print(asyncio.iscoroutinefunction(do_some_work))
print(asyncio.iscoroutinefunction(do_some_work2))

'''
要让这个协程对象运行的话，有两种方式:
* 在另一个已经运行的协程中用 `await` 等待它
* 通过 `ensure_future` 函数计划它的执行
'''
loop = asyncio.get_event_loop()
#loop.run_until_complete(do_some_work2(3))

# 有回调
#ft = asyncio.ensure_future(do_some_work2(2))
#ft.add_done_callback(done_callback)
#loop.run_until_complete(ft)

#loop.run_until_complete(asyncio.gather(do_some_work2(1), do_some_work2(3)))

#coros = [do_some_work2(1), do_some_work2(3)]
#coros = [asyncio.ensure_future(do_some_work2(1)), asyncio.ensure_future(do_some_work2(3))]
#loop.run_until_complete(asyncio.gather(*coros))

futures = asyncio.gather(do_some_work2(1), do_some_work2(3))
futures.add_done_callback(functools.partial(done_callback2, loop))
loop.run_forever()


