
from  io import BytesIO

class learnWriter(object):
    def __init__(self,path=''):
        self._path=path

    def writer(self):
        f = open(self._path,'w')
        f.write('python复杂的写入')
        f.close()


    def simpterWriter(self):
        with open(self._path, 'w') as f:
            f.write('好哒！好哒')

    def byteioRead(self):
        f=BytesIO()
        f.write('中文'.encode('utf-8'))
        return f.getvalue()

    def byteioRead01(self):
        f=BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
        s=f.read()
        return s


#print(learnWriter('d:/a.txt').writer())
#print(learnWriter('d:/a.txt').simpterWriter())
print(learnWriter().byteioRead01())