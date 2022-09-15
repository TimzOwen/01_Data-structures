from collections import deque
from collections import deque

# simple list to add and pop items in an Array

user_array = [] # empty array

user_array.insert(0,90)
user_array.insert(0,34)
user_array.insert(1,400)

print(user_array) # returns entire array
# rerurns ----> [34, 400, 90]

print(user_array.pop()) # removes first element inserted into the array


# using deque()
# flexible and double ended stack & queue
 # deque removes elements using FIFO,

user_dequeue = deque()

user_dequeue.appendleft(4)
user_dequeue.appendleft(6)
user_dequeue.appendleft(8)

print(user_dequeue) # print out the dequeue

print(user_dequeue.pop())   #removes using FIFO 
user_dequeue.appendleft(10) # adds 10 to the queue

print(user_dequeue)
print(user_dequeue.popleft()) # removes the left side of the queue



# QUEUE internal implementation functions
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


## Example 2 

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


# implementation of dequeue
# 
class Queue:
    def __init__(self):
        self._elements = deque()
        
    def enqueue(self, element):
        self._elements.append(element)
    
    def dequeue(self):
        return self._elements.popleft()
    
    
def safaricom():
    data_api = int(input("enter data api number"))