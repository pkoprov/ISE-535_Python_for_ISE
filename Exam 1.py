#1
# Each color has a number associated with ot. Have the computer randomly pick 2 from the list without replacement. Report the total score to user


import random

Colors = [("Red", 10), ("Blue", -20), ("Green", 30), ("Black", 100), ("Yellow", 60), ("Cyan", 43), ("Brown", 80),
          ("White", 88), ("Pink", -10)]

color_list = random.sample(Colors, 2)
total_score = sum([color[1] for color in color_list])
print(f"The total score is {total_score}")


#2
# Write a list comprehension code where strings that contain the vowels (a, e, i, o, u, A, E, I, O, U) in the list is first
# changed to lowercase and then add the ‘ *** ’ string to each filtered word in the list. The new list will contain only
# the words that contain the vowels in lowercase with +++ appended to it.(10 points)
# Ex:
# AStr = [‘Apple’, ’Game’, ’Rhythm’, ‘By’]
#
# Result = ['apple***', 'industrial***', 'game***']

vowel_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
AStr = ['Apple', 'Game', 'Rhythm', 'By',"Industrial"]


result = [word.lower() + "***" for word in AStr if any(vowel in word for vowel in vowel_list)]
print(result)

#3
# Perform the following operations on the dictionary:
# 1) Print the dollar value associated for the month of January to the console screen.
# 2) Increase the value associated with April by 20 % and then print the value to the console screen
# formatted with using the appropriate currency.(10 points)
#
# salesRec = {'Jan':'$1500.00', 'Feb': '$5600.00', 'Mar': '$2393.00', 'Apr': '$4520.00', 'May': '$6504.00'}
#
# The expected output is:
# New Values are:
#
# ('Jan', '$1500.00')
#
# ('Apr', '$5424.0')

salesRec = {'Jan':'$1500.00', 'Feb': '$5600.00', 'Mar': '$2393.00', 'Apr': '$4520.00', 'May': '$6504.00'}

print(f"(Jan, {salesRec['Jan']})")
salesRec['Apr'] = float(salesRec['Apr'].strip("$")) * 1.2
print(f"(Apr, ${salesRec['Apr']})")

#4

# Write a script that converts the following dictionary to a series of lists.(10 points)
# The given dictionary
# records = [{‘Month’: “January”, ‘Sales’: 1000}, {‘Month’: “April”, ‘Sales’: 1300}, {‘Month’: “August”, ‘Sales’: 1850},
# {‘Month’: “December”, ‘Sales’: 8500}]
# The output should be two lists:

# KeyList = [‘Month’, ‘Sales’]
# Values = [“January”, 1000, “April”, 1300, “August”, 1850, “December”, 8500]

records = [{'Month': "January", 'Sales': 1000}, {'Month': "April", 'Sales': 1300}, {'Month': "August", 'Sales': 1850},
{'Month': "December", 'Sales': 8500}]

KeyList = []
Values = []
for rec in records:
    for key, val in rec.items():
        if key not in KeyList:
            KeyList.append(key)
        Values.append(val)

print("KeyList =", KeyList, "\nValues=", Values)

#5
# Write a list comprehension code to square even numbers and cube odd numbers in the given list. The result should be
# two separate lists. Print the two new lists. (10 points)
aList = [1, 4, 5, 2, 6, 10]

even_squared = [num ** 2 for num in aList if num % 2 == 0]
odd_cubed = [num ** 3 for num in aList if num % 2 != 0]
print(even_squared, odd_cubed)

#6
# Given a list of balls = [('red', 10), ('blue', -20), ('green', 30), ('black', 100), ('yellow', 60), ('cyan', 40), (),
#   ('brown', 80), ('white', 80), ('pink', 10)].
# Have the user pick 3 colors. Report the total value of the colors picked.
# To note, once a ball is picked, it can be selected again(i.e with replacement).
# Note that there is an empty tuple in the list(it is not an error).The following example can be used as a guide.(20 points)
# Input
# Chance 1: Pick any color from (red, blue, green, black, yellow, cyan, brown, white, pink)
# Enter Choice: red
# Chance 2: Pick any color from (red, blue, green, black, yellow, cyan, brown, white, pink):
# Enter Choice: black
# Chance 3: Pick any color from (red, blue, green, black, yellow, cyan, brown, white, pink):
# Enter Choice: white
# The Total Score of your choices = 190


balls = [('red', 10), ('blue', -20), ('green', 30), ('black', 100), ('yellow', 60), ('cyan', 40), (),
         ('brown', 80), ('white', 80), ('pink', 10)]

colors = [col[0] for col in balls if len(col)>0]

choices = []
for i in range(3):
    choices.append(input(f"Chance {i+1}: Pick any color from {colors}: "))

total = []
for ch in choices:
    for ball in balls:
        if len(ball)>0:
            if ch == ball[0]:
                total.append(ball[1])

print(f"The Total Score of your choices = {sum(total)}")

#7

row1 = "ABNXBQP"
row2 = "NOHTYPY"
row3 = "PYKEZMT"
row4 = "YYSPSDH"
row5 = "TQDYWQO"
row6 = "HPYTHON"
row7 = "OMPHRSP"
row8 = "NFGOTGI"
row9 = "BGENPHY"

for row in [row1, row2, row3, row4, row5, row6, row7, row8, row9]:
    print(row)
rows = [row1, row2, row3, row4, row5, row6, row7, row8, row9]
columns = ["".join(col) for col in zip(row1, row2, row3, row4, row5, row6, row7, row8, row9)]

numR = 0
for row in rows:
    if 'PYTHON' in row or 'PYTHON' in row[::-1]:
        print(row)
        numR += 1

numC = 0
for col in columns:
    if 'PYTHON' in col or 'PYTHON' in col[::-1]:
        print(col)
        numC += 1

print(f"Number of rows with PYTHON: {numR}")
print(f"Number of columns with PYTHON: {numC}")

# 8

# Given two vectors A = [2, 1, 0] and B = [1, 2, 1]. Find the angle between the two vectors.
# Report the value in degrees. The angle can be found by taking the dot product between the 2 vectors,
# divided by its magnitude and then finding the cosine inverse of the result. DO NOT USE NUMPY. (20 points)

import math


A = [2, 1, 0]
B = [1, 2, 1]


def dot_product(A, B):
    return sum([a*b for a, b in zip(A, B)])


def magnitude(A):
    return math.sqrt(sum([a**2 for a in A]))


def angle(A, B):
    return math.acos(dot_product(A, B) / (magnitude(A) * magnitude(B)))


print(angle(A, B))
