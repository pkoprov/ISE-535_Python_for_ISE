# -*- coding: utf-8 -*-
"""
@author: bstarly
"""

'''
Qn1
Combine the following lists to a single list
x = [1,5,7,2]
y = [7,3,3,1,6,21,5,22,11]

'''
x = [1,5,7,2]
y = [7,3,3,1,6,21,5,22,11]

x.extend(y)

print("The new extended list is", x)


#the alternate method is

z = x + y
print(x)
print(z)

'''
Qn2
Take 2 unequal list and create a new list that 
contains only numbers common to both lists
a=[1, 5, 2, 5, 33, 10, 2]
b=[50, 20, 1, 4, 22, 11, 3, 6, 50, 20, 10, 3, 55]

'''

a=[1, 5, 2, 5, 33, 10, 2]
b=[50, 20, 1, 4, 22, 11, 3, 6, 50, 20, 10, 3, 55]

a = set(a)
b = set(b)

c = a & b
c = list(c)

print("The new list is:", c)





'''
Qn3
# Count how many times the word 'and' appears in this paragraph.
# Break the paragraph into individual bag of words
# print total number of individual words in the paragraph
# Break the paragraph into sentences separated by the full stop
# print number of whole sentences in this new broken up list
paragraph = "Walk into the Library this week"+" and you’ll be greeted not by the towering Bookstacks but by soft,"+
            " hanging lights and a grand, open staircase. Faculty offices"+
            " so small they weren’t accessible have been removed, and long"+
            " windows looking out onto campus are now dotted along the walls."+
            " Colorful chairs and wide tables are still spread across the"+
            " floors, but the library is brighter, more spacious and more"+
            " welcoming after a yearlong renovation."
'''

paragraph = ("Walk into the Library this week"+" and you’ll be greeted not by the towering Bookstacks but by soft,"+
            " hanging lights and a grand, open staircase. Faculty offices"+
            " so small they weren’t accessible have been removed, and long"+
            " windows looking out onto campus are now dotted along the walls."+
            " Colorful chairs and wide tables are still spread across the"+
            " floors, but the library is brighter, more spacious and more"+
            " welcoming after a yearlong renovation.")

countAnd = paragraph.count("and")
print("The number of times 'and' appears is ", countAnd)


bagWords = paragraph.split()
print("The bag of words are:", bagWords)
print("The Number of individual words are:", len(bagWords))


bagSentences = paragraph.split('. ')
print("The bag of words are:", bagSentences)
print("The Number of individual sentences are:", len(bagSentences))

'''
Qn4
Find Movies that start with a letter G 
movies= ["Star Wars", "Batman", "Gone with the Wind", "Shawshank Redemption"]
Randomly Select 1 movie from the list and check if it starts
with "G".
Print True or False for the above check
Do not use loops or Conditional statements
'''

import random
movies= ["Star Wars", "Batman", "Gone with the Wind", "Shawshank Redemption"]
selMovie = random.choice(movies)
ans = selMovie.startswith('G')
print("The random selected movie was: ", selMovie)
print("Did it start with 'G':", ans)

'''
Qn5
Generate a Ball List which should contain 5 colored balls 
each with an associated integer value.
The Ball List is colored to have exactly 5 Red and 5 Blue Balls.
Each colored ball has a randomly selected score value
between 1 and 20

Print the Original Ball List
Randomly Sample 5 balls from this ball List.
Print the total value of the scores on each of the 5 sampled Balls.
DO NOT USE FOR-LOOPS
'''

ball1 = ("Red", random.randint(1,20))
ball2 = ("Red", random.randint(1,20))
ball3 = ("Red", random.randint(1,20))
ball4 = ("Red", random.randint(1,20))
ball5 = ("Red", random.randint(1,20))

ball6 = ("Blue", random.randint(1,20))
ball7 = ("Blue", random.randint(1,20))
ball8 = ("Blue", random.randint(1,20))
ball9 = ("Blue", random.randint(1,20))
ball10 = ("Blue", random.randint(1,20))

ballList = []
ballList.extend([ball1,ball2,ball3,ball4,ball5,ball6,ball7,ball8,ball9,ball10])

print("The contents of the Ball List are:", ballList)


#pick Random 5 balls from the list
selBallList = random.sample(ballList, 5)

print("The lucky list is:", selBallList)

score = selBallList[0][1]+ selBallList[1][1] + selBallList[2][1] + selBallList[3][1] + selBallList[4][1]

print("The Mega Lucky Number Total is:", score)

# the same as above but with for-loops
score = 0
for ball in selBallList:
    score = score + ball[1]
print("The score is through for-loops", score) 


'''
Qn6
Print the values within a list using FOR Loops
'''
numList = [30, 230, 1, 30, 40, 20, 30, 30]

for number in numList:
    print(number)

for i in range(3, len(numList)):
    print(numList[i])

for i in range(3, len(numList),2):
    print(numList[i])

nameList=["Binil", "Starly", "Ethan", "Evan", "Rachel", "Sam"]

for index, name in enumerate(nameList):
    print(index, name)
    
'''
Qn7
Print the key and values within a dictionary
using FOR loops
'''

nameRecord={1:"Binil", 2:"Starly", 3:"Ethan", 4:"Evan", 6:"Rachel", 10:"Sam"}
print(nameRecord[10])

for key, value in nameRecord.items():
    print(key, value)

for k,v in nameRecord.items():
    print(k,v)


'''
Qn8
Find the sum of first 0 to 20 (both inclusive) whole numbers.
using FOR loops
'''

sumVal=0
for number in range(0,21):
    sumVal = sumVal + number
    print(f"Sum={sumVal}, Number={number}")
    
print("The total value :", sumVal)

'''
Qn9
Iterate through a list and create a new list that 
contains the square of the values in the original list
using For Loops
'''
numList = [30, 2, 1, 30, 40, 20, 30, 30]
sqList = []
for number in numList:
    sqList.append(number * number)
print("Square of list is", sqList)

#Using List Comprehensions
sqList2 = [number * number for number in numList]
print("Square of list is", sqList2)

'''
Qn10
Count the number of times the integer 100 appears in this list
num=[0,93,100,9,10,101,100,1,30,100,8,99,82,22]
'''

numList=[0,93,100,9,10,101,100,1,30,100,8,99,82,22]
count = 0
for item in numList:
    if item == 100:
        count = count + 1 #count+=1

print("The number of times 100 appears is", count)

hundredlist = [item for item in numList if item == 100]
print("The number of times 100 appears is", len(hundredlist))
    
'''
Qn11
check if two strings are the same or not
str1 = "My name is"
str2 = "My namee is"
'''
str1 = "My name is"
str2 = "My namee is"

if str1 == str2:
    print("They are the same")
else:
    print("They are not the same")



'''
Qn12
Find if the word 'is' exists in the paraph and count how many times
paragraph = "Walk into the Library this week"+" and you’ll be greeted not by the towering Bookstacks but by soft,"+
            " hanging lights and a grand, open staircase. Faculty offices"+
            " so small they weren’t accessible have been removed, and long"+
            " windows looking out onto campus are now dotted along the walls."+
            " Colorful chairs and wide tables are still spread across the"+
            " floors, but the library is brighter, more spacious and more"+
            " welcoming after a yearlong renovation."
'''

paragraph = ("Walk into the Library this week"+" and you’ll be greeted not by the towering Bookstacks but by soft,"+
            " hanging lights and a grand, open staircase. Faculty offices"+
            " so small they weren’t accessible have been removed, and long"+
            " windows looking out onto campus are now dotted along the walls."+
            " Colorful chairs and wide tables are still spread across the"+
            " floors, but the library is brighter, more spacious and more"+
            " welcoming after a yearlong renovation.")

bagWords = paragraph.split()
count = 0
searchStr = 'the'
for word in bagWords:
    if word == searchStr:
        count=count+1

print(f"The number of times '{searchStr}' appears is {count}")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    





