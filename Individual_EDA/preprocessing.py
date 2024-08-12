# import os
# import pandas as pd
# import matplotlib.pyplot as plt
# import glob

# # Ensure plots don't display during script execution
# plt.ioff()

# def process_patient_file(file_path, output_base_dir):
#     # Load the data
#     df = pd.read_csv(file_path)
    
#     # Drop the 'Other' column
#     df = df[['Date', 'Morning', 'Afternoon']]
    
#     # Calculate statistics
#     stats = {
#         'M_mean': df['Morning'].mean(),
#         'M_median': df['Morning'].median(),
#         'M_std': df['Morning'].std(),
#         'M_min': df['Morning'].min(),
#         'M_max': df['Morning'].max(),
#         'A_mean': df['Afternoon'].mean(),
#         'A_median': df['Afternoon'].median(),
#         'A_std': df['Afternoon'].std(),
#         'A_min': df['Afternoon'].min(),
#         'A_max': df['Afternoon'].max(),
#         '20th_quantile': df[['Morning', 'Afternoon']].quantile(0.20).mean(),
#         '25th_quantile': df[['Morning', 'Afternoon']].quantile(0.25).mean(),
#         '50th_quantile': df[['Morning', 'Afternoon']].quantile(0.50).mean(),
#         '75th_quantile': df[['Morning', 'Afternoon']].quantile(0.75).mean(),
#     }
    
#     # Extract patient ID from filename and create output folder
#     patient_id = os.path.basename(file_path).split('-')[0] + '-' + os.path.basename(file_path).split('-')[1]
#     output_folder = os.path.join(output_base_dir, patient_id)
#     os.makedirs(output_folder, exist_ok=True)
    
#     # Generate and save plots
#     plt.figure(figsize=(10, 6))
#     plt.plot(df['Date'], df['Morning'], label='Morning')
#     plt.plot(df['Date'], df['Afternoon'], label='Afternoon')
#     plt.xlabel('Date')
#     plt.ylabel('Values')
#     plt.title('Line Plot for Morning and Afternoon')
#     plt.legend()
#     plt.xticks(rotation=45)
#     plt.tight_layout()
#     plt.savefig(os.path.join(output_folder, 'line_plot.png'))
#     plt.close()

#     plt.figure(figsize=(10, 6))
#     plt.scatter(df['Date'], df['Morning'], label='Morning')
#     plt.scatter(df['Date'], df['Afternoon'], label='Afternoon')
#     plt.xlabel('Date')
#     plt.ylabel('Values')
#     plt.title('Scatter Plot for Morning and Afternoon')
#     plt.legend()
#     plt.xticks(rotation=45)
#     plt.tight_layout()
#     plt.savefig(os.path.join(output_folder, 'scatter_plot.png'))
#     plt.close()

#     plt.figure(figsize=(10, 6))
#     df[['Morning', 'Afternoon']].boxplot()
#     plt.title('Box Plot for Morning and Afternoon')
#     plt.savefig(os.path.join(output_folder, 'box_plot.png'))
#     plt.close()

#     # Append the statistics to the final CSV
#     stats['Filename'] = os.path.basename(file_path)
#     return stats


# def main():
#     # List to hold all statistics
#     all_stats = []

#     # Specify the directory where the CSV files are located
#     input_directory = "/Users/siddhi/research_new/schas-2024-asthama-2.0/2024-Data-Cleaned/processed_data"
#     output_base_dir = '/Users/siddhi/research_new/schas-2024-asthama-2.0/Individual_EDA/plots'
    
#     # Loop over all CSV files in the specified directory
#     for file_path in glob.glob(os.path.join(input_directory, '*.csv')):
#         stats = process_patient_file(file_path, output_base_dir)
#         all_stats.append(stats)
    
#     # Convert to DataFrame and save as a CSV file in the output directory
#     stats_df = pd.DataFrame(all_stats)
#     stats_df.to_csv(os.path.join(output_base_dir, 'patient_statistics.csv'), index=False)

# if __name__ == "__main__":
#     main()









import os
import pandas as pd
import matplotlib.pyplot as plt
import glob

# Ensure plots don't display during script execution
plt.ioff()

def process_patient_file(file_path, output_base_dir):
    # Load the data
    df = pd.read_csv(file_path)
    
    # Drop the 'Other' column
    df = df[['Date', 'Morning', 'Afternoon']]
    
    # Calculate statistics
    stats = {
        'M_mean': df['Morning'].mean(),
        'M_median': df['Morning'].median(),
        'M_std': df['Morning'].std(),
        'M_min': df['Morning'].min(),
        'M_max': df['Morning'].max(),
        'A_mean': df['Afternoon'].mean(),
        'A_median': df['Afternoon'].median(),
        'A_std': df['Afternoon'].std(),
        'A_min': df['Afternoon'].min(),
        'A_max': df['Afternoon'].max(),
        '20th_quantile': df[['Morning', 'Afternoon']].quantile(0.20).mean(),
        '25th_quantile': df[['Morning', 'Afternoon']].quantile(0.25).mean(),
        '50th_quantile': df[['Morning', 'Afternoon']].quantile(0.50).mean(),
        '75th_quantile': df[['Morning', 'Afternoon']].quantile(0.75).mean(),
    }
    
    # Extract patient ID from filename and create output folder
    patient_id = os.path.basename(file_path).split('-')[0] + '-' + os.path.basename(file_path).split('-')[1]
    output_folder = os.path.join(output_base_dir, patient_id)
    os.makedirs(output_folder, exist_ok=True)
    
    # Generate and save plots
    plt.figure(figsize=(10, 6))
    plt.plot(df['Date'], df['Morning'], label='Morning')
    plt.plot(df['Date'], df['Afternoon'], label='Afternoon')
    plt.xlabel('Date')
    plt.ylabel('Values')
    plt.ylim(100, 800)  # Set y-axis limits
    plt.title('Line Plot for Morning and Afternoon')
    plt.legend()
    plt.xticks(rotation=45)  # Rotate x-axis labels
    plt.gca().xaxis.set_major_locator(plt.MaxNLocator(10))  # Set the number of x-ticks to avoid overlap
    plt.tight_layout()
    plt.savefig(os.path.join(output_folder, 'line_plot.png'))
    plt.close()

    plt.figure(figsize=(10, 6))
    plt.scatter(df['Date'], df['Morning'], label='Morning', alpha=0.8)  # Set opacity
    plt.scatter(df['Date'], df['Afternoon'], label='Afternoon', alpha=0.8)  # Set opacity
    plt.xlabel('Date')
    plt.ylabel('Values')
    plt.ylim(100, 800)  # Set y-axis limits
    plt.title('Scatter Plot for Morning and Afternoon')
    plt.legend()
    plt.xticks(rotation=45)  # Rotate x-axis labels
    plt.gca().xaxis.set_major_locator(plt.MaxNLocator(10))  # Set the number of x-ticks to avoid overlap
    plt.tight_layout()
    plt.savefig(os.path.join(output_folder, 'scatter_plot.png'))
    plt.close()

    plt.figure(figsize=(10, 6))
    df[['Morning', 'Afternoon']].boxplot()
    plt.ylim(100, 800)  # Set y-axis limits
    plt.title('Box Plot for Morning and Afternoon')
    plt.tight_layout()
    plt.savefig(os.path.join(output_folder, 'box_plot.png'))
    plt.close()

    # Append the statistics to the final CSV
    stats['Filename'] = os.path.basename(file_path)
    return stats


def main():
    # List to hold all statistics
    all_stats = []

    # Specify the directory where the CSV files are located
    input_directory = "/Users/siddhi/research_new/schas-2024-asthama-2.0/2024-Data-Cleaned/processed_data"
    output_base_dir = '/Users/siddhi/research_new/schas-2024-asthama-2.0/Individual_EDA/plots'
    
    # Loop over all CSV files in the specified directory
    for file_path in glob.glob(os.path.join(input_directory, '*.csv')):
        stats = process_patient_file(file_path, output_base_dir)
        all_stats.append(stats)
    
    # Convert to DataFrame and save as a CSV file in the output directory
    stats_df = pd.DataFrame(all_stats)
    stats_df.to_csv(os.path.join(output_base_dir, 'patient_statistics.csv'), index=False)

if __name__ == "__main__":
    main()
