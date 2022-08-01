# exercise 1
# Write the following functions. Each of these functions should have a single parameter -- accepting a string as an
# argument. The function should only do what is specified:
# 1. Write a function that counts and returns the number of vowels in the string (A, E, I, O, U, a, e, i, o, u)


def count_vowels(string):
    count = 0
    for i in string:
        if i.lower() in "aeiou":
            count += 1
    return count


# 2. Write a function that counts and returns the number of consonants in the string.


def count_consonants(string):
    count = 0
    for i in string:
        if i.lower() in "bcdfghjklmnpqrstvwxyz":
            count += 1
    return count


# 3. Write a function that converts the string to all lowercase.


def lowercase(string):
    return string.lower()


# 4. Write a function that converts the string to all uppercase.


def uppercase(string):
    return string.upper()


# exercise 2
# Write a main program that performs the following steps:
def main():
    # A. Prompt the user to enter a string, and let them type it in. This could be an entire sentence, with the newline
    # indicating the end of the string.
    string = input("Enter a string: ")
    # B. Display the following menu:
    #     A Count the number of vowels in the string
    #     B Count the number of consonants in the string
    #     C Convert the string to uppercase
    #     D Convert the string to lowercase
    #     E Enter another string
    #     M Display this menu
    #     X Exit the program
    print("A Count the number of vowels in the string")
    print("B Count the number of consonants in the string")
    print("C Convert the string to uppercase")
    print("D Convert the string to lowercase")
    print("E Enter another string")
    print("M Display this menu")
    print("X Exit the program")
    # C. Enter a loop, allowing the user to type in a menu choice from above each time. Loop should continue
    # until the user enters the command to exit. Upper and lowercase letters should be allowed for the menu choices.
    #     a. When the A or B commands are entered (counting vowels or consonants), call the corresponding function, then
    #     print the result
    #     b. When C or D menu options are chosen, just call the appropriate function to convert the string and print the
    #     result to the console.
    #     c. When E is chosen, allow a new string to be typed -- this will replace the previous one. And the menu should
    #     be re-displayed back to the console.
    #     d. The menu should only be displayed once at the start, and then again whenever the E or M option is selected

    while True:
        choice = input("Enter a choice: ")
        if choice.upper() == "A":
            print(count_vowels(string))
        elif choice.upper() == "B":
            print(count_consonants(string))
        elif choice.upper() == "C":
            print(uppercase(string))
        elif choice.upper() == "D":
            print(lowercase(string))
        elif choice.upper() == "E":
            string = input("Enter a string: ")

        elif choice.upper() == "M":
            print("A Count the number of vowels in the string")
            print("B Count the number of consonants in the string")
            print("C Convert the string to uppercase")
            print("D Convert the string to lowercase")
            print("E Enter another string")
            print("M Display this menu")
            print("X Exit the program")
        elif choice.upper() == "X":
            break


# exercise 3
# Write a python to accept the birth date of the user (in mm/dd/yyyy format) and calculate the number of days between
# current system date and the birth date. Ensure that the user has selected a date prior to system date.
# Check if the user has entered it in the correct format including the ‘/’ within the string.
# Print errors if any to the screen. If errors are seen, go back to asking the user to renter the date.


def years_from_birthdate():
    import datetime
    while True:
        birth_date = input("Enter your birth date (mm/dd/yyyy): ")
        if birth_date.count("/") == 2:
            birth_date = birth_date.split("/")
            if len(birth_date[0]) == 2 and birth_date[0] and len(birth_date[1]) == 2 and len(birth_date[2]) == 4:
                try:
                    birth_date = [int(i) for i in birth_date]
                except ValueError as er:
                    print("ValueError: {}: date should be numeric".format(er))
                    continue
                try:
                    birth_date = datetime.date(birth_date[2], birth_date[0], birth_date[1])
                except ValueError as er:
                    print("ValueError: {}".format(er))
                    continue
                today = datetime.date.today()
                if birth_date > today:
                    print("You have entered a date in the future. Please enter a valid date.")
                else:
                    print(today - birth_date)
                    break
            else:
                print("Please enter a date in a valid format: mm/dd/yyyy")  # if the date is not in the correct format
        else:
            print("Please enter a date in a valid format: mm/dd/yyyy")  # if the date is not in the correct format


# exercise 4
# The future value of money, relates how much a current investment will be worth in the future, assuming a constant
# interest rate.
# FV = PV * (1 + Int)^n
# Where FV = future value; PV = Present value; Int = interest rate per compounding period expressed as a fraction,
# ex 5% as 0.05; n = compounding periods
# Write a Python function to calculate FV with the three inputs (PV, Int, n). Dr Starly has three options to decide
# on where to invest his $10,000, as given by choice options in the table.
# Generate an output that displays the total value in his account every year until the maturity year
# for each of the 3 institutions.

# Financial Institution | Int. Rate per month | Years
# NC Capital Bank       | 2.3%                | 3
# Mutual funds          | 2.6%                | 5
# Allie Bank            | 2.5%                | 4


def future_value(PV, Int, n):
    for i in range(n):
        FV = PV * (1 + Int / 100 * 12) ** (i + 1)
        print("Year {}: ${:.2f}".format(i + 1, FV))


# exercise 5
# Consider the behavior of a freely falling object under the influence of gravity. The position of the object is given
# by    d = 0.5 * g * t^2
# d = distance object travels; g = acceleration due to gravity; t = elapsed time.
# The script can set the value of ‘g’ assuming Earth’s gravity. Ask the user to enter the start time, end time
# and the desired time increments. Print the value of d, during each time step. Use consistent system of units.


def falling_object(start_time, end_time, time_increment):
    g = 9.8
    cur_time = start_time
    while cur_time < end_time:
        d = 0.5 * g * cur_time ** 2
        print("At time {} the object is {} meters from the starting point".format(cur_time, d))
        cur_time += time_increment


# exercise 6
# Given a list of students with the following scores received as part of the Python class. Write a function that
# will return the alphabetical grade for the following grading scale: A: >=90, B:80-89, C: 70-79, D: 60-69, F: <59.
# Implement a numeric look up table. Your code script MUST NOT have a series of IF or IF ELSE conditions that assigns
# the letter grade based a range check. For example, these statements are not allowed:
# If (score>80) and (score<89):
# Grade=’A’
# If (score<50):
# Grade=’F’


def grade_letter(score):
    lookup = {}
    for i in [i for i in range(90, 101)]:
        lookup[i] = "A"
    for i in [i for i in range(80, 90)]:
        lookup[i] = "B"
    for i in [i for i in range(70, 80)]:
        lookup[i] = "C"
    for i in [i for i in range(60, 70)]:
        lookup[i] = "D"
    for i in [i for i in range(0, 60)]:
        lookup[i] = "F"
    return lookup[score]


name_score = {"Name": ["Binil", "Starly", "Ethan", "Evan", "Rachel", "Michelle", "Jayden", "Ben"],
              "Score": [90, 40, 88, 87, 95, 79, 82, 48]}
result = [(name_score["Name"][i], name_score["Score"][i], grade_letter(name_score["Score"][i]))
          for i in range(len(name_score["Name"]))]

print(result)
