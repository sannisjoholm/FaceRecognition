import os

# Set the directory
directory = "training/Ahtisaari"

# Give the name for the files
base_name = "Ahtisaari"

# Loop through the files in directory
for index, filename in enumerate(os.listdir(directory), start=1):
    file_path = os.path.join(directory, filename)
    if os.path.isfile(file_path):
        extension = os.path.splitext(filename)[0]
        new_name = f"{base_name}_{index}{extension}"
        new_path = os.path.join(directory, new_name)
        os.rename(file_path, new_path)

print("Files are renamed!")