from threading import Thread, Lock
from time import sleep

A = {}
m = Lock()

class RWLock:
    def __init__(self):
        self.lock = Lock()
        self.readers = 0
        self.writers = 0

    def r_lock(self):
        self.lock.acquire()
        self.readers += 1
        self.lock.release()

    def r_unlock(self):
        self.lock.acquire()
        self.readers -= 1
        self.lock.release()

    def w_lock(self):
        self.lock.acquire()
        self.readers += 1
        self.lock.release()

    def w_unlock(self):
        self.lock.acquire()
        self.readers -= 1
        self.lock.release()

class MyThread(Thread):
    def __init__(self, new_a):
        self.new_a = new_a
        super().__init__()

    def run(self):
        m.acquire()
        global A
        A[self.new_a] = True
        print('A is', A)
        for i in range(self.new_a):
            print(i)
            sleep(0.5)
        m.release()


if __name__ == '__main__':
    t1 = MyThread(5)
    t2 = MyThread(6)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

