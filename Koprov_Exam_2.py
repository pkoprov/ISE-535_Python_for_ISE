# Question 1
print("Question 1")
for i in range(1,1001,1):
    if i %100 == 0:
        print("Loop reached", i)

print("End of loop")
print("*********************************************************\n")

# Question 2
print("Question 2")
# a)
with open("Exam_2_Files/Enrolled.csv","r") as file:
    next(file)
    data = file.readlines()
    data_list = []
    for line in data:
        line = line.split(",")
        if line[1] == "":
            continue
        else:
            data_list.append(line)

# b)
yes = 0
for i in data_list:
    if i[1] == "Yes":
        yes += 1


print("Number of students who registered with yes:", yes)

# c)
print("IDs of those who registered with 'no':")
for i in data_list:
    date = i[2].split("/")
    if i[1] == "No" and int(date[0]) >= 7 and int(date[1]) >= 1 and int(date[2]) >= 2020:
        print(i[0])
print("*********************************************************\n")

# Question 3
print("Question 3")
# a)
import os


folder = os.listdir("Exam_2_Files/Exam2-Abstracts_Collector")

# b)
files = []
for i in folder:
    if os.path.isdir("Exam_2_Files/Exam2-Abstracts_Collector/" + i):
        sub_f_files = os.listdir("Exam_2_Files/Exam2-Abstracts_Collector/" + i)
        for file in sub_f_files:
            if ".json" in file:
                files.append(file)

print("Number of json files:", len(files))

# c)
import json


abstr_list = []
for i in folder:
    if os.path.isdir("Exam_2_Files/Exam2-Abstracts_Collector/" + i):
        sub_f_files = os.listdir("Exam_2_Files/Exam2-Abstracts_Collector/" + i)
        for file in sub_f_files:
            if ".json" in file:
                with open("Exam_2_Files/Exam2-Abstracts_Collector/" + i + "/" + file, "r") as f:
                    data = json.loads(f.read())
                    abstr_list.append(data['abstract'])

# d)
final_list = []
for i in folder:
    if os.path.isdir("Exam_2_Files/Exam2-Abstracts_Collector/" + i):
        sub_f_files = os.listdir("Exam_2_Files/Exam2-Abstracts_Collector/" + i)
        for file in sub_f_files:
            if ".json" in file:
                with open("Exam_2_Files/Exam2-Abstracts_Collector/" + i + "/" + file, "r") as f:
                    data = json.loads(f.read())
                    final_list.append(file + ": " + data['abstract'])

for i in final_list:
    print(i)
print("*********************************************************\n")

# Question 4
print("Question 4")
# a)
with open("Exam_2_Files/DrinksData.json", "r") as file:
    data = json.loads(file.read())

# b)
print("Name of products that were sold more than 200:")
for i in data:
    if i['quantity'] > 200:
        print(i['product_name'])

# c)
inv_dict = {}
for i in data:
    try:
        inv_dict[i["supplier"]] += i["invoice_amount"]
    except:
        inv_dict[i["supplier"]] = i["invoice_amount"]

print("\nInvoice list:")
for key, value in inv_dict.items():
    print(key + ":", value)

print("*********************************************************\n")

# Question 5
print("Question 5")
# a)

with open("Exam_2_Files/From_To.csv", "r") as file:
    next(file)
    data = file.readlines()

# b)
unique_IDs = []
for row in data:
    row = row.replace('\n', '').split(",")
    for id in row:
        if id not in unique_IDs:
            unique_IDs.append(id)

print("Unique IDs:")
for id in unique_IDs:
    print(id)

# c)
IDs = []
for row in data:
    row = row.replace('\n', '').split(",")
    for id in row:
        IDs.append(id)

for id in unique_IDs:
    print("Number of occurances of id", id + ":",IDs.count(id))