from multiprocessing import Process,Queue
import os,time,random

def rade(q):
    print('process read is %s' % os.getpid())
    while True:
        value=q.get(True)
        print('Get %s from Queue' % value)

def writer(q):
    print('process writer is %s' % os.getpid())
    L=['A','B','C']
    for x in L:
        q.put(x)
        print('Set %s from Queue' % x)
        time.sleep(random.random())


if __name__ == '__main__':
    q=Queue()
    pr=Process(target=rade,args=(q,))
    pw=Process(target=writer,args=(q,))
    pw.start()
    pr.start()
    pw.join()

    pr.terminate()
