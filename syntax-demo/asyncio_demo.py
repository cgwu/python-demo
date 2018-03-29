#!/usr/bin/env python
# -*- coding: utf-8 -*-
import asyncio
import threading

#@asyncio.coroutine #Python3.4
async def hello(): # async Python3.5
    print("Hello world! (%s)" % threading.currentThread())
    # 异步调用
    #r = yield from asyncio.sleep(1) #Python3.4
    r = await asyncio.sleep(1) #Python3.5
    print("Hello again, %s(%s)" % (r,threading.currentThread()))
# 获取EventLoop
loop = asyncio.get_event_loop()
#loop.run_until_complete(hello())
#loop.close()

# 执行多个任务
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

