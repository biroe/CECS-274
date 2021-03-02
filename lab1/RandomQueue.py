import random 
from Interfaces import Queue 
import ArrayQueue


class RandomQueue(Queue):
    def __init__(self):
        self.queue = ArrayQueue.ArrayQueue()


    def add(self, x : object):
        '''
            add: Add the value x to the Queue
            Inputs:
                x: Object type, i.e., any object
        '''
        self.queue.append(x)

    def remove(self) -> object:
        '''
            remove: remove the next (previously added) value, y, from the
                    Queue and return y. The Queue’s queueing discipline 
                    decides which element should be removed.
            Return: Object type
        '''
        self.queue[x],self.queue[-1] = self.queue[-1],self.queue[x]
        self.queue.pop()
        return self.queue

    def size(self) -> int:
        return self.queue.size()


