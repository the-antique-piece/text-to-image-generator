import os

# Define the path to the Boder_Collie folder
folder_path = '/home/e/thebiglion/ImageDownloader/unsplash_images/'

def rename_files(folder_path):
    # Iterate over each image in the Boder_Collie folder
    for image_name in os.listdir(folder_path):
        image_path = os.path.join(folder_path, image_name)

        # Check if it's an image file
        if image_name.endswith(('.jpg', '.jpeg', '.png')):

            # If the image name starts with 'Boder', replace 'Boder' with 'Border'
            if image_name.startswith('Boder'):
                # Replace 'Boder' with 'Border' in the image name
                new_image_name = image_name.replace('Boder', 'Border')

                # Construct the full path for the new image name
                new_image_path = os.path.join(folder_path, new_image_name)

                # Rename the image
                os.rename(image_path, new_image_path)
                print(f'Renamed: {image_name} -> {new_image_name}')

# Call the rename function
rename_files(folder_path)
print("Renaming of images completed.")
