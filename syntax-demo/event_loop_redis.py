#!/usr/bin/env python
# -*- coding: utf-8 -*-
from threading import Thread
import time
import asyncio
import redis

def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()

async def more_work(x):
    print('More work {}'.format(x))
    await asyncio.sleep(x)
    print('Finished more work {}'.format(x))

start = time.time()
new_loop = asyncio.new_event_loop()
# 启动线程
t = Thread(target=start_loop, args=(new_loop,))
t.setDaemon(True) # 设置子线程为守护线程
t.start()
print('TIME: {}'.format(time.time()-start))

rcon = redis.StrictRedis(host='192.168.1.5', port=6379, db=0, decode_responses=True)
try:
    while True:
        # 1.轮询的方式
        #msg = rcon.rpop('queue')
        #if not msg:
        #    time.sleep(1)
        #    continue
        # 2.阻塞调用的方式,无消息则阻塞，有消息则返回.
        _,msg = rcon.brpop('queue')
        asyncio.run_coroutine_threadsafe(more_work(int(msg)), new_loop)
except KeyboardInterrupt as e:
    print(e)

print('main done')

