import itertools

i=itertools.count(1)
ns=itertools.takewhile(lambda x:x<=10,i)
print(ns)
for x in i:
    print(x)
    if(x>10):
        break

i=itertools.cycle('abc')
count=0;
for x in i:
    print(x)
    count=count+1
    if(count>5):
        break

i=itertools.repeat('A',4)
for x in i:
    print(x)

for x in itertools.chain('abc','efg'):
    print(x)

#for x,y in itertools.groupby('AaaBBbBCccDDd'):
for x, y in itertools.groupby('AaaBBbBCccDDd',lambda c:c.upper()):
    print(x,list(y))