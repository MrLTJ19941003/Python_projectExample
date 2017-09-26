from multiprocessing import Pool
import os,time,random

def long_time_task(name):
    print('Run task %s (%s) (%s)...' % (name, os.getpid(), os.getppid()))
    start=time.time();
    time.sleep(random.random()*3)
    end=time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__ == '__main__':
    print('Parend process (%s)' % os.getpid())
    p=Pool(5)
    for x in range(9):
        p.apply_async(long_time_task,args=(x,))
    print('Waiting all subprocess done...')
    p.close()
    p.join()
    print('All subprocess done.')

