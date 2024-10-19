# Importing dependencies
import pandas as pd
import numpy as np
import time
import openpyxl
import xlrd
import os
import random

def data_cleaning_master(data_path, data_name):
    print("\nThank you for providing the dataset details!")
    
    # Introduce a random delay to simulate processing time
    sec = random.randint(1, 4)
    print(f"Validating the file path... Please wait for {sec} seconds.")
    time.sleep(sec)
    
    # Check if the provided file path exists
    if not os.path.exists(data_path):
        print("\nError: The specified path does not exist. Please recheck and try again.")
        return
    else:
        # Check the file format and load the data accordingly
        if data_path.endswith('.csv'):
            print("\nDataset detected as CSV format.")
            data = pd.read_csv(data_path, encoding_errors='ignore')
        elif data_path.endswith('.xlsx'):
            print("\nDataset detected as Excel format.")
            data = pd.read_excel(data_path)
        else:
            print("\nError: Unsupported file format. Please provide a CSV or Excel file.")
            return

    # Introduce a delay before showing dataset dimensions
    sec = random.randint(1, 4)
    print(f"\nAnalyzing dataset structure... Please wait for {sec} seconds.")
    time.sleep(sec)
    
    # Display the total number of rows and columns
    print(f"Dataset contains {data.shape[0]} rows and {data.shape[1]} columns.")

    # Start the cleaning process
    sec = random.randint(1, 4)
    print(f"\nChecking for duplicate records... Please wait for {sec} seconds.")
    time.sleep(sec)
    
    # Identify and count duplicate records
    duplicates = data.duplicated()
    total_duplicate = duplicates.sum()

    print(f"\nThe dataset contains {total_duplicate} duplicate records.")

    # Save the duplicate records if any
    if total_duplicate > 0:
        sec = random.randint(1, 4)
        print(f"\nSaving {total_duplicate} duplicate records... Please wait for {sec} seconds.")
        time.sleep(sec)
        duplicate_records = data[duplicates]
        duplicate_records.to_csv(f'{data_name}_duplicates.csv', index=False)
        print(f"Duplicate records saved as '{data_name}_duplicates.csv'.")
    
    # Remove duplicate records
    df = data.drop_duplicates()

    # Introduce a delay before checking for missing values
    sec = random.randint(1, 4)
    print(f"\nChecking for missing values... Please wait for {sec} seconds.")
    time.sleep(sec)

    # Identify missing values
    total_missing_value = df.isnull().sum().sum()
    missing_value_by_columns = df.isnull().sum()

    print(f"\nTotal missing values in the dataset: {total_missing_value}")
    print(f"Missing values by column:\n{missing_value_by_columns}")

    # Handle missing values
    sec = random.randint(1, 6)
    print(f"\nHandling missing values... Please wait for {sec} seconds.")
    time.sleep(sec)

    # Fill missing values for numeric columns and drop rows for non-numeric columns
    for col in df.columns:
        if df[col].dtype in (float, int):
            df[col].fillna(df[col].mean(), inplace=True)
            print(f"Filled missing values in numeric column '{col}' with the column mean.")
        else:
            missing_count = df[col].isnull().sum()
            if missing_count > 0:
                df.dropna(subset=[col], inplace=True)
                print(f"Dropped {missing_count} rows due to missing values in non-numeric column '{col}'.")

    # Introduce a delay before saving the cleaned dataset
    sec = random.randint(1, 5)
    print(f"\nFinalizing and exporting the cleaned dataset... Please wait for {sec} seconds.")
    time.sleep(sec)

    # Save the cleaned dataset
    df.to_csv(f'{data_name}_Clean_data.csv', index=False)
    print(f"\nCongratulations! The dataset has been successfully cleaned.")
    print(f"Cleaned dataset dimensions: {df.shape[0]} rows and {df.shape[1]} columns.")
    print(f"The cleaned dataset is saved as '{data_name}_Clean_data.csv'.")

if __name__ == "__main__":
    print("Welcome to Data Cleaning Master!")
    # Ask for the dataset path and name
    data_path = input("\nPlease enter the dataset file path (with extension): ")
    data_name = input("Please enter a name for the dataset (for saving): ")
    
    # Call the data cleaning function
    data_cleaning_master(data_path, data_name)
