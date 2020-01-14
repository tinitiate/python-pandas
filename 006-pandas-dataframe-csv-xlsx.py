""" MARKDOWN
---
YamlDesc: CONTENT-ARTICLE
Title: Python Pandas Read CSV and XLSX to Dataframe
MetaDescription: Python Pandas Read CSV and XLSX to Dataframe
MetaKeywords: Python Pandas Read CSV and XLSX to Dataframe
Author: (c) Venkata Bhattaram / www.github.com/tinitiate
ContentName: pandas-csv-xlsx-dataframe
---
MARKDOWN """

""" MARKDOWN
# Read CSV and XLSX data into DataFrame
* Read and Assign Various Data Types (Number, Date, String) to the CSV rows data
* Read with Header row, Read without Header row
* Write DataFrame to CSV file
MARKDOWN """
# MARKDOWN ```
from pandas import DataFrame, read_csv
import pandas as pd

################################################################################
# - Read CSV file with Header
################################################################################
df1 = pd.read_csv("emp.csv")

# Print to Screen
print(df1.columns)
print(df1.values)


################################################################################
# - Read CSV file without Header
# - Provide custom CSV Header, using the "names" parameter
# - Set the Index Column by Name
################################################################################
df1 = pd.read_csv( "emp.csv"
                  ,names=["EMP_ID", "EMP_NAME", "JOIN_DATE", "SALARY", "DEPT_ID"]
                  ,index_col=["EMP_ID"]
                  ,skiprows=1)

# Print to Screen
print(df1.columns)
print(df1.values)


################################################################################
# - Read CSV and Assign DataTypes
################################################################################

# STEP 1. Read CSV to DataFrame, by skipping the header and assigning 
#         custom Header using "names"
df_stage = pd.read_csv( "emp.csv"
                       ,names=["EMP_ID", "EMP_NAME", "JOIN_DATE", "SALARY", "DEPT_ID"]
                       ,skiprows=1)

# STEP 2. Assign DataTypes using astype, Handle NULLs, Handle Date DataType 
#         by Column
df_stage["EMP_ID"] = df_stage["EMP_ID"].astype(int)
df_stage.set_index("EMP_ID", inplace = True)
df_stage["EMP_NAME"] = df_stage["EMP_NAME"].astype(str)
# Convert String to Date
df_stage["JOIN_DATE"] = pd.to_datetime(df_stage["JOIN_DATE"])
df_stage["SALARY"] = df_stage["SALARY"].astype(float)
# Convert NULLs to -1 and handle as 
df_stage["DEPT_ID"] = df_stage["DEPT_ID"].fillna(-1).astype(int)

print(df_stage)

# MARKDOWN ```


""" MARKDOWN
# Read CSV with Various DataTypes into DataFrame
* Read and Assign Various Data Types (Number, Date, DateTime, String) to
  the CSV rows data
* Create a new column in the DataFrame from data with in the CSV file
MARKDOWN """
# MARKDOWN ```
from pandas import DataFrame, read_csv
import pandas as pd

################################################################################
# Read CSV file with Header
################################################################################
file_cols = ['ID','Name','JoinDate','Event','EventDate','EventTime']
df        = pd.read_csv("DataTypeTest.csv", names=file_cols)


################################################################################
# Create a New Dataframe with columns and
# Ignore the Header (As it contains the Column names), Read Columns by Data Type
################################################################################
df1 = df[['ID','Name','JoinDate','Event','EventDate','EventTime']].ix[1:]

# Create EventDateTime by concatenating EventDate + EventTime
df1['EventDateTime'] = df1['EventDate']+" "+df1['EventTime']
df1.EventDateTime    = pd.to_datetime(df1['EventDateTime'], format='%m-%d-%Y %H:%M:%S')

# Read Strings, INT, Date types into a new DataFrame
df1.ID        = df1.ID.astype(int)
df1.Name      = df1.Name.astype(str)
df1.JoinDate  = pd.to_datetime(df1['JoinDate'], format='%m-%d-%Y')
df1.Event     = df1.Event.astype(str)
df1.EventDate = pd.to_datetime(df1['EventDate'], format='%m-%d-%Y')
print(df1)

# MARKDOWN ```


""" MARKDOWN
# Read CSV with Various DataTypes and assign column names to DataFrame
* Read and Assign Various Data Types (Number, Date, DateTime, String) to
  the CSV rows data
* Assign column names to the DataFrame
MARKDOWN """
# MARKDOWN ```
from pandas import DataFrame, read_csv
import pandas as pd

################################################################################
# Read Data from CSV file
################################################################################
file_cols = ['nations','capital','sales']
df        = pd.read_csv("SalesData.csv", names=file_cols)


# Add a Column called SKUs after 'sales' column
# Default Value is NewVal
df.insert(loc=3, column='SKUs', value='NewVal')
print(df)

################################################################################
# Assign Columns by renaming Columns in the dataframe
################################################################################
df.rename(columns={'nations': 'NATIONS'}, inplace=True)
df.rename(columns={'capital': 'CAPITAL'}, inplace=True)
df.rename(columns={'sales': 'SALES'}, inplace=True)
print(df)

# Drop Columns
df.drop(labels=['SKUs'], axis=1, inplace=True)
print(df)
# MARKDOWN ```


""" MARKDOWN
# Write DataFrame to CSV file
* Read and Assign Various Data Types (Number, Date, DateTime, String) to
  the CSV rows data
* Assign column names to the DataFrame
MARKDOWN """
# MARKDOWN ```
from pandas import DataFrame

# Create a DataFrame
training = {'Course': ['Python','Java','SQL'],
        'Price': [3000,5000,6000]
        }

df = DataFrame(training, columns= ['Course', 'Price'])

export_to_csv = df.to_csv(r'C:\tinitiate\training_dataframe.csv', index = None, header=True)

print (df)

# MARKDOWN ```
