""" MARKDOWN
---
YamlDesc: CONTENT-ARTICLE
Title: Python Pandas Series Queries
MetaDescription: Python Pandas Series Queries
MetaKeywords: Python Pandas Series Queries
Author: Venkata Bhattaram / tinitiate.com
ContentName: pandas-series-queries
---
MARKDOWN """


""" MARKDOWN
# Pandas Series Queries
* A Series is a one-dimensional labeled array of any data type 
  (integer, string, float, objects..).
* It can be viewed as Column in a data table
MARKDOWN """

""" MARKDOWN
## Python Series Query
* Here we demonstrate Series Query
* Get all data values from series
* Change data value of a Key
* Check if a data value is part of the series
* Check if data value is Null or Not Null
MARKDOWN """

# MARKDOWN ```
import pandas as pd #this is how I usually import pandas
import numpy as np

L_DICT = {'Chicago': 1000, 'New York': 1300, 'Portland': 900,
          'San Francisco': 1100, 'Austin': 450, 'Boston': None}

# Convert a dictionary to series 
cities_series = pd.Series(L_DICT)

# Print series cities_series
print(cities_series)

# Get all the values of cities_series
print(cities_series[cities_series < 1000])

# Change Value of a Key
print('Old value:', cities_series['Chicago'])
cities_series['Chicago'] = 1400

print('New value:', cities_series['Chicago'])

# Check if 'Seattle' part of the series
print('Seattle' in cities_series)

# Check if 'Seattle' part of the series
print('San Francisco' in cities_series)

# Math on Dictionary values
print(cities_series / 3)
print(np.square(cities_series))

# Check Null or Not Null
print(cities_series.isnull())
print('\n')
print(cities_series[cities_series.isnull()])
# MARKDOWN ```
