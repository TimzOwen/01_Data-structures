
# Tuples

# Create a tuple

tupl = ("Timz","Owen","Andela","Kenya","Software Engineer","System Admin")

tupl2 = (2,4,6,8,10,12,14,16,18,20)

print(tupl)
print(tupl2)

# accessing values

print("Tuple at index 0 is: ", tupl[0])
print("Tuples from range 1-4 are: ", tupl2[1:5])

# updating existing tuple:

tup3 = tupl2 + tupl      # prints combined tuple1 and tuple2

print(tup3)

# deleting elements in a tuple

del tup3

print(tup3) # throws a not defined tuple element

