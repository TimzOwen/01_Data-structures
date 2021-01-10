
## Tuples

This are listed immutable objects.

They use parenthesis to list objects 

Tuples created with single elements must have comma after the element


values are separated by commas

formart

    tuple1 = ("element","element")

    oneTuple = (10,)

Indexing starts from 0 like other DS

Tuples can be:

    printed out in order

    sliced at specific index

    Contatenated

#### Updating tuples

Only happens when you need to recreate

You cannot update an existing element in a tuple. Throws an exception error

    tuple[0] = 20   --> throws an error


#### Deleting elements:

Removing one element at a time is not permitted

del is used to remove en entire tuple 

    del tupleName

### Operations on Tuples:

#### Tuple operations

| Expression                    |   expected output   |             Description     |
|:------------------------------|---------------------|----------------------------:|
| len([1,2,3,4])                | 4                   | Find lenght of list         |
| [2,4,6] + [6,8,10]            | [2,4,6,8,10]        | List concatemation          |
| ["Hey"] * 3                   |  ["Hey","Hey,"Hey"] | Repetitionof elements       |
| 10 in [10,20,30]              | True                | check element memebers      |
| for i in [2,3,4] print i      | 2,3,4               | iteratate elements in list  |
