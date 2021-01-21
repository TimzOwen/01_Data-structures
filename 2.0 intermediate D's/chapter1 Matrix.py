
from numpy import * 
a = array([['Mon',18,20,22,17],['Tue',11,18,21,18],
		   ['Wed',15,21,20,19],['Thu',11,20,22,21],
		   ['Fri',18,17,23,22],['Sat',12,22,20,18],
		   ['Sun',13,15,19,16]])
    
m = reshape(a,(7,5))
print(m)

b = array([
	["comp2", 11,22,33,44],
 	["Comp3",12,13,14,15],
    ["comp4",21,22,23,24]
	])
rshp = b.reshape(3,5)
print(rshp)

print(b[2]) # returns array comp 4
print(b[1][0]) # returns comp 3

new_data = append(b,[["ICT",10,10,10,10]],0) # adds to the last part
print(new_data)


new_data = insert(b,[5],[[11],[11],[11]],1) # adds data to new columns 
 
b = delete(b,[1],0) # deleting a row 0->row 

b = delete(b,[1],1) # deleting a column

b[2] = ["comp4",3,3,3,3] # updating existing values

print(b)
