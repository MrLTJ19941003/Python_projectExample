class Chain(object):
    def __init__(self,path=''):
        self._path = path
    def __getattr__(self,path):
        return Chain('%s/%s' % (self._path,path))
    def __str__(self):
        return self._path
    def __call__(self,path=''):
        return Chain('%s/%s' % (self._path,path))

print(callable(Chain()))
print(callable(Chain().users()))
print(callable(list(range(5))))
print(Chain('tttt').user('sss').bbb)