
## 2-D Arrays

This are nested arrays within an array

To access an array we use two indicies to get both row and column data

### Representaiton of an 2-D arrray

temp = [
    [10,20,30,40,50],
    [2,4,6,8,10,12],
    [11,22,33,44,55]
    [13,14,15,16,17]
    ]

### Accessing values

index 1-->Main parent array

index 2 --> the main element to be accessed

one Index--> returns the entire array indexed

    print(temp[0]) --> prints entire array one

    print(temp[1][0]) --> returns 2

print all array:

    use for loop to iterate through it.

    for x in array:
        for c in x:
            print(c, end= " ") # end here is used for formating

### inserting new data into a 2-D Array

you can specify a whole array to be changed by using index

We use the insert key to insert into an array

    tempArray.insert(2,[--elments here--])

### updating 2-D array

you can specify an index or update entire list

    tempArray[index] = [elements]

    tempArray[index][index] = element

### Deleting elements in an array

del()--> used to delete an entire array from existance

to delete existing specific elements, use the UPDATING PROCESS DESCRIBED

    del temp[index]

    del temp[index-1][index-2]



