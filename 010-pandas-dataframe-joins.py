""" MARKDOWN
---
YamlDesc: CONTENT-ARTICLE
Title: Python Pandas Dataframe Joins
MetaDescription: Python Pandas Dataframe Joins
MetaKeywords: Python Pandas Dataframe Joins, inner join, outer join, left join, right join
Author: (c) Venkata Bhattaram / www.github.com/tinitiate
ContentName: pandas-dataframe-joins
---
MARKDOWN """


""" MARKDOWN
# DataFrame Join Operations
* Appending DataFrames of the same column structure
* Inner join
* Outer join
* Right join
* Left join
* Join and filter
MARKDOWN """

# MARKDOWN ```
import pandas as pd

################################################################################
# Data Setup
################################################################################
# Depart DataFrame (Parent Data)
dept = pd.DataFrame({'DeptID':   [1,2,3,4],
                     'DeptName': ['Sales','Operations','Logistics','Admin']
                    },)

# Emp Set1 DataFrame (Child Data)
emp1 = pd.DataFrame({'EmpID':   [1,2,3,4,5],
                    'EmpName': ['AAA','BBB','CCC','DDD','EEE'],
                    'DeptID':  [1,2,3,None,None],
                    'Salary':  [12000,30000,50000,13000,10000],
                    'MgrId':   [2,3,None,None,None]},
                    index=[0,1,2,3,4])


# Emp Set2 DataFrame (Child Data)
emp2 = pd.DataFrame({'EmpID':   [7,8,9,10],
                    'EmpName': ['FFF','GGG','HHH','III'],
                    'DeptID':  [1,2,3,None],
                    'Salary':  [12000,13000,15000,10000],
                    'MgrId':   [2,3,None,None]},
                    index=[5,6,7,8])


################################################################################
# Append TWO DataFrames, using the concat method
################################################################################
emp = pd.concat([emp1,emp2])
print(emp)


################################################################################
# INNER JOIN
# Display DataFrame Data that matches with DeptID on both the DataFrames
################################################################################
print("Inner Join")
InnerJoin = pd.merge(dept, emp, on='DeptID', how='inner')
print(InnerJoin)


################################################################################
# RIGHT JOIN
# Display Dept DataFrame Non Matching Dept Data, on DeptID column
################################################################################
print("Right Join")
RightJoin = pd.merge(dept, emp, on='DeptID', how='right')
print(RightJoin)


################################################################################
# LEFT JOIN
# Display Emp DataFrame Non Matching Dept Data, on DeptID column
################################################################################
print("Left Join")
LeftJoin = pd.merge(dept, emp, on='DeptID', how='left')
print(LeftJoin)


################################################################################
# OUTER JOIN
# Display Matching and Non Matching data between Emp, Dept DataFrame on DeptID column
################################################################################
print("Outer Join")
OuterJoin = pd.merge(dept, emp, on='DeptID', how='outer')
print(OuterJoin)


################################################################################
# JOIN and Filter
################################################################################
print("Join Filter")
JoinFilter = pd.merge(dept, emp, on='DeptID', how='inner')
JoinFilter = JoinFilter[ JoinFilter.EmpName == 'FFF' ]
print(JoinFilter)

# MARKDOWN ```
