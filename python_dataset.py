import pandas as pd

filename = 'diabetes.csv'

df = pd.read_csv(filename)

"""print("Head Function displays 5 rows")
print(df.head()) #5 rows of data

print("\nHead Function displays specified number of rows")
print(df.head(3)) #specified 3 rows of data


print("\nDescribe function displays the Count, mean, min, max, 25, 50, 75")
print(df.describe())

print("\nRound function helps to round off to 3dps")
print(df.describe().round(3))"""

#we can work wit individual columns too
Age = df['Age']
print(Age)

print("\nMean Age is ", Age.mean().round(3))
print("\nMin Age is ", Age.min())

print("\nMax Age is ", Age.max())

print("\nMedian Age is ", Age.median())

print("\nMode Age is ", Age.mode())

print("\nVariance in age is ", Age.var())


print("\nStandard Deviation in age is ", Age.std())


