import time,threading

balance=0
lock=threading.Lock()
def Chang_it(n):
    global balance
    balance=balance+n
    balance=balance-n

def run_thread(n):
    for x in range(100000):
        lock.acquire()
        try:
            Chang_it(n)
        finally:
            lock.release()

def test():
    t = threading.Thread(target=run_thread, args=(5,))
    t1 = threading.Thread(target=run_thread, args=(8,))
    t.start()
    t1.start()
    t.join()
    t1.join()
    print(balance)

def loop():
    x=0
    while True:
        x=x^1

if __name__ == '__main__':
    t=threading.Thread(target=loop)
    t.start()