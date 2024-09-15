import os
import pandas as pd

def calculate_missing_data_chunks(column_data):
    # Identify missing data chunks
    chunks = []
    current_chunk_size = 0
    for value in column_data:
        if pd.isna(value):
            current_chunk_size += 1
        else:
            if current_chunk_size > 0:
                chunks.append(current_chunk_size)
            current_chunk_size = 0
    # Add the last chunk if the column ends with missing data
    if current_chunk_size > 0:
        chunks.append(current_chunk_size)
    return chunks

def process_patient_files(directory, output_file_path):
    summary_data = []

    # Iterate over all CSV files in the directory
    for file_name in os.listdir(directory):
        if file_name.endswith(".csv"):
            # Extract patient_id from the file name
            patient_id = file_name.split('-')[0] + '-' + file_name.split('-')[1]
            
            # Load the CSV file
            file_path = os.path.join(directory, file_name)
            df = pd.read_csv(file_path)
            
            # Drop the 'Other' column
            if 'Other' in df.columns:
                df.drop(columns=['Other'], inplace=True)
            
            # Calculate total_data, start_date, end_date
            total_data = len(df)
            start_date = df['Date'].min()
            end_date = df['Date'].max()

            # Calculate M_total_ad, M_total_md, M_highest_md_chunk, M_lowest_md_chunk
            M_total_ad = df['Morning'].notna().sum()
            M_total_md = df['Morning'].isna().sum()
            M_chunks = calculate_missing_data_chunks(df['Morning'])
            M_highest_md_chunk = max(M_chunks) if M_chunks else 0
            M_lowest_md_chunk = min(M_chunks) if M_chunks else 0

            # Calculate A_total_ad, A_total_md, A_highest_md_chunk, A_lowest_md_chunk
            A_total_ad = df['Afternoon'].notna().sum()
            A_total_md = df['Afternoon'].isna().sum()
            A_chunks = calculate_missing_data_chunks(df['Afternoon'])
            A_highest_md_chunk = max(A_chunks) if A_chunks else 0
            A_lowest_md_chunk = min(A_chunks) if A_chunks else 0

            # Append the calculated data to summary_data
            summary_data.append([
                patient_id, total_data, start_date, end_date,
                M_total_ad, M_total_md, M_highest_md_chunk, M_lowest_md_chunk,
                A_total_ad, A_total_md, A_highest_md_chunk, A_lowest_md_chunk
            ])

    # Create a DataFrame for the summary data
    summary_df = pd.DataFrame(summary_data, columns=[
        'patient_id', 'total_data', 'start_date', 'end_date',
        'M_total_ad', 'M_total_md', 'M_highest_md_chunk', 'M_lowest_md_chunk',
        'A_total_ad', 'A_total_md', 'A_highest_md_chunk', 'A_lowest_md_chunk'
    ])

    # Sort the DataFrame by patient_id
    summary_df.sort_values(by='patient_id', inplace=True)

    # Save the sorted summary DataFrame to the specified CSV file path
    summary_df.to_csv(output_file_path, index=False)

# Specify the directory containing the patient CSV files
directory = '/Users/siddhi/research_new/schas-2024-asthama-2.0/2024-Data-Cleaned/Original_Data'

# Specify the full path where you want to save the summary CSV file
output_file_path = '/Users/siddhi/research_new/schas-2024-asthama-2.0/Individual_EDA/missing_data_summary.csv'

# Process the files and save the sorted summary
process_patient_files(directory, output_file_path)
