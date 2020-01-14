""" MARKDOWN
---
YamlDesc: CONTENT-ARTICLE
Title: Python Pandas Dataframe Indexing
MetaDescription: Python, Pandas, Indexing
MetaKeywords: Python Pandas Dataframe Indexing
Author: (c) Venkata Bhattaram / www.github.com/tinitiate
ContentName: pandas-dataframe-indexing
---
MARKDOWN """

""" MARKDOWN
# DataFrame Indexing
* Here we demonstrate the following
* Create DataFrame index by specifing index = [Index Column Values]
* Create DataFrame index by specifing ColumnName in the set_index
* Create DataFrame index by counting the rows in data frame
* Remove DataFrame index

MARKDOWN """

# MARKDOWN ```

import pandas as pd

################################################################################
# Create DataFrame with Custom Index
# * Here we create index with values [111, 222, 333, 444, 555], make sure the 
#   number of values in the index list are same as the number of values 
#   in the dataframe.
################################################################################
df_emp = pd.DataFrame({'EmpID':   [1,2,3,4,5],
                       'EmpName': ['AAA','BBB','CCC','DDD','EEE'],
                       'DeptID':  [1,2,3,None,None],
                       'Salary':  [12000,30000,50000,13000,10000],
                       'MgrId':   [2,3,None,None,None]},
                       index = [111, 222, 333, 444, 555])

print(df_emp)

################################################################################
# Create DataFrame Index using set_index
# * Use an existing column as index, using the set_index
################################################################################
df_emp = pd.DataFrame({'EmpName': ['AAA','BBB','CCC','DDD','EEE'],
                       'DeptID':  [1,2,3,None,None],
                       'Salary':  [12000,30000,50000,13000,10000],
                       'MgrId':   [2,3,None,None,None]})

# ADD Index
# df_emp['EmpID'] = range(1, len(df_emp) + 1)

# set_index is the function that sets an existing column as index
# inplace: It makes the changes in the DataFrame if True.
# verify_integrity: It checks the new index column for duplicates if True.
# df_emp.set_index('EmpID', inplace=True, verify_integrity=True)

df_emp.set_index('EmpName', inplace=True, verify_integrity=True)
print(df_emp)



################################################################################
# Create DataFrame Add Index
# * Use a column as index, using the set_index
################################################################################
df_emp = pd.DataFrame({'EmpName': ['AAA','BBB','CCC','DDD','EEE'],
                       'DeptID':  [1,2,3,None,None],
                       'Salary':  [12000,30000,50000,13000,10000],
                       'MgrId':   [2,3,None,None,None]})

# Create a Index of numbers by counting the rows in the dataframe
# New Column values starting from 1 to the number of rows
df_emp['EmpID'] = range(1, len(df_emp) + 1)

# set_index is the function that sets an existing column as index
df_emp.set_index('EmpID', inplace=True, verify_integrity=True)
print(df_emp)


################################################################################
# Remove Index in a DataFrame, using the reset_index
################################################################################
df_emp = pd.DataFrame({'EmpID':   [1,2,3,4,5],
                       'EmpName': ['AAA','BBB','CCC','DDD','EEE'],
                       'DeptID':  [1,2,3,None,None],
                       'Salary':  [12000,30000,50000,13000,10000],
                       'MgrId':   [2,3,None,None,None]})

df_emp.set_index('EmpID', inplace=True, verify_integrity=True)
print(df_emp)

# Reset the index using reset_index
df_emp.reset_index(inplace=True)
print(df_emp)

# MARKDOWN ```
