## Arrays

Arrays are containers which can hold a fixed number of items and of the same type

uses arrays to implement data interaction with the computer

#### Array identification

    Index -->location of an element in an array
    
    Element -> member inside an array 

#### Keep in mind:

    index starts at 0

    Arrays legth is always n-1

    Elements can be accessed via indexing

    typecode must be declared to make it clear the data types in an array

#### Arrays Operations

    update --> update value of an array at a given index

    Search -->Search an element by index / value

    Deletion -->used to delete elements at specified index position

    Insert--> add an element to an array at index specified

    Traverse-->print elements of an array one after another

#### Structure of an array in python

    from array import *

    arrayVarName = array('type code', ['value-initializers'])


### Type code tables

| Type code |     Value representation
|:----------|----------------------------------:|
| b         | 1 byte **singed integers**        |
| B         | 1 byte **unsigned integers**      |
| c         | 1 byte **characters**             |
| i         | 2 bytes **signed integers**       |
| I         | 2 byte **unsiged integers**       |
| f         | 4 byte **floating points**        |
| d         | 8 byte **floating points**      \||


### accessing an element

you can access an element using index

    print(array[i])

### inserting a new data in array

insert at specific index:
    
    array1[0,100]

Delete an item of an array

n/b removing out of range throw 'out of index' error

    array1.remove(element)

#### search element in an array

you can do a search operation using index 

you also have to pass in an existing element

    print(array1.index(element))

#### updating an element

This will replace the existing element with the new data

you have to provide an index to be update with the new data to be updated to

    array1[1] = element
