# This is a Data Cleaning application 

"""
Please create a python application that can take datasets and clean the data
Here’s the rephrased version of the points in a more professional tone:

- The application will prompt the user to provide the dataset's file path and name.
- It will identify and remove any duplicate records from the dataset.
- A separate file will be created to store a copy of all identified duplicates.
- The program will assess the dataset for any missing values.
- For numeric columns, missing values will be replaced with the column's mean; for non-numeric columns, 
  rows with missing data will be removed.
- Finally, the cleaned dataset will be saved as a new file, 
  and both the duplicates and cleaned data 
  will be returned for further use.
"""

# Step - 1 : Importing libraries
import pandas as pd
import numpy as np
import time
import openpyxl
import xlrd
import os
import random

# Step - 2 : Checking if path exists

data_path = 'sales.xlsx'
data_name = 'jan_sales'


if not os.path.exists(data_path):
    print("Please enter correct path!")
    #return
else:
    #checking the file type
    if data_path.endswith('.csv'):
        print('Dataset is csv!')
        data = pd.read_csv(data_path, encoding_errors = 'ignore')
    elif data_path.endswith('.xlsx'):
        print('Dataset is xlsx!')
        data = pd.read_excel(data_path)

    else:
        print('unknown file type')
        # return

# Showing number of records

print(f'Dataset contains {data.shape[0]} rows and {data.shape[1]} columns.')

# Start Cleaning

# Checking Duplicates 
duplicates = data.duplicated()
total_duplicates = data.duplicated().sum()

print(f'Dataset has total duplicate records : {total_duplicates}')

# saving the duplicates 

if total_duplicates>0:
    duplicate_records = data[duplicates]
    duplicate_records.to_csv(f'{data_name}_duplicates.csv', index = None)

# Deleting Duplicates

df = data.drop_duplicates()


# Missing Values

total_missing_value = df.isnull().sum().sum()
missing_value_by_columns = df.null().sum()

print(f'Dataset has total missing value: {total_missing_value}')
print(f'Dataset contains missing value by columns \n {missing_value_by_columns}')


# Dealing with missing values
#fillna - int and float
#dropna - any object

columns = df.columns

for col in columns:
    # filling mean for numeric columns for all rows
    if df[col].dtype in (float,int):
        df[col] = df[col].fillna(df[col].mean())
    else:
        # Dropping all rows with missing records for non number col
        df.dropna(subset = col, inplace = True)

# Data is cleaned
print("Congrats! Dataset is cleaned! \nNumber of Rows: {df.shape[0]} Number of columns: {df.shape[1]}")

df.to_csv(f'{data_name}_Clean_Data.csv', index = None)
print("Dataset is saved!")
