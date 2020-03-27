import queue

def example_1():
    q = queue.Queue(2)
    q.put('1')
    q.put('2')
    print(q.get())
    q.put('3')
    print(q.get())
 
    print(q.get())
    q.task_done()
    q.task_done()
    q.join()
    

if __name__ == '__main__':
    example_1()
    