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

z = x+y
print(z)






'''
Qn2
Take 2 unequal list and create a new list that 
contains only numbers common to both lists
a=[1, 5, 2, 5, 33, 10, 2]
b=[50, 20, 1, 4, 22, 11, 3, 6, 50, 20, 10, 3, 55]

'''
a = [1, 5, 2, 5, 33, 10, 2]
b = [50, 20, 1, 4, 22, 11, 3, 6, 50, 20, 10, 3, 55]
c = [i for i in a if i in b]
print(c)





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
paragraph = '''Walk into the Library this week and you’ll be greeted not by the towering Bookstacks but by soft,
hanging lights and a grand, open staircase. Faculty offices so small they weren’t accessible have been removed, and long
windows looking out onto campus are now dotted along the walls. Colorful chairs and wide tables are still spread across the
floors, but the library is brighter, more spacious and more welcoming after a yearlong renovation.'''

print("The word 'and' appears", paragraph.count('and'), "times in the paragraph")
bag = paragraph.split()
print("The number of words in the paragraph is", len(bag))
sentences = paragraph.split('.')
print("The number of sentences in the paragraph is", len([i for i in sentences if i != '']))


'''
Qn4
Find Movies that start with a letter G 
movies= ["Star Wars", "Batman", "Gone with the Wind", "Shawshank Redemption"]
Randomly Select 1 movie from the list and check if it starts
with "G".
Print True or False for the above check
Do not use loops or Conditional statements
'''
movies= ["Star Wars", "Batman", "Gone with the Wind", "Shawshank Redemption"]
import random
rand = random.choice(movies)
print("Selected Movie is:", rand, "and it starts with G:", rand.startswith('G'))


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
Ball_list = []
for c in ['red', 'blue']:
    for i in range(5):
        Ball_list.append((c, random.randint(1,20)))

print("Original Ball List:", Ball_list)
sampled_balls = random.sample(Ball_list, 5)
print("Sampled Balls:", sampled_balls)
print("Total Scores:", sum([i[1] for i in sampled_balls]), "on the sampled balls")

'''
Qn6
Print the values within a list using FOR Loops
'''
numList = [30, 230, 1, 30, 40, 20, 30, 30]

for i in numList:
    print(i)
    
'''
Qn7
Print the key and values within a dictionary
using FOR loops
'''
dict1={1:"Binil", 2:"Starly", 3:"Ethan", 4:"Evan", 6:"Rachel", 10:"Sam"}
for item in dict1.items():
    print(item)


'''
Qn8
Find the sum of first 0 to 20 (both inclusive) whole numbers.
using FOR loops
'''
f

'''
Qn9
Iterate through a list and create a new list that 
contains the square of the values in the original list
using For Loops
'''


'''
Qn10
Count the number of times the integer 100 appears in this list
num=[0,93,100,9,10,101,100,1,30,100,8,99,82,22]
'''
num=[0,93,100,9,10,101,100,1,30,100,8,99,82,22]
count = num.count(100)
    
'''
Qn11
check if two strings are the same or not
str1 = "My name is"
str2 = "My namee is"
'''
str1 = "My name is"
str2 = "My namee is"
print(str1 == str2)


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


        
        
        
        
        
        
        
        
        
        
        
        
        
        
    





