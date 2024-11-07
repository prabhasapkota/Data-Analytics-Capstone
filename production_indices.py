import pandas as pd

# Load the dataset
file_path = '/Users/prabha/Documents/capstone/Data-Analytics-Capstone/fao_data_production_indices_data.csv'  
production_df = pd.read_csv(file_path)

# Ensure 'year' column is in integer format
production_df['year'] = pd.to_numeric(production_df['year'], errors='coerce').astype('Int64')

# Check for missing values in important fields
important_columns = ['country_or_area', 'year', 'value', 'category']  
missing_values = production_df[important_columns].isnull().sum()

# Display the count of missing values per important column
print("Missing values in important fields:")
print(missing_values)

# Drop rows where 'year' or 'value' are missing
production_df_cleaned = production_df.dropna(subset=['year', 'value'])

# Verify the changes by checking for missing values again
missing_values_cleaned = production_df_cleaned[important_columns].isnull().sum()
print("\nMissing values after cleaning:")
print(missing_values_cleaned)

# Get the number of rows and columns
num_rows, num_columns = production_df.shape
print(f"The dataset has {num_rows} rows and {num_columns} columns.")

# Check for duplicates based on specific columns
duplicates = production_df_cleaned.duplicated(subset=['country_or_area', 'year', 'category', 'value'])
print(f"\nNumber of duplicate rows: {duplicates.sum()}")

# Drop duplicates from the cleaned dataset
production_df_cleaned = production_df_cleaned.drop_duplicates(subset=['country_or_area', 'year', 'category', 'value'])

# save the cleaned dataset to a new CSV file
cleaned_file_path = '/Users/prabha/Documents/capstone/Data-Analytics-Capstone/cleaned_fao_data_production_indices_data.csv' 
production_df_cleaned.to_csv(cleaned_file_path, index=False)

# Check if there are any duplicates in the cleaned dataset based on specific columns
remaining_duplicates = production_df_cleaned.duplicated(subset=['country_or_area', 'year', 'category', 'value']).sum()

# Display the result
if remaining_duplicates > 0:
    print(f"There are still {remaining_duplicates} duplicate rows remaining in the cleaned dataset.")
else:
    print("No duplicate rows remain in the cleaned dataset.")