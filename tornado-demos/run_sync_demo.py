#!/usr/bin/env python
# -*- coding: utf-8 -*-
# tornado: 5.0.1
import asyncio
from tornado import gen
from tornado.ioloop import IOLoop
async def main():
    print('main func called')
    #await gen.sleep(2)
    await asyncio.sleep(2)
    print('main func done')

if __name__ == '__main__':
    IOLoop.current().run_sync(main)

