# 由并发变成了串行,牺牲了运行效率,但避免了竞争
import os
import time
import random
from multiprocessing import Process,Lock

def work(lock,n):
    lock.acquire()
    print('%s: %s is runing' % (n,os.getpid()))
    time.sleep(random.random())
    print('%s: %s is down' % (n, os.getpid()))
    lock.release()

if __name__ == '__main__':
    lock = Lock()
    for i in range(3):
        p=Process(target=work,args=(lock,i))
        p.start()
