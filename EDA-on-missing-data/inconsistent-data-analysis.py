import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Folder containing patient CSV files
folder_path = 'Original_data'

# Load all patient data
all_data = []
for file in os.listdir(folder_path):
    if file.endswith('.csv'):
        patient_id = file.split('.')[0]  # Assuming patient ID is the filename without extension
        df = pd.read_csv(os.path.join(folder_path, file))
        df['patient_id'] = patient_id
        all_data.append(df)

# Combine all data into a single DataFrame
df_all = pd.concat(all_data)

# Convert date column to datetime
df_all['date'] = pd.to_datetime(df_all['date'])

# Determine the earliest and latest dates
start_date = df_all['date'].min()
end_date = df_all['date'].max()

print(f"Earliest Start Date: {start_date}")
print(f"Latest End Date: {end_date}")

# Define yearly blocks
blocks = pd.date_range(start=start_date, end=end_date, freq='YS').to_pydatetime().tolist()
blocks.append(end_date)  # Ensure the last block covers till the end date

# Create a summary DataFrame to store the presence of data in each block
patient_ids = df_all['patient_id'].unique()
summary = pd.DataFrame(index=patient_ids, columns=range(1, len(blocks)))

for i in range(1, len(blocks)):
    block_start = blocks[i-1]
    block_end = blocks[i]
    
    for patient_id in patient_ids:
        patient_data = df_all[(df_all['patient_id'] == patient_id) & 
                              (df_all['date'] >= block_start) & 
                              (df_all['date'] < block_end)]
        
        if patient_data.empty:
            summary.loc[patient_id, i] = 'No Data'
        elif patient_data.isna().any().any():
            summary.loc[patient_id, i] = 'Partial Data'
        else:
            summary.loc[patient_id, i] = 'Complete Data'

# Visualize the missing data summary
plt.figure(figsize=(15, 10))
cmap = sns.color_palette(['red', 'yellow', 'green'])
sns.heatmap(summary.applymap(lambda x: {'No Data': 0, 'Partial Data': 1, 'Complete Data': 2}[x]),
            cmap=cmap, cbar=False, annot=True, fmt='')
plt.title('Patient Data Completeness by Yearly Blocks')
plt.xlabel('Time Blocks')
plt.ylabel('Patients')
plt.xticks(ticks=np.arange(0.5, len(blocks)-1.5), labels=[f'Block {i}' for i in range(1, len(blocks))], rotation=45)
plt.show()
