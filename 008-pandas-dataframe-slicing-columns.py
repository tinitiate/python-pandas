""" MARKDOWN
---
YamlDesc: CONTENT-ARTICLE
Title: Python Pandas Dataframe Slicing Columns ix, loc, iloc
MetaDescription: Python, Pandas, Dataframe, Slicing Columns, ix, loc, iloc
MetaKeywords: Python Pandas Dataframe  Indexing Columns ix, loc, iloc
Author: (c) Venkata Bhattaram / www.github.com/tinitiate
ContentName: pandas-dataframe-slicing-columns
---
MARKDOWN """

""" MARKDOWN
# Slicing Columns ix, loc, iloc
* Slicing means taking a part of your data set for further inspection.
* Pandas offers at least three methods for slicing data: .loc[], iloc[], ix[]
* **DataFrame.ix** **Depricated**
* A primarily label-location based indexer, with integer position fallback.
* **DataFrame.iloc**
* Purely integer-location based indexing for selection by position. **iloc[]**
  is primarily integer position based (from 0 to length-1 of the axis)
* **DataFrame.loc**
* Access a group of rows and columns by label or a boolean array, **loc[]**
  is primarily label based, but may also be used with a boolean array.

MARKDOWN """

# MARKDOWN ```

import pandas as pd

# EMP DataFrame
df_emp = pd.DataFrame({'EmpID':   [1,2,3,4,5],
                       'EmpName': ['AAA','BBB','CCC','DDD','EEE'],
                       'DeptID':  [1,2,3,None,None],
                       'Salary':  [12000,30000,50000,13000,10000],
                       'MgrId':   [2,3,None,None,None]},
                       index = [0,1,2,3,4])

################################################################################
# - DataFrame.ix, Depricated label based slicing 
################################################################################
print(df_emp.ix[:,['EmpID']])
print(df_emp.ix[:,[2]])


################################################################################
# - DataFrame.iloc, Slice DataFrame by index positions
################################################################################
print(df_emp.iloc[:,[0]])
print(df_emp.iloc[:,[1,2]])


################################################################################
# - DataFrame.loc, Slice DataFrame by Column Name
################################################################################
print(df_emp.loc[:,['EmpID']])

print(df_emp.loc[:,['EmpName','DeptID']])

# MARKDOWN ```
