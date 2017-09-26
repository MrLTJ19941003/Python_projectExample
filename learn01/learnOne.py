#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class student(object):
    def __init__(self):
            self.a,self.b = 0,1
    def __str__(self):
        return 'My name is %s' % self.name

    def __iter__(self):
        return self

    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if(self.a>100):
            raise StopIteration()
        else:
            return self.a
    def __getitem__(self, item):
        if isinstance(item,int):
            a,b=1,1
            for x in range(item):
                a,b=b,a+b
            return a
        if isinstance(item,slice):
            start=item.start
            stop=item.stop
            if start is None:
                start=0
            a,b=1,1
            L=[]
            for x in range(stop):
                if x>=start:
                    L.append(x)
                a,b=b,a+b
            return L

    def __getattr__(self, item):
        if item=='age':
            return lambda :25
        else:
            return item
s = student()
print(s.bbbb)
print(list(range(5))[1:3])
print(s[1:13])
for n in s:
    print(n)