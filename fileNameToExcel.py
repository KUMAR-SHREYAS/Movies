import os
import pandas as pd

# Specify the path of the directory
folder_path = "D:/New folder (2)"

# Get the list of folder names
folder_names = [folder for folder in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, folder))]

# Convert the list to a pandas DataFrame
df = pd.DataFrame(folder_names, columns=['Folder Names'])

# Save the DataFrame to an Excel file
df.to_excel('folder_names.xlsx', index=False)
