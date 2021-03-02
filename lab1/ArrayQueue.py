import numpy as np
from Interfaces import Queue

class ArrayQueue(Queue):
    def __init__(self):
        self.n = 0
        self.j = 0
        self.a = self.new_array(1)
        
    def new_array(self, n: int) ->np.array:
        return np.zeros(n, np.object)
    
    def resize(self):
        '''
            Resize the array
        '''
        if self.isFull():
            self = new_array(self.size*2)
            for i in range(len(self)):
                self.append(self[i])
            self.the_array = self
            self.size = (self.size)*2    
        elif len(self) < (1/8)*(self.size) and (self.size) >= 40:
            self = new_array((self.size)//2)
            for i in range(len(self)):
                self.append(self[i])
            self.the_array = self
            self.size = (self.size)//2
        else:
            pass

    
    def add(self, x : np.object) :
        '''
            shift all j > i one position to the right
            and add element x in position i
        '''
        # adds an item at the end of the list 
        new_node = new_array(x, None)
        current = self.head # Start the traversal 
        if self.size == 0: # check if list is empty
            self.add(x) 
        else:
            while (current.getNext()!=None): 
                current = current.getNext() # traversing the list 
            current.setNext(new_node)
            self.size = self.size +1

    def remove(self) -> np.object :
        '''
            remove the first element in the queue
        '''
        # remove the node containing the item from the list 
        if self.size == 0:
            raise Exception('List is Empty')
        current = self.head 
        previous = None
        found = False 
        while current != None and not found:
            if current.getData() == np:
                found = True 
            else:
                previous = current
                current = current.getNext()
        if not found: 
            raise Exception('Item not in list')
    
    def size(self) :
        return self.n

    def __str__(self):
        s = "["
        for i in range(0, self.n):
            s += "%r" % self.a[(i + self.j) % len(self.a)]
            if i  < self.n-1:
                s += ","
        return s + "]"

    def __iter__(self):
        self.iterator = 0
        return self

    def __next__(self):
        if self.iterator < self.n:
            x = self.a[self.iterator]
            self.iterator +=1
        else:
             raise StopIteration()
        return x

