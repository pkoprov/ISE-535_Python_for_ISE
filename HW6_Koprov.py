import time

print("Excersize 1")
# Create one random integer array, aVec, containing 20 values ranging from 0 to 100. Generate a random float value, b,
# between 0 and 100. Find the index in aVec whose value is closest to b. Print also the value within aVec through
# the index.

import numpy as np

aVec = np.random.randint(0, 100, 20)
b = np.random.random() * 100
print(aVec, '\n', b)
closest_ind = np.argmin(np.abs(aVec - b))
print("The index in aVec whose value is closest to b is %s" % closest_ind)

print("Excersize 2")
# Write a Python program to create random vector with values between 0 and 1 of size 15 and replace the maximum value
# within it by -1.

vec = np.random.random(15)
print(vec)
vec[np.argmax(vec)] = -1
print(vec)

print("Excersize 3")

# Replace all the positions at which non-zeros exist in the given matrix, A to -1. The given 2D array is
# A = [1 0 1 0 1 1 1 0 1 0 0
#      0 1 0 1 1 0 1 0 1 1 1
#      0 0 0 0 0 0 0 0 1 1 1]

A = np.array([[1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
              [0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1],
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]])

A = np.where(A != 0, -1, A)
print(A)

print("Excersize 4")
# Write a numpy program that creates a 1D vector with random integer values ranging from 10 to 100 with 20 elements.
# Further, for each value that is below the mean of all the values in the vector, replace those values with 0.

vect = np.random.randint(10, 100, 20)
print(vect)
mean = np.mean(vect)
print(mean)
vect[vect < mean] = 0
print(vect)

print("Excersize 5")


# Consider an elementary system of three linear equations:
# x+2y+z=2,
# 2x+6y+z=7,
# x+y + 4z = 3,
# Solve for x, y and z using a python program using the numpy library.


def solve_system(A, b):
    return np.linalg.solve(A, b)


A = np.array([[1, 2, 1], [2, 6, 1], [1, 1, 4]])
b = np.array([2, 7, 3])
print(solve_system(A, b))

print("Excersize 6")
# Randomly generate two objects. The first object is a 1D array, a vector ‘v’ of 10 integer elements. Randomly
# generate a second 2D array, B, a matrix of 10 x 5 elements. Subtract the 1d array, ‘v’ from the 2d matrix B, such
# that each item of v subtracts from respective column of A. The resulting matrix must still be of shape 10 x 5.
# The values in the vector randomly range from (1, 100)

v = np.random.randint(1, 100, 10)
print("v= ", v)
B = np.random.randint(1, 100, (10, 5))
print("B= ", B)

X = (B.transpose() - v).transpose()
print(X)

print("Excersize 7")
# A cleaning services company compiled the following data related to the annual profit of the firm to its annual
# Facebook advertising campaign (measured in thousands) as shown in the table below
# Advertising Expenditure 12 14 17 21 26 30
# Profit 60 70 90 100 100 120

ad_expend = np.array([12, 14, 17, 21, 26, 30])
profit = np.array([60, 70, 90, 100, 100, 120])

# a) Find the best least squares fit to the data in the form of a straight line given by y = mx + c by writing
# a numpy program.

print("a)")


def best_fit(x, y):
    return np.polyfit(x, y, 1)


print(best_fit(ad_expend, profit))

# b) Plot the points and least square fit line using matplotlib.
print("b)")
import matplotlib.pyplot as plt

plt.plot(ad_expend, profit, 'o')
plt.plot(ad_expend, best_fit(ad_expend, profit)[0] * ad_expend + best_fit(ad_expend, profit)[1])
plt.show()

# c) Calculate the profit if the company allocates in its next FB campaign with a $50,000 budget allocation.
# Report the value in $ currency.
print("c)")
print(best_fit(ad_expend, profit)[0] * 50 + best_fit(ad_expend, profit)[1])

print("Excersize 8")
# The US Social Security Administration releases baby names given by parents from the Years 1880 up until 2022.
# The dataset zip file can be downloaded from :
# Baby Names from Social Security Card Applications - National Data - CKAN
# (https://catalog.data.gov/dataset/baby-names-from-social-security-card- applications-national-data)
# Answer the following questions in regard to the Baby Names Dataset (20).
# a. Total number of records across all years (1880 – 2021).
import pandas as pd
import os


records = 0
for file in os.listdir(os.getcwd() + "/names"):
    if file.endswith(".txt"):
        with open(os.getcwd() + "/names/" + file, 'r') as csv:
            records += len(csv.readlines())

print("a) Total number of records across all years (1880 – 2021) = ", records)

# b. Compute the number of times that each name was used, separately for boys and girls across all years. For example,
# the output should be
# Sex Name Total
# F Aabha 21


total_df = pd.DataFrame(columns=["Name", "Sex", "Total"]).set_index(["Sex", "Name"])
for file in os.listdir(os.getcwd() + "/names"):
    if file.endswith(".txt"):
        print("Year", file[3:-4])
        df = pd.read_csv(os.getcwd() + "/names/" + file, names=["Name", "Sex", "Total"]).set_index(["Sex","Name"])
        total_df = pd.concat([total_df, df]).groupby(["Sex","Name"]).sum()

print("b) The number of times that each name was used, separately for boys and girls across all years is in 'total_df'")
print(total_df)

# c. Display a single plot showing the popularity of the name 'Harper', 'Evelynn', 'Evan', 'Ethan' across the years.
import matplotlib.pyplot as plt
print("c)")

data = {"year":[], 'Harper': [], 'Evelynn': [], 'Evan': [], 'Ethan': []}
for n, file in enumerate(os.listdir(os.getcwd() + "/names")):
    if file.endswith(".txt"):
        print("Year", file[3:-4])
        data["year"] += [int(file[3:-4])]
        df = pd.read_csv(os.getcwd() + "/names/" + file, names=["Name", "Sex", "Total"])
        for name in ['Harper', 'Evelynn', 'Evan', 'Ethan']:
            data[name] += [df["Total"].loc[df["Name"] == name].sum()]

df = pd.DataFrame(data)
[plt.scatter(df["year"], df[name], label = name) for name in ['Harper', 'Evelynn', 'Evan', 'Ethan']]
plt.legend()

# d. Compute the 10 most popular names for all Male ‘M’ names and Female – ‘F’ for every year.

top10y = pd.DataFrame(index=range(10))
columns = []
for file in os.listdir(os.getcwd() + "/names"):
    if file.endswith(".txt"):
        year = file[3:7]
        print("Year", year)
        df = pd.read_csv(os.getcwd() + "/names/" + file, names=["Name", "Sex", "Total"])
        top10M = df["Name"][df["Sex"] == "M"].head(10).reset_index(drop=True).to_frame()
        top10M.columns = ["M"]
        top10F = df["Name"][df["Sex"] == "F"].head(10).reset_index(drop=True).to_frame()
        top10F.columns = ["F"]
        top10y = pd.concat([top10y, top10M, top10F], axis=1)
        for i in ["M", "F"]: columns.append((year, i))

top10y.columns = pd.MultiIndex.from_tuples(columns)

print("d) 10 most popular names for all Male ‘M’ names and Female – ‘F’ for every year:")
print(top10y)
