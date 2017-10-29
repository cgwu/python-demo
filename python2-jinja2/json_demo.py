#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,json,io
from jinja2 import Template

reload(sys)
sys.setdefaultencoding('utf8')

data = {
'name':'ACME',
'shares':100,
'price':3.1415,
'extra':[1,'hello中国',('1','2')]
}

print data
str_json = json.dumps(data) # 导出为字符串
print type(str_json), ' : ', str_json
json_data = json.loads(str_json) # 将字符串转为python对象dict
print type(json_data), ' : ', json_data

print '----------------'

# 写入到文件
with open('data.json', 'w') as f:
    json.dump(data,f)

with io.open('data2.json', 'w', encoding='utf8') as f:
    f.write(u'Hello中国')
#    f.write(json.dumps(data).encode('utf8'))

# 从文件读取
json1 = {}
with open('data.json', 'r') as f:
    json1 = json.load(f)
print type(json1), json1

#template = Template('Hello {{name}}')
#print template.render(name='John Doe 张三')




