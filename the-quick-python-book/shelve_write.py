#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
reading or writing of pieces of data in large files,
without reading or writing the entire file
'''
import shelve
book = shelve.open('address.dat')
book['flintstone'] = ('fred','555-1234', '123 Bedrock Place')
book['rubble'] = ('barney', '555-4321', '1235 Bedrock Place')
book.close()

print("done")

