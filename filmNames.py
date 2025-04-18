import os
import pandas as pd
from datetime import datetime

# Specify the path of the directory
folder_path = r"D:\New folder (2)"

# Check if the directory exists
if not os.path.isdir(folder_path):
    print(f"The directory {folder_path} does not exist.")
else:
    # Get the list of folder names along with their creation dates
    folder_data = []
    for folder in os.listdir(folder_path):
        folder_full_path = os.path.join(folder_path, folder)
        if os.path.isdir(folder_full_path):
            try:
                # Get the creation date of the folder
                creation_time = os.path.getctime(folder_full_path)
                # Convert the creation time to a readable format
                creation_date = datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d %H:%M:%S')
                folder_data.append([folder, creation_date])
            except Exception as e:
                print(f"Error getting creation date for folder {folder}: {e}")

    # Check if folder_data is empty
    if folder_data:
        # Convert the list to a pandas DataFrame
        df = pd.DataFrame(folder_data, columns=['Folder Names', 'Creation Date'])

        # Try saving the DataFrame to an Excel file
        try:
            df.to_excel('folder_names_with_dates.xlsx', index=False)
            print("Excel file saved successfully!")
        except Exception as e:
            print(f"Error saving to Excel: {e}")
    else:
        print("No folders found or an error occurred.")
