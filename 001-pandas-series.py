""" MARKDOWN
---
YamlDesc: CONTENT-ARTICLE
Title: Python Pandas Series
MetaDescription: Python Pandas Series
MetaKeywords: Python Pandas Series
Author: Venkata Bhattaram / tinitiate.com
ContentName: pandas-series
---
MARKDOWN """


""" MARKDOWN
# Pandas Series
* A Series is a one-dimensional labeled array of any data type 
  (integer, string, float, objects..).
* It can be viewed as Column in a data table
MARKDOWN """


""" MARKDOWN
## Create Series from a List
* Here we demonstrate create a Series using a python List.
* The Series create TWO columns, 
  * The first column called index. starts from 0 to (N-1), where N 
    is the size of the list.
  * The second column with the values of the list.
MARKDOWN """
# MARKDOWN ```
import pandas as pd
import numpy as np
L_LIST = [1, 3, 5, 7]
L_SERIES = pd.Series(L_LIST)
print(L_SERIES)
# MARKDOWN ```


""" MARKDOWN
## Create Series from a Dictionary
* Here we demonstrate create a Series using a python dictionary.
* The Series create TWO columns, 
  * The first column called index, from the keys of the dict and
  * The second column with the values of the dict.
MARKDOWN """
# MARKDOWN ```
##import (library) as (give the library a nickname/alias)
import pandas as pd #this is how I usually import pandas
import numpy as np

L_DICT = {'Chicago': 1000, 'New York': 1300, 'Portland': 900,
          'San Francisco': 1100, 'Austin': 450, 'Boston': None}

# Convert a dictionary to series 
cities_series = pd.Series(L_DICT)

print(cities_series)
# MARKDOWN ```


""" MARKDOWN
## Python Series Create Custom Name and Custom Index
* Here we demonstrate create a Series using lists to create data and custom index
* The `Series` parameters
  * name
  * data
  * index
* The Series create TWO columns, 
  * The first column called index, from the keys of the dict and
  * The second column with the values of the dict.
MARKDOWN """
# MARKDOWN ```
custom_series = pd.Series(name="test_series", data=['a', 'b', 'c', 'd'], index=[11, 22, 33, 44])
print(custom_series)
# MARKDOWN ```


""" MARKDOWN
## Generate Series from a CSV file
* Here we read a CSV and generate a Series
MARKDOWN """
# MARKDOWN ```
# importing pandas module  
import pandas as pd

# making data frame
df = pd.read_csv("series_data.csv")

ser = pd.Series(df['name'])
# csv_data = ser.head(3)
print(ser)
# MARKDOWN ```
