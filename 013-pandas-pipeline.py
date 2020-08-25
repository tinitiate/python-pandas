""" MARKDOWN
---
Title: Python Pandas Pipes
MetaKeywords: Python Pandas Pipes
Author: (c) Venkata Bhattaram
ContentName: pandas-pipes
---
MARKDOWN """

""" MARKDOWN
# Pandas pipelines
* Python pipeline feature where Python functions are combined together as a
  sequence of steps or connected as pipes, that enable data progression of processing
MARKDOWN """
# MARKDOWN ```
import pandas as pd

# Create empty dataframe
df = pd.DataFrame()

# Create a column
df['name'] = ['John', 'Steve', 'Sarah']
df['gender'] = ['Male', 'Male', 'Female']
df['age'] = [31, 32, 19]

# Create a function that
def mean_age_by_group(dataframe, col):
    # groups the data by a column and returns the mean age per group
    return dataframe.groupby(col).mean()

# Create a function that
def uppercase_column_name(dataframe):
    # Capitalizes all the column headers
    dataframe.columns = dataframe.columns.str.upper()
    # And returns them
    return dataframe

df = df.pipe(mean_age_by_group, col='gender').pipe(uppercase_column_name)

print(df)


#####################################################################################
# Transformations
#####################################################################################
# 1. Transformations are modifications to input data
# 2. Transformations ususally are stateless, Any"transformation" of input data
#    should ONLY be dependent on other inputs provided,
#    So this is to say provide all changes required as well

# Create empty dataframe
df = pd.DataFrame()

# Create a column
df['name'] = ['John', 'Steve', 'Sarah']
df['gender'] = ['Male', 'Male', 'Female']
df['age'] = [31, 32, 19]

def get_avg(dataframe, measure_col, groupby_col):
    return dataframe.groupby([groupby_col]).min()[measure_col]

#def get_percent(dataframe, col):
#    return dataframe.groupby([groupby_col]).min()[measure_col]

df = df.pipe(get_avg,measure_col='age', groupby_col='gender')

print(df)
# MARKDOWN ```
