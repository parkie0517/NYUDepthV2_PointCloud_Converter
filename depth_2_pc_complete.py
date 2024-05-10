import numpy as np
import open3d as o3d
import sys
import os
import imageio.v2 as imageio
import torch

# Depth camera's intrinsic parameters
# acquired from camera_params.m which is part of the NYU Depth V2's official toolbox
fx_d = 5.8262448167737955e+02
fy_d = 5.8269103270988637e+02
cx_d = 3.1304475870804731e+02
cy_d = 2.3844389626620386e+02



def convert(file_base, input_path, output_path, scale):
    """1. Settings before we begin"""
    # create paths for the input images
    depth_path = os.path.join(input_path, "depth", f"{file_base}.png")
    label_path = os.path.join(input_path, "label40", f"{file_base}.png")
    rgb_path = os.path.join(input_path, "rgb", f"{file_base}.png")
    
    # read the images
    depth_image = imageio.imread(depth_path)
    label_image = imageio.imread(label_path)
    rgb_image = imageio.imread(rgb_path)

    """2. Depth Image Processing"""
    # Convert the depth image to a numpy array
    depth_image_array = np.array(depth_image).astype(np.float64)
    depth_height, depth_width = depth_image_array.shape

    # Create a meshgrid of pixel coordinates
    x = np.linspace(0, depth_width-1, depth_width)
    y = np.linspace(0, depth_height-1, depth_height)
    x, y = np.meshgrid(x, y)

    # Conversion
    Z = depth_image_array
    X = (x - cx_d) * Z / fx_d
    Y = (y - cy_d) * Z / fy_d




    """
    # Filter out points where depth is 0
    mask = depth_image_array > 0
    X = X[mask]
    Y = Y[mask]
    Z = Z[mask]
    """

    # Stack to get a 3D point for each pixel
    depth_PC = np.stack((X, Y, Z), axis=-1)
    depth_PC = depth_PC.reshape(depth_height * depth_width, 3)

    # Scale the Point Cloud
    scaled_depth_PC = depth_PC / scale
    # Aling the Point Cloud
    min_z = scaled_depth_PC[:, 2].min()
    scaled_depth_PC[:, 2] -= min_z

    """3. Label Image Processing"""
    # Convert the label image to a numpy array
    label_image_array = np.array(label_image).astype(np.int64)
    label_height, label_width = label_image_array.shape
    label_GT = label_image_array.reshape(label_height * label_width, 1)


    """4. RGB Image Processing"""
    # Convert the depth image to a numpy array
    rgb_image_array = np.array(rgb_image).astype(np.float64)
    rgb_height, rgb_width, rgb_channel = rgb_image_array.shape # (480, 640, 3)

    # Reshape this rgb image
    reshaped_rgb = rgb_image_array.reshape(rgb_height * rgb_width, rgb_channel)


    """ 5. Save Data """
    sample = {'coord':scaled_depth_PC, 'color':reshaped_rgb, 'semantic_gt':label_GT}

    save_path = os.path.join(output_path, f'{file_base}.pth') 
    torch.save(sample, save_path)

    

def main(input_path, output_path, num_data, scale):

    for i in range(1, num_data + 1):
        file_base = f"{i:06d}"
        convert(file_base, input_path, output_path, scale)
        print(f'Done creating: {file_base}.pth')



if __name__ == "__main__":
    # define some things
    input_path = "/root/datasets/NYU_Depth_V2" # change this!
    output_path = "/root/datasets/NYU_Depth_V2/dataset" # change this!
    num_data = 1449
    scale = 1000.0 # divides the point cloud data
    
    main(input_path, output_path, num_data, scale)