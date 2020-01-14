""" MARKDOWN
---
YamlDesc: CONTENT-ARTICLE
Title: Python Pandas Dataframe Basics
MetaDescription: Python Pandas Dataframe, basics
MetaKeywords: Python, Pandas ,Dataframe, basics
Author: (c) Venkata Bhattaram / tinitiate.com
ContentName: pandas-dataframe-basics
---
MARKDOWN """

""" MARKDOWN
# Python Pandas Dataframe
* Data frame is a representation of data in tabular two-dimensional data 
  structure.
* Tabular data structure consists of the rows and columns, which form the axes 
  of the data structure.
* Dataframe provides mechanisms to query data across operations rows and 
  columns and across multiple dataframes using the `JOIN` operations.
MARKDOWN """

""" MARKDOWN
## Creating Data Frame
* Here we demonstrate creating a Dataframe from a List, Dictionary and 
  Dictionary of Lists.

MARKDOWN """
# MARKDOWN ```
import pandas as pd

# 1. CREATE DATAFRAME FROM LIST
#################################
# Source Data List
nations  = ['India','China','USA','Russia','Brazil']

# Create DataFrame from List and assign column name
df_nations = pd.DataFrame(nations, columns=['nations'])

# Print the Data Frame contents
print(df_nations)
print("")


# 2. CREATE DATAFRAME INDEX AND DATA FROM LISTS
##############################################
# Source Data List
nation_id = [1, 2, 3, 4, 5]
nations  = ['India','China','USA','Russia','Brazil']
df_nations = pd.DataFrame(nations, index=nation_id, columns=[ 'nations'])

# Set the Index Name to "id"
df_nations.index.name='id'
print(df_nations)
print("")


# 3. CREATE DATAFRAME INDEX AND DATA FROM MULTIPLE LISTS
########################################################

# Create Lists of equal sizes of DataFrame
nation_id = [1, 2, 3, 4, 5]
nations  = ['India','China','USA','Russia','Brazil']
sales    = [968, 155, 77, 578, 973]

# Combine Multiple Lists (of the same index size) into a list of 
# tuples using zip (This returns a iterator of tuples
nationSales = list(zip(nation_id, nations, sales,))

# Create a DataFrame nationSales from the above lists
# use  the "nation_id" as index
df_nationSales = pd.DataFrame(data = nationSales, columns=['nation_id', 'nations', 'sales'])
df_nationSales.set_index('nation_id', inplace=True)

# Print the aDataframe
print(df_nationSales)
print("")


# 4. CREATE DATAFRAME FROM DICTIONARY
#####################################

# Create a Dictionary
data_dict = { 'Chicago': 1000, 'New York': 1300, 'Portland': 900
             ,'San Francisco': 1100, 'Austin': 450, 'Boston': None}

# Create DataFrame with Key and Value as Columns of the DataFrame
df_from_dict = pd.DataFrame()
df_from_dict['CityName'] = data_dict.keys()
df_from_dict['Population'] = data_dict.values()

# Set Index
df_from_dict.set_index('CityName', inplace=True)

print(df_from_dict)


# 5. CREATE DATAFRAME FROM DICTIONARY OF LISTS
##############################################

# Create a Dictionary
EmpData = {'EmpID' : [1, 2, 3],
           'EmpName' : ['AAA', 'BBB', 'CCC'],
           'Sal' : [1000, 2000, 4000]
          }

# Create DataFrame with Key and Value as Columns of the DataFrame
df_from_dict = pd.DataFrame(EmpData, columns=['EmpID','EmpName','Sal'])

# Set Index
df_from_dict.set_index('EmpID', inplace=True)

print(df_from_dict)

# MARKDOWN ```
