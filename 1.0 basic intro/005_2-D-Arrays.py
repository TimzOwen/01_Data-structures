
# 2-D Arrays

from array import *

# create an array

temp = [
    [10,20,30,40,50],
    [2,4,6,8,10,12],
    [11,22,33,44,55],
    [13,14,15,16,17]
    ]

# accessing elements of an array.

print(temp[0]) # -->  [10,20,30,40]

print(temp[1][3]) # --> 8

# prin entire array and formart it acrodingly
for x in temp:
    for i in x:
        print(i, end= " ")
    print()
   
# inserting values in arrays:

temp.insert(1,[99,88,77,66,55])

for x in temp:
    for i in x:
        print(i,end=" ")
    print()

# Updating values in 2-D array

temp[1] = [786, 500]
temp[2][1] = 1000

for x in temp:
    for i in x:
        print(i, end= " ")
    print() 
    
    # output
    # 10 20 30 40 50 
    # 786 500 
    # 11 1000 33 44 55 
    # 13 14 15 16 17
    
# Deleting values in a 2-D Array

del temp[2]

for x in temp:
    for i in x:
        print(i, end= " ")
    print()
