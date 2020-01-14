""" MARKDOWN
---
YamlDesc: CONTENT-ARTICLE
Title: Python Pandas Dataframe Data Modification, Insert, Update, Delete
MetaDescription: Python Pandas Dataframe Data Modification, Insert, Update, Delete
MetaKeywords: Python, Pandas, Dataframe Data Modification, Insert, Update, Delete
Author: (c) Venkata Bhattaram / www.github.com/tinitiate
ContentName: pandas-dataframe-data-modification
---
MARKDOWN """


""" MARKDOWN
# Modifying data in a DataFrame
* Here we demonstrate reading data from a CSV into a DataFrame
  And modifying the data in the DataFrame and printing the data to screen
* Data Modification by Insert Update and Delete data operations
MARKDOWN """

# MARKDOWN ```
import pandas as pd

################################################################################
# Read Data from CSV file
################################################################################
# Emp Set1 DataFrame (Child Data)
df_emp = pd.DataFrame( {'EmpID':   [1,2,3,4,5],
                        'EmpName': ['AAA','BBB','CCC','DDD','EEE'],
                        'Salary':  [12000,30000,50000,13000,10000]})

df_emp.index = df_emp['EmpID']
print(df_emp)


################################################################################
# Insert or Add Data from DataFrame
################################################################################
idx = len(df_emp)
df_emp.loc[idx] = [6,'FFF','9000']

print(df_emp)


################################################################################
# Update or Modify Data from DataFrame
################################################################################
df_emp.loc[ df_emp.EmpID == 1, 'Salary'] = 5000
df_emp.loc[ df_emp.EmpID == 2, 'Salary'] = 6000

print(df_emp)


################################################################################
# Delete or Remove data from DataFrame
# Use NOT Equal To
################################################################################
df_emp = df_emp[ df_emp.EmpID != 1 ]

print(df_emp)


# MARKDOWN ```
