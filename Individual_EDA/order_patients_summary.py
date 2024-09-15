import pandas as pd

# Load the CSV file into a DataFrame
csv_file_path = '/Users/siddhi/research_new/schas-2024-asthama-2.0/Individual_EDA/patient_statistics.csv'
df = pd.read_csv(csv_file_path)

# Extract the numerical part of the filename for sorting
df['numeric_id'] = df['Filename'].str.extract(r'SB-(\d+)-Imputed.csv').astype(int)

# Sort the DataFrame by the extracted numeric part
df.sort_values(by='numeric_id', inplace=True)

# Drop the temporary 'numeric_id' column used for sorting
df.drop(columns=['numeric_id'], inplace=True)

# Save the sorted DataFrame back to a CSV file
output_file_path = '/Users/siddhi/research_new/schas-2024-asthama-2.0/Individual_EDA/ordered_patients_summary.csv'
df.to_csv(output_file_path, index=False)
