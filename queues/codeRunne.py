
# Homework 2.1 Estonian elections

# In Estonia local and parliament elections are conducted every 4 years. The mandatory age to vote in local elections is 16 and for parliament, 
# it’s 18. Write a program that asks the user for his/her age and tells them in which elections they can vote. Also, the program has to check the 
# validity of the entered age: the maximum allowed age is 140, a valid age cannot be negative.
# Example:
# >>> %Run solution.py
# Enter your age: 10
# You are too young to participate in government elections in Estonia.
# >>> %Run solution.py
# Enter your age: 17
# You can only vote at local elections.
# >>> %Run solution.py
# Enter your age: -4
# Entered age is invalid.
# >>> %Run solution.py
# Enter your age: 25
# You can vote in both local and parliamentary elections.
# >>> %Run solution.py
# Enter your age: 200
# Entered age is invalid.
# >>> %Run solution.py
# Enter your age: x
# Entered age is invalid.

from curses.ascii import isdigit
from tabnanny import check


def election_checker():
    age = input(("What's you age?: "))
    try:
        age_number = int(age)
        if type(age_number) == int:    
            if(age_number>0 and age_number <16):
                print("You are too young to participate in government elections in Estonia.")
            elif(age_number==16 or age_number<=17):
                print("You can only vote at local elections.")
            elif(age_number>=18 and age_number<=140):
                print("You can vote in both local and parliamentary elections.")
            else:
                print("Entered age is invalid.")
    except:
        print(f"Entered age {age} is invalid..")
election_checker()

# Homework 2.2 Divisibility

# Write a program that asks the user for a number and checks if it can be divided by 3 and/or 5. If the selected number can only be divided by 3 or 5 then print
# the one that it is divisible with. In case the number is divisible with both 3 and 5 the program should only print that it can be divided by both. If it’s not 
# divisible then inform the user about it. You should also handle non-integer inputs.

# Example:
# >>> %Run solution.py
# Enter a number: 9
# Number 9 is divisible by 3
# >>> %Run solution.py
# Enter a number: 10
# Number 10 is divisible by 5
# >>> %Run solution.py
# Enter a number: 15
# Number 15 is divisible by 3 and 5
# >>> %Run solution.py
# Enter a number: 1
# Number 1 cannot be divided by 3 or 5
# >>> %Run solution.py
# Enter a number: hello world
# The inserted value was not a number

def check_divisibility():
    num = input("Enter a number to check divisibility: \n")
    try:
        number = int(num)
        if number.isdigit():
            if(number% 3 == 0 and number % 5 == 0):
                print(f"Number {num} is divisible by 3 and 5")
            elif(number % 3 == 0):
                print(f"Number {num} is divisible by 3")
            elif(number % 5 == 0):
                print(f"Number {num} is divisible by 5")
            else:
                print(f"Number {num} cannot be divided by 3 or 5")
    except:
            print("The inserted value was not a number")
check_divisibility()
