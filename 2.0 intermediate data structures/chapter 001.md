
## Matrix

This are 2-D arrays where elements must be equal in number of elements and of the same data type

They can be used with numpy to perform mathematical expression and scientifi operations too

Make sure to install __numpy__

0s take the rows and 1s take the column when editing matrix

### sample matrix

from numpy import * 
a = array([['Mon',18,20,22,17],['Tue',11,18,21,18],
		   ['Wed',15,21,20,19],['Thu',11,20,22,21],
		   ['Fri',18,17,23,22],['Sat',12,22,20,18],
		   ['Sun',13,15,19,16]])
    
m = reshape(a,(7,5))
print(m)

### Accessing values:

done using __indexes__ just similar to 2-D arrays

	print(array[index])

### adding new row data

uses __append()__ method

	new_r = append(matrix[["data",12,12,12,12,]],0)

### updating a column

uses the __insert()__ method

Also indicate the column to which you want to change

	mat_clm = insert(matrix,[column],[[22],[33],[44],[55],[66]],1)

### Deleting a row from a matrix

uses the __delete()__ method 

	delete (matrix[2],0)

### Deleting a column

uses the __delete()__ method 

Also specify the axis to delete from

	delete(matrix, [index],axis)
	delete(mat,[2],1)

### Updating a row in a matrix

done by re-assigning values at specified index row

	mat[index] = ['name', data]
	b[2] = ["comp",2,2,2,2]
