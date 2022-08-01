print("Excersize 1")
# 1) Find the cross product of the following vector defined as a tuple:
# a = (3, 2, 3) and b = (7, 5, 1)
# The cross product is: (2, -4, -1)
a = (3, 2, 3)
b = (7, 5, 1)
c = (a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[1] - a[1]*b[0])
print(c)
print("*********************************************************")


print("Excersize 2")
# 2) Write a script that asks the user for three numbers. Each time the user inputs the number,
# convert the input value to an integer using the floor() method. Each integer must be appended
# to a list. For example:
# Enter the value: 34.2
# Enter the value: 20.0
# Enter the value: 1
# The list contains 34, 20, 1
a = []
for i in range(3):
    a.append(float(input("Enter the value: ")).__floor__())

print("The list contains {}, {}, {}".format(*a))
print("*********************************************************")


print("Excersize 3")
# 3) Write a script to reverse the order of characters in the given sentence
# sentence = ‘My name is Binil Starly’
# The output should be:
# ylratS liniB si eman yM
sentence = "My name is Binil Starly"
print(sentence[::-1])
print("*********************************************************")


print("Excersize 4")
# 4) Write a program to check whether a given substring is present in the given string and
# number of times it appears.
# Input Text:
# The world is round. We live in it. But perhaps the world is flat!
# Enter Search Text:
# perhaps
# Output
# The number of times ‘perhaps’ appears is: 1

inputText = input("Enter Text: ")
searchText = input("Enter Search Text: ")
print("The number of times '{}' appears is: {}".format(searchText, inputText.count(searchText)))
print("*********************************************************")


print("Excersize 5")
# 5) Take two lists, say for example the two lists below:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 78, 21]
# and write a script that returns a list that contains only the elements that are common
# between the lists (without duplicates). Make sure your program works on two lists of different
# sizes.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 78, 21]
c = []
for i in a:
    if i in b:
        c.append(i) if i not in c else None
print(c)
print("*********************************************************")


print("Excersize 6")
# 6) A user has two standard dices. Each dice has values from 1 through 6. The user throws
# each set of 2 dices 3 times. Simulate this action using a Python script wherein the script
# randomly picks integers for the dices. For the three throws, print the values that appear on
# the dices and the total sum of the scores obtained (total of 6 values ( 2 dices x 3 throws).
# (Do not use For Loops).

import random


c = [] # list to store the values of the dices
for i in range(3):
    c.append([random.choice(range(1, 7)) for j in range(2)])
print(c)
print("The total sum of the scores obtained is: {}".format(sum(sum(i) for i in c)))
print("*********************************************************")