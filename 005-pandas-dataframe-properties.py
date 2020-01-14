""" MARKDOWN
---
YamlDesc: CONTENT-ARTICLE
Title: Python Pandas Dataframe Properties
MetaDescription: Python Pandas Dataframe, properties
MetaKeywords: Python, Pandas ,Dataframe, properties
Author: (c) Venkata Bhattaram / tinitiate.com
ContentName: pandas-dataframe-properties
---
MARKDOWN """


""" MARKDOWN
# Python Pandas Dataframe Properties
* Information about DataFrame using .info()
* dtypes
* describe()
  * Describe DataFrame, with data metrics
* iloc[]
  * Print a Single Row using .iloc[, using the row number (index starts from 0)
* Head and Tail (Head and Tail of the records)
MARKDOWN """

# MARKDOWN ```
# Import all libraries needed for the tutorial
import pandas as pd #this is how I usually import pandas

# Create DataFrame from Lists
#############################

# Create Lists of equal sizes of DataFrame
nation_id = [1, 2, 3, 4, 5]
nations   = ['India','China','USA','Russia','Brazil']
sales     = [968, 155, 77, 578, 973]
profits   = [140, 110, 170, 130, 120]

# Combine Multiple Lists (of the same index size) into a list or
# tuples using zip (This returns a iterator of tuples
nationSales = list(zip(nation_id, nations, sales, profits, ))

# Create a DataFrame nationSales from the above lists
# use  the "nation_id" as index
df_nationSales = pd.DataFrame(data = nationSales, columns=['nation_id', 'nations', 'sales', 'profits'])
df_nationSales.set_index('nation_id', inplace=True)


# Print the aDataframe
print(df_nationSales)
print("")

# Assign Indexes 
# info()
##############################
# Info About Data Frame
print(df_nationSales.info())

# dtypes
##############################
# Print Data types of DataFrame
print(df_nationSales.dtypes)

# describe()
##############################
# Describe DataFrame, with data metrics
print(df_nationSales.describe())

# iloc[]
##############################
# Print a Single Row using .iloc[], using the row number (index starts from 0)
print(df_nationSales.iloc[2])

# Print Head and Tail of the Data Frame
#######################################
print(df_nationSales.head(2))
print(df_nationSales.tail(2))

# MARKDOWN ```
