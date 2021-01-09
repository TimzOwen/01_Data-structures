
##  Lists

This is a data storage where elements are separated by comma and elements need not be of the same datatype

Elements must be in square brackets

example:

    listA = [10,20,30,40,50]

    listB = ['a','b'.'c','d']
    
    listMixed = ["Owen",20,"Kabarak University", 2000]

Values can are accessed with indexes

### data operation

Accessing elements:

    elements are accessed by slicing or specific index

    print(list[0])

    print(list[1:6]) 

    first index on slicing is always include and last element is N-1

#### Updating an element  in a list

apped

    used for adding elements

    elements can be added in multuples with slicing

example:

    list1 = elements

    list1[2] = New element

#### deleting an element

uses the python key word del

    del list[index]

#### List operations

| Expression                    |   expected output  |             Description    |
|:------------------------------|------------------------------------------------:|
| len([1,2,3,4])                | 4                  | Find lenght of list        |
| [2,4,6] + [6,8,10]            | [2,4,6,8,10]       | List concatemation         |
| ["Hey"] * 3                   | ["Hey","Hey,"Hey"] | Repetitionof elements      |
|10 in [10,20,30]               | True               | check element memebers     |
| for i in [2,3,4] print i      | 2,3,4              | iteratate elements in list |
