# NYUDv2_Depth_Image_to_Point_Cloud ⬜

## What is this repo for?! ⬜
I am trying to convert NYU Depth V2 dataset to point cloud dataset.

## Prerequisites ✅
- Depth Image
- Point Cloud
- Coding skills (Linux, Python, Numpy, Conda)
- 3D Geometry (Coordinate System, Calibration)

## What I need to do (⬜, ✅)
This is for my own reference, you do not need to read this section.
- Download the NYU Depth V2 Data ✅
    - RGB, Depth, Label40, train.txt, test.txt
    - Check if they are downloaded well
    - RGB was downloaded from [Github Repo](https://github.com/ankurhanda/nyuv2-meta-data?tab=readme-ov-file)
    - I got the rest from my colleague (Ph.D. Course Soyun Choi)
- Donwload S3DIS [Download Form](https://docs.google.com/forms/d/e/1FAIpQLScDimvNMCGhy_rmBA2gHfDu3naktRm6A8BPwAWWDv-Uhm6Shw/viewform?c=0&w=1&fbzx=5903082483074287663)
    - Understand how S3DIS is composed
- Find the neccessary matrices for the conversion process ⬜
    - 
- Understand the S3DIS dataset format ⬜
- Preprocess the data ⬜
- Create the conversion code ⬜
- Create a visualization code ⬜
- Complete writing the github README file to share knowledge with others! ⬜
- ⬜
- ⬜
- ⬜

## Prepare NYU Depth V2 Data ⬜
- RGB, Depth, Label, train.txt, test.txt, calibration information
- Download the files above by clicking on this link()

## 1. Installation
- conda create -n NYUDv2 python=3.11
- conda activate NYUDv2
- pip install numpy opencv-python open3d

## 2. Code Usage
- Converting
    - python depth_2_pc.py NAME_OF_THE_DEPTH_IMAGE_FILE
- Visualizing
    - python visualize_pc.py NAME_OF_THE_POINT_CLOUD_FILE
 
## 3. Reuslt
![image](https://github.com/parkie0517/NYUDv2_Depth_Image_to_Point_Cloud/assets/80407632/f56250b5-c9bb-42b9-9396-0a85883e991f)
