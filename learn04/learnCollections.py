from collections import namedtuple,deque,defaultdict,OrderedDict,Counter

def namedtupleLearn():
    p=(1,2)
    print(p[0])
    Poilt=namedtuple('Poilt',['x','y'])
    p=Poilt(55,55)
    print(p)
    print(isinstance(p,Poilt))
    print(isinstance(p,tuple))

def dequeLearn():
    q=deque(['a','b','c'])
    q.append('d')
    q.appendleft('e')
    print(q)
    print(q.pop())
    print(q)
    print(q.popleft())
    print(q)

def defaultdictLearn():
    dd=defaultdict(lambda :'N\A')
    dd['key1']='dd'
    print(dd['key1'])
    print(dd['key2'])

def OrderedDictLearn():
    dc=dict([('a',1),('c',2),('b',3)])
    print(dc.keys())

    od=OrderedDict([('a',1),('b',2),('c',3)])
    print(od)
    od=OrderedDict()
    od['z']=1
    od['y']=2
    od['x']=3
    print(od.keys())

def CounterLearn():
    c=Counter()
    for ch in 'programming':
        c[ch]=c[ch]+1
    print(c)

if __name__ == '__main__':
    #namedtupleLearn()
    #dequeLearn()
    #defaultdictLearn()
    #OrderedDictLearn()
    CounterLearn()