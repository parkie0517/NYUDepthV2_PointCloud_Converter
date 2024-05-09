import os
import shutil

# Define the source and destination directories
source_dir = '/root/datasets/NYU_Depth_V2/rgb'
destination_dir = '/root/datasets/NYU_Depth_V2/rgb_changed'

# Create the destination directory if it doesn't exist
os.makedirs(destination_dir, exist_ok=True)

# Loop through all files in the source directory
for filename in os.listdir(source_dir):
    if filename.endswith('.png'):
        # Extract the number from the filename
        num = filename.split('_')[-1].split('.')[0]
        # Format the new filename as six-digit number
        new_filename = f'{int(num):06}.png'
        # Define the full source and destination paths
        src_path = os.path.join(source_dir, filename)
        dst_path = os.path.join(destination_dir, new_filename)

        # Copy the file from the source to the destination with the new name
        shutil.copy(src_path, dst_path)
        print(f'{new_filename}.png')

print("Files copied and renamed successfully.")
