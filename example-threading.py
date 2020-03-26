import threading
import time

def example_1():
    class ThreadSet(threading.Thread):
        def __init__(self, data):
            super().__init__()
            self.data = data
        def run(self):
            time.sleep(1)
            self.data[0] = time.time()

    class ThreadPrint(threading.Thread):
        def __init__(self, data):
            super().__init__()
            self.data = data
        def run(self):
            time.sleep(2)
            print(self.data[0])

    data = [0]
    thread_set = ThreadSet(data)
    thread_print = ThreadPrint(data)
    threads = [thread_print,thread_set]
    for t in threads:
        t.start()
        t.join()


def example_2():
    def task():
        time.sleep(10)
    a = threading.Thread(target=print,args=('10'))
    b = threading.Thread(target=task)
    for i in [a, b]:
        i.start()
    for i in [a, b]:
        i.join()
    threading.local())

if __name__ == '__main__':
    example_2()