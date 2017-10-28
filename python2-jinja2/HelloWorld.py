#!/usr/bin/env python
# coding=utf8
import sys
from jinja2 import Template

reload(sys)
sys.setdefaultencoding('utf8')

template = Template('Hello {{name}}')
print template.render(name='John Doe 张三')

