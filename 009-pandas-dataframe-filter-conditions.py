""" MARKDOWN
---
YamlDesc: CONTENT-ARTICLE
Title: Python Pandas Dataframe Filter Conditions
MetaDescription: Python Pandas Dataframe Filter Conditions, Equal, Not Equal, Less Than, Greater Than, In, Not In, Is Null, Not Is Null
MetaKeywords: Python Pandas Dataframe Filter Conditions, Equal, Not Equal, Less Than, Greater Than, In, Not In, Is Null, Not Is Null
Author: (c) Venkata Bhattaram / www.github.com/tinitiate
ContentName: pandas-dataframe-filter-conditions
---
MARKDOWN """

""" MARKDOWN
# DataFrame filter Conditions
* Arithmetic Operations on various Data Types
* Union and Union All
* Inclusion / Exclusion Operators on various Data Types
* String Case Check filters (Upper / Lower)
* Filter Conditions with Nulls, NA, NaN
* Single Filter Condition
* Multiple Filter Conditions
* Multiple Filter Conditions using Query 
MARKDOWN """

# MARKDOWN ```
################################################################################
# Data Setup
################################################################################
import pandas as pd

# Emp DataFrame
emp1 = pd.DataFrame({  'EmpID':   [1,2,3,4,5,6,7,8,9,10]
                      ,'EmpName': ['AAA','BBB','CCC','ddd','eee','EEE','FFF','GGG','HHH','iii']
                      ,'DeptID':  [1,2,3,2,None,1,1,2,3,None]
                      ,'Salary':  [13000,30000,50000,50000,30000,13000,13000,50000,13000,10000]
                      ,'MgrId':   [2,3,None,None,None,2,3,None,None,None] }
                      ,index = [0,1,2,3,4,5,6,7,8,9])

# IN Clause
###################################
in_data = emp1['DeptID'].isin([2,3])
print(emp1[in_data])

# NOT IN Clause
###################################
not_in_data = ~emp1['DeptID'].isin([2,3])
print(emp1[not_in_data])

# GREATER THAN Clause
###################################
gt_data = emp1[emp1.Salary > 20000]
print(gt_data)

# LESS THAN Clause
###################################
lt_data = emp1[emp1.Salary < 20000]
print(lt_data)

# EQUAL TO Clause
####################################
eq_data = emp1[emp1.Salary == 13000]
print(eq_data)

# NOT EQUAL TO Clause
####################################
neq_data = emp1[emp1.Salary != 13000]
print(neq_data)

# IS NULL Clause
####################################
null_data = emp1[emp1['DeptID'].isnull()]
print(null_data)

# IS NOT NULL Clause
####################################
notnull_data = emp1[emp1['DeptID'].notnull()]
print(notnull_data)

# APPLYING MULTIPLE FILTER CONDITIONS USING AND
###############################################
multiple_filter_data_and = emp1[(emp1['DeptID'].notnull()) & (emp1['Salary'] != 13000) ]
print(multiple_filter_data_and)

# APPLYING MULTIPLE FILTER CONDITIONS USING OR
###############################################
multiple_filter_data_or = emp1[(emp1['DeptID'].notnull()) | (emp1['Salary'] != 13000) ]
print(multiple_filter_data_or)

# APPLYING MULTIPLE FILTER CONDITIONS USING QUERY Function
##########################################################
multiple_filter_data_query = emp1.query('Salary != 13000 & DeptID == 2')
print(multiple_filter_data_query)

# MARKDOWN ```
