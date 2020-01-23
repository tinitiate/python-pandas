""" MARKDOWN
---
YamlDesc: CONTENT-ARTICLE
Title: Python Pandas Dataframe Operations
MetaDescription: Python Pandas Dataframe Operations
MetaKeywords: Python Pandas Dataframe Operations
Author: (c) Venkata Bhattaram / www.github.com/tinitiate
ContentName: pandas-dataframe-operations
---
MARKDOWN """

""" MARKDOWN
# Creat Psuedo Columns
* Create column by applying a function on an existing column
* Create column by applying operator on multiple existing columns
MARKDOWN """
# MARKDOWN ```
from pandas import DataFrame

# Create DataFrame
training = {'Course': ['Python','Java','SQL'],
            'Price': [3000.00,5000.00,6000.00] }

df1 = DataFrame(training, columns= ['Course', 'Price'])
print(df1)

# Creating a Psuedo Column using mathematical operator
# ##############################################################################
df1['Discount'] = df1['Price']*(10/100)
print(df1)


# Create a Psuedo Column using a function
# ##############################################################################
# Function to apply discount to the price
def ApplyDiscount(inPrice, inDiscount):
    return inPrice - inDiscount

# Apply the function
df1['FinalPrice'] = df1.apply(lambda row: ApplyDiscount(row['Price'], row['Discount']), axis=1)
print(df1)
# MARKDOWN ```


""" MARKDOWN
# Pandas Dataframe Operations
* DataFrame Column Change Index Values Operations
* Stack
* UnStack
* Transpose
MARKDOWN """

# MARKDOWN ```
import pandas as pd
from pandas import DataFrame


# Data for DataFrame
departments = { 'DeptID':[1,2,3,4]
               ,'DName': ['Sales','Engg','Marketing','Management']
               ,'StaffCount': [100,50,20,5] }


# Create the DataFrame
df1 = DataFrame(departments, columns= ['DeptID', 'DName', 'StaffCount'])
print(df1)


## STACK
## Creates Multilevel Indexes with repeating column names
## #############################################################################
l_stack = df1.stack()
print(l_stack)


## UNSTACK
## Creates Multilevel Indexes with repeating values
## #############################################################################
l_unstack = df1.unstack()
print(l_unstack)


## TRANSPOSE
## Flips the orientation of a given range or array.
## #############################################################################
l_transpose = df1.T
print(l_transpose)


## PIVOT
## Summarizes data, which could include sums, averages, etc. for each column
## #############################################################################
l_pivot = df1.pivot('DeptID', 'DName', 'StaffCount')
print(l_pivot)


## MELT / UNPIVOT
## Generates Rows for each column
## #############################################################################
l_melt = pd.melt(df1, id_vars = ['DeptID','DName'], value_vars = ['StaffCount'])
print(l_melt)
"""
# MARKDOWN ```
