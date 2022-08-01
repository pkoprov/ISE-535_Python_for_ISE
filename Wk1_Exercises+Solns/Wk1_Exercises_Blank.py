# -*- coding: utf-8 -*-
"""
@author: bstarly
"""

'''
Complete Watching Section 1 - Python Essentials - 1
 - Chapter 1.1 - 1.8 : Getting Started
 - Chapter 2.1 - 2.3 : Data Types (Numeric, Boolean and String)
before attempting these exercises

'''

'''
Qn 1:
What is wrong with the following lines of code. The computer is dumb and is wanting
the human to do basic subtraction. It then takes the number and asks the user
to multiply it by 2. The following code is wrong. The Computer asks you for help!!
'''

number = int(input("What is 9 subtracted from 15:"))
newNumber = number * 2
print('The final result is:{}'.format(newNumber)) # using the format command



'''
Qn 2:
Write a python script that will ask the user his/her age and the script
will output the year in which the person was born.
	
'''

age = int(input("What is your age: "))
from datetime import datetime
print("You were born in the year: {}".format(datetime.now().year - age))


'''
Qn 3:
Write a python program which uses the formula C = (5/9)*(F-32) to print the Fahrenheit
temperatures as Celsius equivalents. Ask the user to input temperature in F and the code should
output the value in the Celsius scale. The result should be in the following format:
<write the value>F is <> celsius

'''
fahr = int(input("What is the temperature in Fahrenheit: "))
print("{}F is {} Celsius".format(fahr, (5/9)*(fahr-32)))





'''
Qn 4:
a. Accept the user's first name and last name in two separate variables.
b. Print the output as : Hi, <first name> , your <last name> is 'awesome'	

'''
name = input("What is your first name: ")
lastName = input("What is your last name: ")
print("Hi, {} , your {} is awesome".format(name, lastName))






'''
Qn 5:
There are 100 jelly beans. The Starly family has 4 members. Myself, my wife and 2 young kids. The kids 
love jelly beans. Starly himself has a sugar tooth and needs jelly beans himself.
His wife isn't into jelly beans. But she will eat whatever remains"

a. Write a script that calculates how many whole jelly beans that each kid + Prof Starly gets.
b. Also calculate how many jelly beans his wife gets if there are any remaining.

'''
total = 100
print("Each kid + Prof Starly gets {} beans".format(total//3))
print("His wife gets {} beans".format(total%3))













