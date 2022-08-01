# -*- coding: utf-8 -*-
"""
@author: bstarly
"""

'''
Complete Watching Section 1 - Python Essentials - 1
  - Chapter 2.4 - 2.11: Data Types (List, Sets, Tuples Dictionaries)
  - Chapter 3.1 - 3.9: Math Functions (Round, Min/Max, Random, Sorted)
before attempting these exercises

'''

'''
Qn 1:
a. Define a list of Names that contain Binil, Rachel, Ethan, Evan, Starly, Sam)
b. Print the length of the list.
c. Print the 3rd item in the list.
d. Print the last item in the list    
e. print the entire list
'''
Names = ["Binil", "Rachel", "Ethan", 'Evan', "Starly", "Sam"]
print(len(Names))
print(Names[2])
print(Names[-1])
print(Names)
'''
Qn 2:
a. Initiate a new Number list and assign it to be empty.
b. Now append the list with numbers 1,3,5,6,7,8,9,10,11,13,15,17,20
c. Print the number that is in the middle of the list.
d. Print the contents of the list that lies between the 4th and 10th index value
e. Reorder the list to be in the reverse order and print the contents to confirm it.
f. find the maximum value in the list
'''
Number = []
for i in (1,3,5,6,7,8,9,10,11,13,15,17,20):
    Number.append(i)
print(Number[len(Number)//2])
print(Number[3:10])
print(Number[::-1])
print(max(Number))


'''
Qn 3:
a.  Initiate the following list chocBrandList=["Mars", "Snickers", "Bounty", "Twix"]
b. print the length of the list
c. copy the contents of this list to a new List called newChocList
d. To the original chocBrandList, add the following String - "Lion Bar"    
e. print the contents of the newChocList. Comment on the results obtained
    
'''
chocBrandList=["Mars", "Snickers", "Bounty", "Twix"]
print(len(chocBrandList))
newChocList = chocBrandList[:]
chocBrandList.append("Lion Bar")
print(newChocList)
'''
Qn 4:
a. Define a new list aList = [1, 5, 3, 6, 2]
b. Multiply each value in this list by 2
c. Print the new list
'''
aList = [1, 5, 3, 6, 2]
newList = [i*2 for i in aList]
print(newList)




'''
Qn 5: 
a. Define a list aList = [1,5,2] and bList=[9,2,3]
b. What is aList + bList
c. What is aList * 2
'''
aList = [1,5,2]
bList=[9,2,3]
aList+bList
aList*2



'''
Qn 6:
a. Define a new dictionary with the months of the year as key, and the value 
   being the corresponding number of days in the month
'''
from datetime import datetime
import calendar


monthDict = {}
for month in range(1,13):
    monthDict[calendar.month_name[month]] = calendar.monthrange(2020, month)[1]


'''
Qn 7:
Instantiate a new Dictionary to be empty
Define this dictionary with the following content
Student Name(Key)     Score 1 (Value)
Binil                   78
Starly                  85
Ethan                   89
Jessica                 95 
Carson                  97

a. print the entire dictionary content
b. print the score of Carson
c. Add a new dictionary item with the following student and score: Daniele, 48
d. prints all the values of the dictionary
'''
newDict = {}
for name, score in zip(["Binil", "Starly", "Ethan", "Jessica", "Carson"], [78, 85, 89, 95, 97]):
    newDict[name] = score

print(newDict)
print(newDict["Carson"])
newDict["Daniele"] = 48
print(newDict)

'''
Qn 8
For the same dictionary, to the scores above, add a new Score 2 for each student.
Student Name(Key)     Score 2 (Value)
Binil                   88
Starly                  58
Ethan                   79
Jessica                 85 
Carson                  67
'''
Score2 = [88, 58, 79, 85, 67]
for i, item in enumerate(newDict.items()):
    newDict[item[0]] = item[1] + Score2[i]




'''
Qn 9:
For the same dictionary above, copy the content to another dictionary.
Changes to one dictionary should not affect the other.
'''
anotherDict = newDict.copy()




'''
Qn 10:
a. Define a tuple with variable aTuple to be containing 1, 4, 2, 5
b. Change the value available at the index value 2 of aTuple to 10
c. Can you convert a Tuple to a List? Convert a List to a Tuple
'''

aTuple =( 1, 4, 2, 5)
aTuple =( 1, 4, 10, 5)
aTuple.toList()
lst = list(aTuple)
tpl = tuple(lst)




