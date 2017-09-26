from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self,max):
        super(LastUpdatedOrderedDict,self).__init__()
        self._max=max

    def __setitem__(self, key, value):
        #containsKey=1 if key in self else 0 等价于下面的if .. else ..判断
        if key in self:
            containsKey=1
        else:
            containsKey=0
        print('dict count is %s .. %s '   % (len(self),containsKey))
        if len(self)-containsKey>=self._max:
            last=self.popitem(last=False)
            print('remove: ', last)

        if containsKey:
            del self[key]
            print('set :',(key,value))
        else:
            print('add:',(key,value))
        OrderedDict.__setitem__(self, key, value);

if __name__ == '__main__':
    lastod=LastUpdatedOrderedDict(2)
    lastod['a']=1
    lastod['b']=2
    lastod['a']=3
    print(lastod)
    #lastod['b']=4
    print(lastod)