from multiprocessing import Process
import os

#子进程要访问的代码
def run_proc(name):
    print('run child process %s (%s)' % (name,os.getpid()))

if __name__ == '__main__':
    print('parent process %s. ' % os.getpid())
    p=Process(target=run_proc,args=('ss',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process will end')


