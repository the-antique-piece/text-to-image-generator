import os
import re

# Define the path to the DogBreeds folder
folder_path = '/home/thebiglion/Downloads/StanfordBreeds/'

def remove_unwanted_chars(folder_path):
    if os.path.isdir(folder_path):
        for folder in os.listdir(folder_path):
            # Create full path for the current folder
            current_folder_path = os.path.join(folder_path, folder)
            if os.path.isdir(current_folder_path):
                new_folder_name = re.sub(r'^n|\d','',folder)
                new_folder_name=re.sub(r'-','',new_folder_name,count=1)
                new_folder_path = os.path.join(folder_path, new_folder_name) 
                # Rename only if the new name is different
                if current_folder_path != new_folder_path:
                    os.rename(current_folder_path, new_folder_path)
     
# Call the rename function
remove_unwanted_chars(folder_path)
print("Unwanted chars removed.")
