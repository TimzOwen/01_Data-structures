
# Dictionary

#create a new dictionary

dict1 = {"Timz":23,"Age":67,"Country":"Kenya"}

print(dict1)

# Acess elements:
print("Timz's age is : ", dict1["Age"])
print("From : ",dict1["Country"])

# Modiying elements of a dictionary

dict1['Age'] = 21  # updating existing data

dict1['Company'] = "Central Bank of Kenya"  # adding a new entry

# deleting:

dict1.clear() # removes all elements in a dictionary

del dict1['Name'] # Removes elements

del dict1  # Deletes an entire dictionary




