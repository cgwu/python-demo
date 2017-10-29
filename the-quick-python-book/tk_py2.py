#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *

#import Tkinter
#Tkinter._test()

import sys
win = Tk()
button = Button(win, text="Goodbye", command=sys.exit)
button.pack()
mainloop()


