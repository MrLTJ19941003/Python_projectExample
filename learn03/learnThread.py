import time,threading

def loop():
    print('thread %s running .. ' % threading.current_thread().name)
    n=0
    while n<5:
        n=n+1
        print('thread %s >>> %s ' % (threading.current_thread().name,n))
        time.sleep(1)
    print('thread %s end ' % threading.current_thread().name)

if __name__ == '__main__':
    print('thread %s running .. ' % threading.current_thread().name)
    t=threading.Thread(target=loop)
    t1=threading.Thread(target=loop)

    t.start()
    t1.start()
    t.join()
    t1.join()
    print('thread %s end ' % threading.current_thread().name)