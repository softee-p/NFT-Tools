import os
import json

# Define the folder containing the JSON files
folder_path = r"E:\PythonProjects\NFT\json_folder"

# Iterate through each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        file_path = os.path.join(folder_path, filename)
        
        with open(file_path, 'r') as file:
            data = json.load(file)
             
        # Modify the 'description' field
        if 'description' in data:
            data['description'] = "_"
        
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)
        
        print(f"Processed {filename}")

print("All files processed.")
