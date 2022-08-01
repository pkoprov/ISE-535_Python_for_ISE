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

nameList = ['Binil', 'Rachel', 'Ethan', 'Evan', 'Starly', 'Sam']

print(f"b. The length of the list is {len(nameList)}")

print(f"c. The 3rd item in the list is {nameList[2]}")

print(f"d. The last item in the list is {nameList[5]}")
print(f"d. The last item in the list is {nameList[-1]}")

print("e. The entire list is:",*nameList)
print("e. The entire list is:",nameList)


'''
Qn 2:
a. Initiate a new Number list and assign it to be empty.
b. Now append the list with numbers 1,3,5,6,7,8,9,10,11,13,15,17,20
c. Print the number that is in the middle of the list.
d. Print the contents of the list that lies between the 4th and 10th index value
e. Reorder the list to be in the reverse order and print the contents to confirm it.
f. find the maximum value in the list
'''

numList = []

numList.append(1)
numList.append([3,5,6,7,8,9,10,11,13,15,17,20])

print(numList)

numList = [1,3,5,6,7,8,9,10,11,13,15,17,20]
midIndex = int(len(numList)/2)

print(numList[midIndex])


#slicing
print("Contents within 4th and 10th index values", numList[4:11])


revList = numList[::-1]
print("Contents of new List is", *revList)

revSkipList = numList[::-2]
print("Contents of new skipped List is", *revSkipList)





'''
Qn 3:
a.  Initiate the following list chocBrandList=["Mars", "Snickers", "Bounty", "Twix"]
b. print the length of the list
c. copy the contents of this list to a new List called newChocList
d. To the original chocBrandList, add the following String - "Lion Bar"    
e. print the contents of the newChocList. Comment on the results obtained
    
'''

chocBrandList=["Mars", "Snickers", "Bounty", "Twix"]
print("The length of the list is", len(chocBrandList))

newChocList = chocBrandList #copied the contents to the new list

chocBrandList.append("Lion Bar")
print("The original Choc List is: ", chocBrandList)

print("New Choc List is ",newChocList)



'''
Qn 4:
a. Define a new list aList = [1, 5, 3, 6, 2]
b. Multiply each value in this list by 2
c. Print the new list
'''

aList = [1, 5, 3, 6, 2]
#newList = aList * 2

aList[0] = aList[0] * 2
aList[1] = aList[1] * 2
aList[2] = aList[2] * 2
aList[3] = aList[3] * 2
aList[4] = aList[4] * 2
print(aList)





'''
Qn 5: 
a. Define a list aList = [1,5,2] and bList=[9,2,3]
b. What is aList + bList
c. What is aList * 2
'''

aList = [1,5,2]
bList=[9,2,3]

cList = aList + bList

print(cList) #concatenate the lists


aString = "binil"
bString = "starly"
print(aString+bString)

print(aString[5])


'''
Qn 6:
a. Define a new dictionary with the months of the year as key, and the value 
   being the corresponding number of days in the month
'''

yearDict = {
            "Jan":31, 
            "Feb":28, 
            "Mar":31,
            "Apr":30
            }


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

studentScore={}
studentScore={
                "Binil":78,
                "Starly":85,
                "Ethan":89,
                "Jessica":95,
                "Carson":97
            }

print(studentScore)

print("Carson's score is: ", studentScore["Carson"])

studentScore["Daniele"] = 48

print(studentScore)

studentScore["Daniele"] = 88

print(studentScore)

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


studentScore={}
studentScore={
                "Binil":[78,88],
                "Starly":[85,58],
                "Ethan":[89,79],
                "Jessica":[95,85],
                "Carson":[97,67]
            }



'''
Qn 9:
For the same dictionary above, copy the content to another dictionary.
Changes to one dictionary should not affect the other.
'''
studentScore={
                "Binil":78,
                "Starly":85,
                "Ethan":89,
                "Jessica":95,
                "Carson":97
            }

newStudentScore = studentScore
print("Original Dict:", studentScore)

studentScore["Binil"]=100
print("Original Dict:", studentScore)
print("Copied Dict:", newStudentScore)

new2StudentScore  = studentScore.copy()


studentScore["Binil"]=0
print("Original Dict 2:", studentScore)
print("Shallow Copied Dict 2 :", new2StudentScore)


studentScore={
                "Binil":[78,88],
                "Starly":[85,58],
                "Ethan":[89,79],
                "Jessica":[95,85],
                "Carson":[97,67]
            }

new2StudentScore  = studentScore.copy()
studentScore["Binil"][0]=0
print("Original Dict 2:", studentScore)
print("Shallow Copied Dict 2 :", new2StudentScore)



'''
Qn 10:
a. Define a tuple with variable aTuple to be containing 1, 4, 2, 5
b. Change the value available at the index value 2 of aTuple to 10
c. Can you convert a Tuple to a List? Convert a List to a Tuple
'''


aTuple=(1,4,2,5)
aTuple[2]=10
print(aTuple) #this will not work


aTuple=(1,4,2,5)
aList = list(aTuple)
aList[2]=10
print(aList)

aTuple = tuple(aList)
print("Data Type is:", type(aTuple))








