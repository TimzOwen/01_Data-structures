from collections import queue
from operator import le

class Queue:
    
    def __init__(self) -> None:
        self.queue = []
        
    # add an element
    def enqueue(self, item):
        self.queue.append(item)
        
    #remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)
    
    # Display the queue
    def display(self):
        print(self.queue)
        
    # check the size of the queue
    def size(self):
        return len(self.queue)