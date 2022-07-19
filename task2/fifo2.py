"""
В этой реализации используется модуль queue с многофункциональным интерфейсом
для работы с FIFO очередями в многопоточном режиме
Плюсы:
- У producer может быть несколько consumer
- у consumer может быть несколько producer
- Метод учета FIFO (first in, first out «первым пришёл — первым ушёл») в
многопоточном режиме не нарушается так как в модуле queue реализованы
все необходимые блокирующие операции
- Позволяет указать объем буфера
"""

import threading
import time
import random
import queue

BUF_SIZE = 10
q = queue.Queue(BUF_SIZE)

class ProducerThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super(ProducerThread,self).__init__()
        self.target = target
        self.name = name

    def run(self):
        while True:
            if not q.full():
                item = random.randint(1,10)
                q.put(item)
                time.sleep(random.random())

class ConsumerThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None):
        super(ConsumerThread,self).__init__()
        self.target = target
        self.name = name
        return

    def run(self):
        while True:
            if not q.empty():
                item = q.get()
                print("Processing item: {}".format(item))
                time.sleep(random.random())

if __name__ == '__main__':
    
    p = ProducerThread(name='producer')
    c = ConsumerThread(name='consumer')

    p.start()
    time.sleep(2)
    c.start()
    time.sleep(2)