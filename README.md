# NYUDv2_Depth_Image_to_Point_Cloud

## 1. Installation
- conda create -n NYUDv2 python=3.11
- conda activate NYUDv2
- pip install numpy opencv-python open3d

## 2. Code Usage
- Converting
    - python depth_2_pc.py NAME_OF_THE_DEPTH_IMAGE_FILE
- Visualizing
    - python visualize_pc.py NAME_OF_THE_POINT_CLOUD_FILE