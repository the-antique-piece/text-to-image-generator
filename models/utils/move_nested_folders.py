import os
import shutil

source_folder = '/home/thebiglion/Downloads/StanfordBreeds'
destination_folder = '/home/thebiglion/Downloads/DogBreeds'
dest_folder_list=[]
for dir in os.listdir(destination_folder):
    dest_folder_list.append(dir)

# Move top-level directories first
for dir in os.listdir(source_folder):
    dir_path = os.path.join(source_folder, dir)
    if os.path.isdir(dir_path):
        destination_dir_path = os.path.join(destination_folder, dir)
        if dir not in dest_folder_list:
            shutil.move(dir_path, destination_dir_path)
            print(f"Moved {dir} to {destination_folder}")

print("Done")