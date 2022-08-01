print("Exercise 1")
# 1) Write a python program to assign two integer and one float variable to 20, 15, and 22.6 respectively.
# The program should then print these values to the console screen
var1 = 20
var2 = 15
var3 = 22.6
print(var1, var2, var3)
print("*********************************************************")


print("Exercise 2")
# 2) Write a python program to prompt the user to input her/his name and age. Print the values back to
# the console output screen in the format as shown below.
# Input:
# Enter your name: Binil
# Enter your age: 43.0
# Output:
# Binil, you are 43 years old
# (Note that if the user enters a floating point value, only an integer should be displayed as the
# output. Truncate any decimal values)
name = input("Enter your name: ")
age = input("Enter your age: ")
print("{}, you are {} years old".format(name, int(age)))
print("*********************************************************")

print("Exercise 3")
# 3) Write a python program which uses the formula C = (5/9)*(F-32) to print the Fahrenheit
# temperatures as Celsius equivalents. Ask the user to input temperature in F and the code should
# output the value in the Celsius scale. Search for “Eval” method in Python. Perhaps this might be
# more useful then type casting the incoming input variable.
temp_f = float(input("Enter the temperature in Fahrenheit: "))
temp_c = (5/9)*(temp_f-32)
print("The temperature in Celsius is: ", temp_c)
print("*********************************************************")


print("Exercise 4")
# 4) Find the weight of a car in Newton whose mass is input by the user. A solved exercise is as follows:
# User inputs 1400 kg; W = m * g = 1400 * 9.81 = 13734N;
# Write a python program that asks the user for the input for mass in kg. Provide an output formatted
# as shown below:
# Given Input (kg): 1400
# Weight (N): 13734
weight_kg = float(input("Given Input (kg): "))
weight_N = weight_kg * 9.81
print("Weight (N):", weight_N)
print("*********************************************************")


print("Exercise 5")
# 5) Write a python program to compute the perimeter and area of a rectangle from user provided
# inputs. Example as follows
# Input
# Enter height of Rectangle in inches: 5.0
# Enter width of Rectangle in inches: 8.0
# Output:
# The area of the rectangle is: 40.0 sq. in
# The perimeter of the rectangle is: 26.0 sq. in
height = float(input("Enter height of Rectangle in inches: "))
width = float(input("Enter width of Rectangle in inches: "))
area = height * width
perimeter = 2 * (height + width)
print("The area of the rectangle is: ", area, "sq. in")
print("The perimeter of the rectangle is: ", perimeter, "sq. in")
print("*********************************************************")