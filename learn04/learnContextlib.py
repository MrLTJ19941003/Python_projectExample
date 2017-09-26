from contextlib import contextmanager,closing
from urllib.request import urlopen
class query(object):
    def __init__(self,name):
        self.name=name

    def querys(self):
        print('name : ',self.name)
        return 'a'

def create_query(name):
    print('start')
    q=query(name)
    q.querys()
    print('end')

with closing(urlopen('http://www.baidu.com')) as u:
    for x in u:
        print(x)