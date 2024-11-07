import pandas as pd

# Load the dataset
file_path = '/Users/prabha/Documents/capstone/Data-Analytics-Capstone/fao_data_land_data.csv'  # Replace with your file path
land_df = pd.read_csv(file_path)

# Ensure 'year' column is in integer format
land_df['year'] = pd.to_numeric(land_df['year'], errors='coerce').astype('Int64')

# Check for missing values in important fields
important_columns = ['country_or_area', 'year', 'value', 'category']  # Replace with actual column names as needed
missing_values = land_df[important_columns].isnull().sum()

# Display the count of missing values per important column
print("Missing values in important fields:")
print(missing_values)

# Drop rows where 'year' or 'value' are missing
land_df_cleaned = land_df.dropna(subset=['year', 'value'])

# Verify the changes by checking for missing values again
missing_values_cleaned = land_df_cleaned[important_columns].isnull().sum()
print("\nMissing values after cleaning:")
print(missing_values_cleaned)

# Check if 'year' column is in integer format
print("\nData type of 'year' column:", land_df_cleaned['year'].dtype)

# Save the cleaned dataset to a new CSV file
cleaned_file_path = '/Users/prabha/Documents/capstone/Data-Analytics-Capstone/cleaned_fao_data_land_data.csv'  # Specify a path for the cleaned file
land_df_cleaned.to_csv(cleaned_file_path, index=False)

# Get the number of rows and columns
num_rows, num_columns = land_df_cleaned.shape
print(f"The dataset has {num_rows} rows and {num_columns} columns.")

# Check for duplicates based on specific columns
duplicates = land_df.duplicated(subset=['country_or_area', 'year', 'category', 'value'])
print(f"\nNumber of duplicate rows: {duplicates.sum()}")
