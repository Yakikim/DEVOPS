# Second class
# A.
# 1. Create two numeric variables named X and Y.
# 2. Print the word “BIG” if the value of X is bigger than Y .
'''
X , Y = 0 , 0
X, Y = input("Insert X:") , input("Insert Y:")
if X > Y:
    print(X)
'''
# B.
# 1. Run a “for” loop 5 times.
# 2. Print the iteration number every time.
'''for x in range(1,6):
    print(x)
    x +=1'''
# C.
# 1. Create a variable and initialize it with a number 1-4.
# 2. Create 4 conditions (if-elif) which will check the variable
# value.
'''x = 1
if x > 5:
    print("no")
elif x == 5:
    print ("no")
elif x in range(5,50):
    print("no")
elif x < 5:
    print("yes")'''

# 3. print a different season name for each number:
# For example:
# - 1 = summer
# - 2 = winter
# - 3 = fall
# - 4 = spring
'''x = int
x = int(input("Insert 1-4:"))
if x == 1:
    print("summer")
elif x == 2:
    print("winter")
elif x == 3:
    print("fall")
else:
    print("spring")'''

# D.
# 1. how many times will the following loop run?
# 2. what will be printed last?
'''
1. 10
2. 10
    '''
# E.
# Write a program with variables holding the following:
# 1. Your age.
# 2. First letter of your last name.
# 3. Current shekels-dollar currency.
# 4. Did you flew abroad (true/false)
# 5. Your apartment number.
# ● Print all variables.
# ● Add the currency(3) to your age(1), and check the result.
# F.
# Create a program which uses input with the following:
# 1. Ask user for his phone number
# 2. Print the words “phone number” and the phone number
# the user entered.
# G.
# Write a program with the following:
# 1. Function named printHello() that prints the word “hello”.
# 2. Function named calculate() which adds 5+3.2 and prints the
# result.
# H.
# Write a program with the following:
# 1. Function that receive a name as an argument and prints it.
# 2. Function that receive a number, divide it by 2, and prints the
# result.
# I.
# Write a program with the following:
# 1. Function that receive two numbers, add them, and return the
# sum.
# 2. Function that receive two Strings, add space between them,
# and return one spaced string.
'''def num( x, y):
    return (x + y)
def str (x , y):
    return(x + " " + y)
print(num(1,4) , str("Yaki", "metuki"))
'''
# J.
# Create a program with the following:
# 1. Create an array with 3 numbers
# 2. Iterate through the array to print all elements.
'''def iter(i):
    for value in range(0, len(i)):
        print(i[value])
lst = [False, 2 , "Three"]
iter(lst)
'''
# K.
# Create a program which will get a list of numbers and prints the
# sum of all items.
'''x = [33, 55, 66]
y = 0
for i in range(0, len(x)):
    y += x[i]
print(y)'''

# L.
# Write a Python program to iterate over dictionaries and prints all keys
# using for loop
'''x = {"a": 1, "b": 2, "c": 5}
for key in x:
    print (key)'''

# Challenges:
# M.
# Create a nested for loop (loop inside another loop) to create
# a pyramid shape:
'''for i in range (0,10):
    for j in range(i, i+1):
        print(j*"*") '''
