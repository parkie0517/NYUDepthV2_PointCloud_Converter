import shutil # import shell utilities moudule
import os

# Define path!
source_dir = '/root/datasets/NYU_Depth_V2/dataset/' # Define the source path of the file
destination_dir = '/root/datasets/NYU_Depth_V2/dataset/train/' # Define the destination path
text_path = '/root/datasets/NYU_Depth_V2/train.txt' # path of the train.txt


with open(text_path, 'r') as file:
    # Read each line in the file one at a time
    for line in file:
        line = line.strip()
        file_base = f'{line}.pth'
        source_path = os.path.join(source_dir, file_base)
        destination_path = os.path.join(destination_dir, file_base)
        shutil.move(source_path, destination_path)
        print(f'Done moving {file_base}')

