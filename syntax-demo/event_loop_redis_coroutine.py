#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import asyncio
import redis

now = lambda : time.time()

def get_redis():
    connection_pool = redis.ConnectionPool(host='192.168.1.5', db=0, decode_responses=True)
    return redis.Redis(connection_pool=connection_pool)

rcon = get_redis()

async def worker(flag):
    print('Start worker')

    while True:
        start = now()
        _, msg = rcon.brpop("queue")
        print(flag, '#Wait ', int(msg))
        await asyncio.sleep(int(msg))
        print(flag, '#Done ', msg, now() - start)

def main():
    #asyncio.ensure_future(worker(1))
    asyncio.ensure_future(worker(2))

    loop = asyncio.get_event_loop()
    try:
        loop.run_forever()
    except KeyboardInterrupt as e:
        print(asyncio.gather(*asyncio.Task.all_tasks()).cancel())
        loop.stop()
        loop.run_forever()
    finally:
        loop.close()

if __name__ == '__main__':
    main()

