import pandas as pd

df = pd.read_csv('Sales.csv')

"""print(df.head())

print(df.describe())
"""

"""
1) How many different types of items did each student create for the bake sale? Which student provided the most Items?

2) What was the total quantity of baked goods sold, by item? Which item sold the largest quantity?

3) What were the total profits generated by each Item? Which Item generated the most total profit?

4) Which student sold the largest quantity of items?

5) Which student generated the most total profit?

6) How much money has the club earned overall by the end of Day 4? How much more do they need to earn on Day 5 to meet their goal?

"""


# Let us first set the item as the new index
#QT WHY DO WE HAVE TO SET_INDEX ON ITEM?

df.set_index('Item', inplace=True)
print(df.head())


#1) How many different types of items did each student create for the bake sale? Which student provided the most Items?
# Get the unique values and their count for the Student column
#basically the value_counts() returns count of unique values in descending order

print(df["Student"].value_counts())

print(df["Student"].value_counts(normalize=True))

