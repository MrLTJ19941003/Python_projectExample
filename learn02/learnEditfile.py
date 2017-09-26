from datetime import datetime
import os

#print(os.name)
#print(os.uname()) window系统不支持
#print(os.environ.get('JAVA_HOME'))
#print(os.environ.get('PATH'))
print(os.path.abspath("."))
createfile=os.path.join(os.path.abspath("."),'createfile')
#os.mkdir(createfile)
#os.rmdir(createfile)
print(os.path.split('d:\strageyg.png'))
print(os.path.splitext('d:\strageyg.png'))
print(os.path.isfile(os.listdir('.')[2]))
print ([x for x in os.listdir('.') if os.path.isdir(x)])
print ([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])

pwd=os.path.abspath('.')
for x in os.listdir(pwd):
    fsize=os.path.getsize(x)
    mtime=datetime.fromtimestamp(os.path.getmtime(x)).strftime('%Y-%m-%d %H:%M')
    flag='/'if os.path.isdir(x) else ''
    print('%4d  %s  %s%s' % (fsize,mtime,x,flag))

paths='d:/'
listdir=os.listdir(os.path.abspath(paths))
for d in listdir:
    print(os.path.isdir(os.path.join(paths,d)))
    #print(os.path.isfile(os.path.join(paths,d)))