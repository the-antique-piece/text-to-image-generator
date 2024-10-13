import os
import csv
import re  # Import regex module


# Define the path to the dogbreed folder
src = '/home/thebiglion/Downloads/DogBreeds'

# Output CSV file
dest = 'models/data/dog_breeds.csv'

def gen_csv(src, dest):
    # Create the CSV file with the header
    with open(dest, mode='w', newline='') as file:  # Open the destination file, not the source directory
        writer = csv.writer(file)
        writer.writerow(['image_name', 'breed_name'])

        # Iterate over each breed folder
        for breed_folder in os.listdir(src):
            breed_path = os.path.join(src, breed_folder)

            # Check if it's a directory
            if os.path.isdir(breed_path):
                # Iterate over each image in the breed folder
                for image_name in os.listdir(breed_path):
                    if image_name.endswith(('.jpg', '.jpeg', '.png')):  # Check for image file extensions
                        # Remove file extension
                        breed_name = os.path.splitext(image_name)[0]

                        # Remove numbers from the breed name
                        breed_name = re.sub(r'\d+', '', breed_name)
                        image_name = image_name.replace('_','')
                        image_name=re.sub(' ', '_',image_name)

                        # Replace underscores with spaces
                        breed_name = breed_name.replace('_', ' ')
                        breed_name_with_dog="".join([breed_name,' ','dog'])

                        # Write the image name and breed name to the CSV
                        writer.writerow([image_name.lower(), breed_name_with_dog.lower()])


gen_csv(src, dest)
print(f"CSV file '{dest}' generated successfully.")
