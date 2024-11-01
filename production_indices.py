import pandas as pd

# Load the dataset
file_path = '/Users/prabha/Documents/capstone/Data-Analytics-Capstone/fao_data_production_indices_data.csv'  # Replace with your file path
production_df = pd.read_csv(file_path)

# Check for missing values in important fields
important_columns = ['country_or_area', 'year', 'value', 'category']  # Replace with actual column names as needed
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

# Optionally, save the cleaned dataset to a new CSV file
cleaned_file_path = '/Users/prabha/Documents/capstone/Data-Analytics-Capstone/cleaned_fao_data_production_indices_data.csv'  # Specify a path for the cleaned file
production_df_cleaned.to_csv(cleaned_file_path, index=False)