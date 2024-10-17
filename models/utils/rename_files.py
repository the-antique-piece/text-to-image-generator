import os
img_name='west_highland_white_terrier'
# Define the path to the Boder_Collie folder
folder_path = f'/home/thebiglion/Downloads/DogBreeds/{img_name}'

def rename_files(folder_path):
    count=1
    
    # Iterate over each image in the Boder_Collie folder
    for image_name in os.listdir(folder_path):
        image_path = os.path.join(folder_path, image_name)

        # Check if it's an image file
        if image_name.endswith(('.jpg', '.jpeg', '.png')):
            str_count=str(count)
            img_extension=image_name.split(".")[1]
            
            new_image_name = "".join([img_name,str_count,'.',img_extension])

            # Construct the full path for the new image name
            new_image_path = os.path.join(folder_path, new_image_name)

             # Rename the image
            os.rename(image_path, new_image_path)
            count+=1
    print(count)
# Call the rename function
rename_files(folder_path)
print("Renaming of images completed.")
