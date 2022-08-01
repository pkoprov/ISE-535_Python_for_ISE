# -*- coding: utf-8 -*-
"""
@author: bstarly

Read Section 1 Chapter 5 (FUNCTIONS) before attempting these exercises.

"""


# Qn 1 Write a program to create a function that simply squares and cubes any number passed to it and returns the value.
#The main program should then print the value to the console screen.
#The main program should also 'unpack' the tuple and print its contents.

def cubedNum(number):
    ansSqu = number * number
    ansCub = number * number * number 
    return ansCub, ansSqu # another way: return number * number * number 

#main program
num = float(input("Enter the number:"))
result = cubedNum(num)
print("The answer is : ", result)

#unpacking the tuple
resCub, resSqu = cubedNum(num)
print("The square of the number is ", resSqu)
print("The cube of the number is ", resCub)


#Qn 2 Write a function that takes the length and breadth of a rectangle.
#Return the area, the perimeter and if it is a rectangle or square.

def shapeMetrics(l, b):
    area = l * b
    perimeter = l + l + b + b
    
    if l==b:
        shape="Square"
    else:
        shape="Rectangle"
        
    return area, perimeter, shape

length = 100
breadth = 100
result = shapeMetrics(length,breadth)

print(f"The area is: {result[0]}")
print(f"The perimeter is: {result[1]}")
print(f"The shape is: {result[2]}")




#Qn 3 Write a function that counts the number of even numbers within a list defined by the user. 
#The user enters the numbers on the console, with a comma to separate the numbers. Report the total number of even numbers to the console screen. Example
#Input Enter the numbers (separated by a comma): 1,3,4,6,10,11,12
#Output There are 4 even numbers in the list

def chekEven(num):
  
    if num % 2 == 0:
        return True
    else:
        return False
    
#main program
numStr = input("Enter the values separated by comma:")
numStrList = numStr.split(',')
print(numStrList)

numList = [int(num) for num in numStrList]
print(numList)

count=0
for num in numList:
    res = chekEven(num)
    if res == True:
        count = count + 1

print("The total number even numbers is:", count)


#Qn 4 Write a function that takes 2 parameters to compute the area of a triangle.
#A = 1/2 (b * h). Return the value to the main program

def areaT(b, h):
    return 0.5*(b*h)

base = 10
height = 5
res = areaT(base, height)
print("The area of the triangle is:", res)




#Qn 5 Write a function that finds the maximum value of all the even numbers in a given list of integers.
def chekEven(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
numList = [64,34,22,35,87,88]

evenList = [num for num in numList if chekEven(num)==True]
print("The max of the even numbers are:", max(evenList))



#Qn 6 Write a function that converts two lists to a single dictionary. Given two lists such as
#keys = ["Binil", "Starly", "Sara", "Evan", "Rachel"]
#scores = [90, 99, 98, 80, 73]
#
#Return dictionary to main program and print the key and corresponding values of the dictionary

keys = ["Binil", "Starly", "Sara", "Evan", "Rachel"]
scores = [90, 99, 98, 80, 73]

studentScore={}
for name, score in zip(keys, scores):
    studentScore[name]=score

print("The contents of the dictionary:", studentScore)


#Qn 7 Write a program to merge the following list together so that it outputs all the scores of a given student in the form of a dictionary
#
#Student_Python_Scores=[{'Binil': 90, 'Starly': 80, 'Sara': 99, 'Rohan': 88},
#                       {'Binil': 70, 'Starly': 89, 'Sara': 99, 'Rohan': 77},
#                       {'Binil': 75, 'Starly': 70, 'Sara': 93, 'Rohan': 98}]
#
#The output should be a dictionary as follows:
#{'Binil':[90, 70], 'Starly':[80,89], 'Sara':[99,99], 'Rohan':[88,77]}
#
#Also compute the average scores for the student

def findAvg(scoreList):
    
    #also try out the sum() method of a list
    sumScore=0 
    for score in scoreList:
        sumScore = sumScore + score
    
    average = sumScore/len(scoreList)
    
    return average
    
Student_Python_Scores=[{'Binil': 90, 'Starly': 80, 'Sara': 99, 'Rohan': 88},
                       {'Binil': 70, 'Starly': 89, 'Sara': 99, 'Rohan': 77},
                       {'Binil': 75, 'Starly': 70, 'Sara': 93, 'Rohan': 98}]

modifiedDict={}
for record in Student_Python_Scores:
    for key, value in record.items():
        if key in modifiedDict.keys():
            modifiedDict[key].append(value)
        else:
            modifiedDict[key]=[value]

print("The contents of the dict is", modifiedDict)

for name, scoreList in modifiedDict.items():
    avg = findAvg(scoreList)
    print(f"The Student {name} scored an average of {avg}")

#8
#Search for a value in the dictionary below:
#studentScores={"Binil":[34,63,100], "Johanna":[33,22,77], "Evan":[66,21,97], "Ben":[100,5,10]}
#The values represents a list with scores for 3 exams = Exam 1, Exam 2 and Exam 3
#A: Check if anyone has scored a 100. Return a True
#B: Print all students who scored more than 50 in the 3rd exam    

studentScores={"Binil":[34,63,100], "Johanna":[33,22,77], "Evan":[66,21,97], "Ben":[100,5,10]}
found = False
for name, scoreList in studentScores.items():
    for score in scoreList:
        if score == 100:
            found=True
            break
    if scoreList[2] > 50:
        print(name)

if found:
    print("Wow, someone did score a 100")
else:
    print("Hmm, the exam was harder that I thought")
    

#9 Design a menu that has the following options. The menu must continuously be displayed as long as the user has not exited out of the program
#1) Enter the integers
#2) Odd or even
#3) Integer or Float
#4) Is it a Prime Number
#5) Factorial of Number
#6) Exit the Program

def oddEvenChk(number):
    if number % 2 == 0:
        res = "even"
    else:
        res = "odd"
    return res

def integFloatChk(number):
    if '.' in number:
        res = "float"
    else:
        res = "integer"
    return res

def primeChk(number):
    flag = False
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                flag = True
                break
    return flag

def factorial(number):
    fact = 1
    for i in range(1, number+1):
        fact = fact * i
    return fact

#MAIN PROGRAM
print("**** MY FUNCTION LIBRARY******")
print("1: Enter the Integer:")
print("2: Find Odd or Even")
print("3: Is it Integer or Float")
print("4: Is it Prime or Not")
print("5: Factorial of Number")
print("6: Exit the program" )
choice=0

while (choice!=6):
    choice = int(input("Enter your Choice:"))
    if choice == 1:
        number = input("Enter the integer: ")
    if choice == 2:
        res = oddEvenChk(int(number))
        print(f"The given number {number} is {res}")
    if choice == 3:
        res= integFloatChk(number)
        print(f"The given number {number} is {res}")
    if choice == 4:
        res = primeChk(int(number))
        if res:
            print(f"The given number {number} is not Prime")
        else:
            print(f"The given number {number} is Prime")
    if choice == 5:
        res = factorial(int(number))
        print(f"The given number {number} factorial is {res}")
    
print("Thank you for using my library")















