## Sets

This are collections of items with no particular order

Elements in a set cannot be duplicate

Whole set is muttable But individual elements are __immutable__

__No indexing__ supported as elements are unordered which also means __no Slicing__

__created with set()__ method or __{curl brackets}__ 

### Operations on sets

1. union
2. Intersection
3. difference 
4. Compliment

### new empty sets

	setA = {"elements"}
	setB = set(["Elements"])

### Accessing Values in a set

use loops to access whole list

Individual elements are not accessible

	for x in arry:
		print(x)

### Adding new elements to a set

elements can be added with __add()__ method

	set.add("Element)

### Removing elements from a set

we use __discard()__ method

	set.discard("item")

### Union between sets 

returns a set with elements in both sets  discarding repeated elements in the list

	uses __(|)__ to do the union

### set intersections

returns elements only common in both sets

	uses the and (&) symbol

### set Difference

returns list of elements found on first set and not in both or set two

	uses the minus (-) sysmbol operator

### comparing sets 

Done by checking for subset or superset 

The results are always boolean 

	True
	False
uses __(<=)__ for __subset__

uses __(>=)__ for __superset__
