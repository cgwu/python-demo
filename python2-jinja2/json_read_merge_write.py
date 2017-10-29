#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 安装命令：pip install Jinja2
# ref: http://jinja.pocoo.org/
# python 3 从json配置文件读取,合并模板,保存到文件


import sys,json
from jinja2 import Template

json1 = {}
with open('cfg.json', 'r', encoding='utf8') as f:
    json1 = json.load(f)
print('从文件再读入到变量:', type(json1), json1 )
print(json1['extra'][1])

template = Template("您好 {{ cfg['extra'][1] }}")
result = ( template.render(cfg = json1) )
print(result)

# 写入到文件
with open('result_utf8.txt', 'w', encoding='utf8') as f:
    f.write(result)
print('done')
