# -*- coding: utf-8 -*-
"""
@author: bstarly

"""

#1
#Write a program to get a list of dates between two dates entered 
#by the user in mm/dd/yyyy. 
#Check also if the first date is less than the second date.

from datetime import date, timedelta

def returnDT(dateInput):
    dateList = dateInput.split("/")
    month = int(dateList[0])
    day = int(dateList[1])
    year = int(dateList[2])
    dayDT = date(year, month, day)

    return dayDT
    

firstDay = input("Enter the first date in mm/dd/yyyy:")
secondDay = input("Enter the second date in mm/dd/yyyy:")

firstDT = returnDT(firstDay)
secondDT = returnDT(secondDay)

if (firstDT < secondDT):
    diff = secondDT - firstDT
    daydiff = diff.days
    print(daydiff)
    
    for i in range (0, daydiff+1):
        print(firstDT+timedelta(i))
else:
    print("Wrong data entry")    



#2
#Write a Program to Write The Given Strings to a File
#n1='\n'
#lines = 'Binil', n1, 'Starly', 'is', n1, 'teaching', n1, 'Python', n1, 'today'

n1='\n'
lines = 'Binil', n1, 'Starly', 'is', n1, 'teaching', n1, 'Python', n1, 'today'

file = open("myfirstfile.txt", 'a') #w = write a=append r=read
file.writelines(lines)

file.close()

#3
#Write a program that removes all empty lines from the attached 
#text file “SampleText.txt’ and copy the contents to a new file 
#without the empty lines.

rfile = open(r"Week_5_Data\SampleTextFile.txt", 'r')
ofile = open(r"Week_5_Data\NewTextFile.txt", 'w')
wordList=[]

for everyline in rfile:
    words = everyline.split()
    for word in words:
        wordList.append(word)

for word in wordList:
    ofile.write(word)
    ofile.write(' ')

ofile.close()



#4
#For the contents in the file, count the number of words in a 
#text file and print the unique words in the file
#if on a MAC, read it as a .rtf file
rfile = open(r"Week_5_Data\SampleTextFile.txt", 'r')
wordList=[]

for everyline in rfile:
    words = everyline.split()
    for word in words:
        word = word.strip("?.(),")
        wordList.append(word)

uniqueList=[]

for word in wordList:
    if word not in uniqueList:
        uniqueList.append(word)
    
print(uniqueList)



#5
#Write a function CodeWord(filename) that reads a file ‘CNCFile.txt’ containing a large amount of text.
#For every instance of the word – CNC contained in the file, replace this word with the word – ‘XYZ’. Output this new text to another file – “CodedText.txt”.
#Also output the number of times the word – CNC appeared in the file to the console screen.

rfile = open("Week_5_Data/CNCFile.txt", 'r')
ofile = open("Week_5_Data/XYZFile.txt", 'w')

wordList=[]
for line in rfile:
    words = line.split()
    for word in words:
        word = word.strip("?.,()")
        if word == "CNC": #alternate if "CNC" in word:
            word = "XYZ"
        wordList.append(word)

for word in wordList:
    ofile.write(word+" ")    
    
ofile.close()




#Qn 6
#A: Extract the content of the zip file.
#B: Count the number of units sold
#C: max order sold by each country in the file and store the result in a dictionary
#D: Output a JSON file that lists each Item_Type and the countries that sold those items
#   as a dictionary, in the following format
#   ItemType: List of countries that sold that item 


import zipfile as zp
import csv, json

path = "Week_5_Data/5000-Sales-Records.zip"

zipfile = zp.ZipFile(path, 'r')
fileList = zipfile.namelist() #contains the name of the files in the zip

zipfile.extract(fileList[0], "Week_5_Data//")
unitsold=0
with open("Week_5_Data//"+ str(fileList[0])) as file:
    content = csv.reader(file)
    next(content)
    for row in content:
        unitsold = unitsold + int(row[8])

print("Total units sold ={:,}".format(unitsold))

#which Country had the highest revenue
maxRev=0
with open("Week_5_Data//"+ str(fileList[0])) as file:
    content = csv.reader(file)
    next(content)
    for row in content:
        rev = float(row[11])
        if maxRev < rev:
            maxRev = rev
            maxCountry = row[1]

print("Max Revenue ${:,} was obtained by {}".format(maxRev, maxCountry))

#C

#D
itemTypeDict={}
with open("Week_5_Data//"+ str(fileList[0])) as file:
    content = csv.reader(file)
    next(content)
    
    for row in content:
        if row[2] not in itemTypeDict.keys():
            itemTypeDict[row[2]] = [row[1]]
        else:
            itemTypeDict[row[2]].append(row[1])
    

with open("Week_5_Data//outputfile.json", 'w') as outfile:
    json.dump(itemTypeDict, outfile)
            








