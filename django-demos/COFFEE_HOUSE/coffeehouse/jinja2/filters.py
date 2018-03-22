import jinja2
def customcoffee(value,arg="muted"):
    return jinja2.Markup('%s %s' % (arg,value))

import math
def squarerootintext(value):
    return "The square root of %s is %s" % (value,math.sqrt(value))
def startswithvowel(value):
    if value.lower().startswith(("a", "e", "i", "o","u")):
        return True
    else:
        return False

