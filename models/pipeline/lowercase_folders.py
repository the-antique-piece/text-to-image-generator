import os

# Define the path to the DogBreeds folder
folder_path = '/home/thebiglion/Downloads/DogBreeds/'

def lowercase_folders(folder_path):
    if os.path.isdir(folder_path):
        for folder in os.listdir(folder_path):
            # Create full path for the current folder
            current_folder_path = os.path.join(folder_path, folder)
            if os.path.isdir(current_folder_path):
                new_folder_name = folder.lower()
                new_folder_path = os.path.join(folder_path, new_folder_name) 
                # Rename only if the new name is different
                if current_folder_path != new_folder_path:
                    os.rename(current_folder_path, new_folder_path)
     
# Call the rename function
lowercase_folders(folder_path)
print("Lowercasing of folders completed.")
