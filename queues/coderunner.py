from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self,val):
        self.buffer.appendleft(val)
    
    def dequeue(self):
        return self.buffer.pop()
        
    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)
    
user_queue = Queue() # instantiate a class

user_queue.enqueue(
    {'name': 'Timz',
     'age': 40,
     'school':'University of Nairobi'
    }
)
user_queue.enqueue(
    {'name': 'Owen',
     'age': 20,
     'school':'University of Mombasa'
    }
)
user_queue.enqueue(
    {'name': 'Excellency',
     'age': 30,
     'school':'University of Eldoret'
    }
)

print(user_queue.size()) # returns the total number of elements in the dequeue

for i in user_queue.buffer:
    print(i) # return the items 


print(user_queue.dequeue()) # removes first element inserted


