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
#
*
MARKDOWN """


# MARKDOWN ```
# Notes
# 1. DataFrame
# 2. DataFrame Column Change Index Values Operations
# 3. Stack
# 4. UnStack
# 5. Transpose

# Import all libraries needed for the tutorial

# General syntax to import specific functions in a library: 
##from (library) import (specific library function)
from pandas import DataFrame, read_csv
import pandas as pd


# Read Data from CSV file
file_cols = ['nations','capital','sales']
df        = pd.read_csv("SalesData.csv", names=file_cols)


# columns={'nations': 'NATIONS','capital': 'CAPITAL','sales': 'SALES'}

# Change Index Names
i=['a','b','c','d','e','f','g','h','i','j','k','l']

# Index is no more from Digit 0 
df.index=i
print(df)


file_cols = ['nations','capital','sales']
df        = pd.read_csv("SalesData.csv", names=['nations','capital'])

l_stack = df.stack()
print(l_stack)
print("\n")


l_unstack = df.unstack()
print(l_unstack)
print("\n")


l_transpose = df.T
print(l_transpose)

# MARKDOWN ```

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
#
*
MARKDOWN """


# 1. DataFrame
# 2. axis

# MARKDOWN ```
# Import all libraries needed for the tutorial

# General syntax to import specific functions in a library: 
##from (library) import (specific library function)
from pandas import DataFrame, read_csv
import pandas as pd


# Read Data from CSV file
file_cols = ['Nations','Capital','Month','Sales']
df        = pd.read_csv("MonthlySalesData.csv", names=file_cols)



# Create a New Dataframe with only 3 of the 4 columns
# Ignore the Header (As it contains the Column names)
df1 = df[['Nations','Month','Sales']].ix[1:]


# Conversion of DataTypes to make sure the 
# Mathematical Operations will work
df1.Nations = df1.Nations.astype(str)
df1.Month   = df1.Month.astype(str)
df1.Sales   = df1.Sales.astype(int)



# Creating a Psuedo Column 
df1['psuedo_column1'] = df1['Sales']*10
print(df1)


# Applying Axis Function
# AXIS-0 Column Wise
print("AXIS-0 Column Wise")
df2 = df1[['Sales','psuedo_column1']].sum(axis=1)
print(df2)


# AXIS-1 Row Wise
print("AXIS-1 Row Wise")
df2 = df1[['Sales','psuedo_column1']].sum(axis=0)
print(df2)




# This is a Function to calcluate comission
def getComission(i_sales):
    return i_sales*(5/100)

# Apply a Custom Function to a Data Frame
print("Appplying Calculating Functions")
df1['psuedo_column2'] = df1.apply(lambda row: getComission(row['Sales']), axis=1)
print(df1)
# MARKDOWN ```
