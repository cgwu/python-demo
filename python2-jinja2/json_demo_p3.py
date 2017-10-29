#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,json
from jinja2 import Template

data = {
'name':'ACME',
'shares':100,
'price':3.1415,
'extra':[1,u'hello中国',('1','2')]
}

print( data )
str_json = json.dumps(data) # 导出为字符串
print('导出成字符串:', type(str_json), ' : ', str_json)
json_data = json.loads(str_json) # 将字符串转为python对象dict
print('将字符串转为python对象dict:', type(json_data), ' : ', json_data )

print( '----------------' )

# 写入到文件
with open('data.json', 'w', encoding='utf8') as f:
    json.dump(data,f)

# 从文件读取
json1 = {}
with open('data.json', 'r', encoding='utf8') as f:
    json1 = json.load(f)
print('从文件再读入到变量:', type(json1), json1 )

#template = Template('Hello {{name}}')
#print template.render(name='John Doe 张三')




