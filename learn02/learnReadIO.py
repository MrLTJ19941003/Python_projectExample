from io import StringIO

class learnReadIOs(object):
    def __init__(self,path=''):
        self._path=path

    def reads(self):
        try:
            f=open(self._path,'r')
            result = f.read()
        except IOError as e:
            print(e)
        finally:
            print('文件已关闭')
            f.close();
        return result

    def simplteRead(self):
        with open(self._path,'r') as f:
            return f.read()

    def stringioRead(self):
        s=StringIO()
        s.write('python写入内存')
        s.write(',hello')
        s.write(',word!')
        return s.getvalue()

    def stringioRead01(self):
        s=StringIO('Hello!\nHi!\nGoodbye!')
        while True:
            f=s.readlines()
            if f=='':
                break
            return f




#print(learnReadIOs('d:/a.txt').simplteRead())
#print(learnReadIOs().stringioRead())
print(learnReadIOs().stringioRead01())

