"""
@author: Okwudili Ezeme
@date: 2019-02-11
This problem was asked by Apple.

Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods: enqueue, which inserts an element into the queue, and dequeue, which removes it.
"""


class Queue:
    "I dont know why two stacks are required"

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        try:
            return self.queue.pop(0)
        except IndexError as err:  # catch exception due to empty list
            print(f'>>> {err} has occured <<<')
            return False
