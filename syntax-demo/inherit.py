#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.weight = 80
        print('Person %s __init__' %  self.name)

    def talk(self):
        print('%(name)s, %(age)d, %(weight)d Person is talking...'
               % {'name': self.name, 'age':self.age, 'weight':self.weight})

class Chinese(Person):
    def __init__(self,name,age,language):
        #Person.__init__(self,name,age)         # 经典的语法
        super(Chinese,self).__init__(name,age)  # 新式的语法
        self.language = language
        print('Chinese %s __init__' % self.name)

    def talk(self):
        print('%s,%d,%d, %s Chinese is talking...' % (self.name,self.age,self.weight,self.language))

if __name__ == '__main__':
    p1 = Person('danny',30)
    c1 = Chinese('张三',29,'中文')
    p1.talk()
    c1.talk()

