import shutil # import shell utilities moudule
import os

def move_files(source_dir, destination_dir, text_path):
    with open(text_path, 'r') as file:
        # Read each line in the file one at a time
        for line in file:
            line = line.strip()
            file_base = f'{line}.pth'
            source_path = os.path.join(source_dir, file_base)
            destination_path = os.path.join(destination_dir, file_base)
            shutil.move(source_path, destination_path)
            print(f'Done moving {file_base}')

if __name__ == "__main__":
    # Define path!
    source_dir = '/root/datasets/NYU_Depth_V2/dataset/' # Define the source path of the file
    destination_dir = '/root/datasets/NYU_Depth_V2/dataset/test/' # Define the destination path
    text_path = '/root/datasets/NYU_Depth_V2/test.txt' # path of the train.txt or test.txt

    print('Begin moving files! :O')
    move_files(source_dir, destination_dir, text_path)
    print('Moving files complete! :D')