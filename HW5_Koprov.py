# exercise 1
print("exercise 1")
# Read the file ‘grades.csv’. Write code that finds and displays the 5 student IDs and their corresponding grades
# who received the lowest grades in the class. Some students have not appeared for the exam, but they are not to be
# treated as 0. They need to be simply skipped from the computation. (20 points)


def lowest_grade(file_name):
    import csv
    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        IDs = []
        grades = []
        for row in csv_reader:
            if row[1] != "":
                IDs.append(row[0])
                grades.append(int(row[1]))
        for i in range(5):
            ind = grades.index(min(grades))
            print("{} has the {} lowest grade of {}".format(IDs[ind], i+1, grades.pop(ind)))

lowest_grade('HW5_Files/grades.csv')
print("*****************************************************************************************")

print("exercise 2")
# exercise 2
# Open and read the contents of the file – ‘2_NoofParts_assem.txt’. Perform the following (20 points):
# a) Calculate how many entries are available in that file excluding the header.


def no_of_parts(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        print("There are {} entries in the file".format(len(lines)-1))

no_of_parts('HW5_Files/2_NoofParts_assem.txt')

# b) Calculate the sum of all parts from each file. Essentially, finding the sum of all values contained
# in the 2nd column of the file.


def sum_of_parts(file_name):
    with open(file_name, 'r') as file:
        next(file)
        lines = file.readlines()
        sum = 0
        for line in lines:
            try:
                sum += int(line.split('\t')[1])
            except:
                pass
        print("The sum of all parts is {}".format(sum))

sum_of_parts('HW5_Files/2_NoofParts_assem.txt')


# c) Extract the part ID that has the largest associated no. of parts from the entire list.

def max_parts(file_name):
    with open(file_name, 'r') as file:
        next(file)
        lines = file.readlines()
        max_parts = 0
        for line in lines:
            try:
                if int(line.split('\t')[1]) > max_parts:
                    max_parts = int(line.split('\t')[1])
                    max_parts_id = line.split('\t')[0]
            except:
                pass
        print("The part with the largest number of parts is {}: {} parts".format(max_parts_id, max_parts))

max_parts('HW5_Files/2_NoofParts_assem.txt')


print("*****************************************************************************************")

print("exercise 3")
# exercise 3
# Open the files contained in the .zip file – “3_Jobs_Completed_log.zip”. Scan the files for the line that starts
# with the word string – “Jobs Completed.. ”. Extract the number associated with this line and for all instances
# that this word string appears across all log files, count the total sum across all files within the .zip file.
# (30points)
# For example:
# Jobs Completed.. 10 2018-09-04 08:21:28.503153
# Extract the number 10 from this sentence which signifies the total number of jobs completed at the point in time.
# Find for all instances in which the string - ‘Jobs Completed’ appears, find the total number of jobs completed by
# adding the numbers from across the provided log files.


def jobs_completed(file_name):
    import zipfile
    sum = 0
    with zipfile.ZipFile(file_name, 'r') as zip_file:
        for file in zip_file.namelist():
            with zip_file.open(file) as f:
                for line in f:
                    if line.startswith(b'Jobs Completed..'):
                        sum += int(line.decode('utf-8').split(' ')[2])
    print("The total number of jobs completed is {}".format(sum))


jobs_completed("HW5_Files/Jobs_Completed_log.zip")

print("*****************************************************************************************")

print("exercise 4")
# exercise 4
# Read the file ‘grades_2.csv’ into an appropriate data structure.
# 1) Write code that finds and displays the average score of all the students across the three exams.


def average_score(file_name):
    import csv
    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        IDs = []
        grades = []
        for row in csv_reader:
            IDs.append(row[0])
            for grade in row[1:]:
                try:
                    grades.append(int(grade))
                except:
                    pass

        print("The average score of all students is {}".format(sum(grades)/len(grades)))

average_score("HW5_Files/grades_2.csv")

# 2) Find the Student ID that scored the maximum in each of the respective exams (output must be 3 values).
# Exam entries with an empty value can be considered as ZERO. (30points)


def max_score(file_name):
    import csv
    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        IDs = []
        grades = []
        for row in csv_reader:
            IDs.append(row[0])
            grades.append(row[1:])
        exam_1_max = exam_2_max = exam_3_max = 0
        for row in grades:
            if "" in row:
                row[row.index('')] = 0
            if int(row[0]) > exam_1_max:
                exam_1_max = int(row[0])
                exam_1_max_id = IDs[grades.index(row)]
            if int(row[1]) > exam_2_max:
                exam_2_max = int(row[1])
                exam_2_max_id = IDs[grades.index(row)]
            if int(row[2]) > exam_3_max:
                exam_3_max = int(row[2])
                exam_3_max_id = IDs[grades.index(row)]
        print("The student with the highest score in exam 1 is {} with a score of {}".format(exam_1_max_id, exam_1_max))
        print("The student with the highest score in exam 2 is {} with a score of {}".format(exam_2_max_id, exam_2_max))
        print("The student with the highest score in exam 3 is {} with a score of {}".format(exam_3_max_id, exam_3_max))


max_score("HW5_Files/grades_2.csv")
