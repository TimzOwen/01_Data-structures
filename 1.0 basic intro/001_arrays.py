
#  Arrays structure

from array import *

arrayVarName = array('TypeCode',['value-initializers'])

# Create and print elements of an array

from array import *

array1 = array('i',[11,22,33,44,55,66,77,88,99])

for i in array1:
    print(i)
    
# acess elements 

print(array1[0]) # 11

# Add new elements
array1.insert(0,100) 

# remove elements

array1.remove(33)

# search an element
print(array1.index(44))

# update elemts

array1[1] = 555

print(array1)

