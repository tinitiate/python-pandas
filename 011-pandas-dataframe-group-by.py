""" MARKDOWN
---
YamlDesc: CONTENT-ARTICLE
Title: Python Pandas Dataframe Group By
MetaDescription: Python Pandas Dataframe Group By, Min, Max, Count, Sum
MetaKeywords: Python Pandas Dataframe Group By, Min, Max, Count, Sum
Author: (c) Venkata Bhattaram / www.github.com/tinitiate
ContentName: pandas-dataframe-group-by
---
MARKDOWN """

""" MARKDOWN
# DataFrame Data Operations
* Read with Header row, Read without Header row
* Demonstration of Group By Operations on columns to run aggregate expression, 
  on the columns.
MARKDOWN """

# MARKDOWN ```
from pandas import DataFrame, read_csv
import pandas as pd

################################################################################
# SalesData
# This is the Line Item Details of each BillNumber
# Here we see the BillNumber repeat itself for all the line items of a bill
################################################################################
SalesData = pd.DataFrame({'BillNumber':  [1,1,1,1,2,2,3,3,4,5,6,6,7],
                          'ProductName': ['Fruits', 'Breads', 'Soda','Milk','Breads', 'Soda','Milk','Soda','Milk','Milk','Breads','Milk','Breads'],
                          'UnitPrice':   [3.00, 2.50, 1.50, 2.00, 2.50, 1.50, 2.00, 1.50, 2.00, 2.00, 2.50, 2.00, 2.50]})
print(SalesData)


################################################################################
# Distinct
# Group By is the process of applying a Arithmetic Function for distinct 
# elements of a given tabular data set, Here we get Distinct Bill Numbers
################################################################################
print("Distinct")
Distinctvalues = SalesData.BillNumber.unique() 
print(Distinctvalues)

################################################################################
# Group By
# Get the First Row of every BillNumber
################################################################################
print("Group By, Get First Row from each")
print(SalesData.groupby(['BillNumber']).first())


################################################################################
# COUNT
# Get count of a column, Group By other columns
################################################################################
print("Count")
# Get Count of line items Across all SalesData data, [Ignore Header using the ix]
print(SalesData['BillNumber'].ix[0:].count())

# Get Count of line items Across all SalesData data, by BillNumber
print(SalesData.groupby(['BillNumber']).count()['ProductName'])


################################################################################
# SUM
# Get Sum value of a column, Group By other columns
################################################################################
print("Sum")
# Get Max of UnitPrice Across all SalesData data, [Ignore Header using the ix]
print(SalesData['UnitPrice'].ix[0:].sum())

# Get Max of UnitPrice Across Every BillNumber SalesData data
print(SalesData.groupby(['BillNumber']).sum()['UnitPrice'])


################################################################################
# MAX
# Get Max value of a column, Group By other columns
################################################################################
print("Max")
# Get Max of UnitPrice Across all SalesData data, [Ignore Header using the ix]
print(SalesData['UnitPrice'].ix[0:].max())

# Get Max of UnitPrice Across Every BillNumber SalesData data
print(SalesData.groupby(['BillNumber']).max()['UnitPrice'])


################################################################################
# MIN
# Get Min value of a column, Group By other columns
################################################################################
print("Min")
# Get Min of UnitPrice Across all SalesData data, [Ignore Header using the ix]
print(SalesData['UnitPrice'].ix[0:].min())

# Get Min of UnitPrice Across Every BillNumber SalesData data
print(SalesData.groupby(['BillNumber']).min()['UnitPrice'])


################################################################################
# Multiple Operations with GroupBy
# Here We demonstrate multiple operations with GroupBy and specifying 
# custom column names
################################################################################
print("Multiple Operations with GroupBy")
sumDF = SalesData.groupby(['BillNumber']).count()['UnitPrice'].reset_index().rename(columns={'UnitPrice':'UnitPrice_count'})
countDF = SalesData.groupby(['BillNumber']).sum()['UnitPrice'].reset_index().rename(columns={'UnitPrice':'UnitPrice_sum'})

print(sumDF)
print(countDF)

# Add columns to existing dataframe
x = sumDF.merge(countDF, on='BillNumber', how='inner')
print(x)

# MARKDOWN ```
