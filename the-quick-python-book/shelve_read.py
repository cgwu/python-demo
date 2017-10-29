#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import shelve
book = shelve.open('address.dat')
print(book['flintstone'])
print(book['rubble'])
book.close()


