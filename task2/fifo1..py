"""
Данное решение является простейшей реализацией FIFO в однопоточном режиме
После запуска цикличного чтения из очереди и его опустошения происходит прерывание выполнения программы
Возможность записать новые данные после чтения из очереди не предусмотрена
"""


class Producer:
    def __init__(self, queue):
        self.queue = queue

    def write(self, data):
        self.queue.append(data)


class Consumer:
    def __init__(self, queue):
        self.queue = queue

    def read(self):
        while True:
            try:
                data = self.queue.pop(0)
                # Обработать данные
                print(data)
            except IndexError:
                print("Queue is empty")
                return


def main():
    queue = []
    producer = Producer(queue)
    consumer = Consumer(queue)
    producer.write(1)
    producer.write(2)
    producer.write(3)
    consumer.read()

main()