import os
import json

# This script is an example of how to edit a folder
# of metadata.json to be compliant with the loopring format.
# It takes a folder's CID containing other files and appends
# the file name. Essentially you want your links to look like
# ipfs://CID/1.json
# ipfs://SAMECID/2.json
# etc


# Define the folder containing the JSON files
folder_path = r"E:\PythonProjects\NFT\json_folder"

# Define traits to replace
trait_to_search = "Trait"
new_value = "New_Value"

# Iterate through each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith('.json'):
        file_path = os.path.join(folder_path, filename)
        
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        # Remove unwanted fields
        if 'compiler' in data:
            del data['compiler']
        if 'creators' in data:
            del data['creators']
        if 'external_url' in data:
            del data['external_url']
        
        # Update the 'image' field
        if 'image' in data:
            image_filename = data['image']
            data['image'] = f"ipfs://YOUR_CID_HERE/{image_filename}"

        # You can use the same code snipped from above for the 'animation_url'
        #
        #
        #

        # Search for the specific trait_type in the attributes
        if 'attributes' in data:
            attributes = data['attributes']
            for attribute in attributes:
                if attribute.get('trait_type') == trait_to_search:
                    attribute['value'] = new_value
        
        # Modify the 'properties' field
        if 'properties' in data:
            data['properties'] = {}
        
        # Modify the 'description' field
        if 'description' in data:
            data['description'] = "new description"
        
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)
        
        print(f"Processed {filename}")

print("All files processed.")
