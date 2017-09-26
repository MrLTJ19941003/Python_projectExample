import pickle


d=dict(name='zhangsao',age=23)
print(pickle.dumps(d))

f=open('d:/a.txt','wb')
pickle.dump(d,f)
f.close()

g=open('d:/a.txt','rb')
s=pickle.load(g)
g.close()
print(s)

import json
print(json.dumps(d))
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))

class student(object):
    def __init__(self,name,age):
        self._name=name
        self._age=age
    def student2dict(self):
        return {'name':self._name,'age':self._age}

print(json.dumps(student('zhangsan',22),default=lambda obj:obj.__dict__))