import numpy as np
import open3d as o3d
import sys
import os
import imageio.v2 as imageio
import torch

# Depth camera's intrinsic parameters
fx_d = 5.8262448167737955e+02
fy_d = 5.8269103270988637e+02
cx_d = 3.1304475870804731e+02
cy_d = 2.3844389626620386e+02

def convert(file_base, input_path, output_path):
    # create paths for the input images
    depth_path = os.path.join(input_path, "depth", f"{file_base}.png")
    label_path = os.path.join(input_path, "label40", f"{file_base}.png") 
    
    # read the images
    depth_image = imageio.imread(depth_path)
    label_image = imageio.imread(label_path)

    # Convert the image to a numpy array
    depth_image_array = np.array(depth_image)
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

    # Convert the image to a numpy array
    label_image_array = np.array(label_image).astype(np.int64)
    label_height, label_width = label_image_array.shape
    label_GT = label_image_array.reshape(label_height * label_width, 1)

    # Save data
    sample = {'coord':depth_PC, 'semantic_gt':label_GT}

    save_path = os.path.join(output_path, f'{file_base}.pth') 
    torch.save(sample, save_path)
    
    """
    print(depth_PC.shape)
    print(label_GT.shape)
    """



    """
    # Create a point clou data
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)

    # Save the point cloud
    output_path = output_path + f"/{image_name}.pcd"
    o3d.io.write_point_cloud(output_path, pcd)

    print(f'Point cloud saved to {output_path}')
    """
    

def main(input_path, output_path, num_data):

    for i in range(1, num_data + 1):
        file_base = f"{i:06d}"
        convert(file_base, input_path, output_path)
        print(f'Done creating: {file_base}.pth')

    """
    # Define the parts of your path
    input_depth_path = os.path.join(input_path, "depth")
    image_name = "000001"
    file_name = image_name + ".png"
    # Use os.path.join to concatenate the directory and filename
    full_path = os.path.join(input_depth_path, file_name)
    convert(full_path, output_path, image_name)
    """

if __name__ == "__main__":
    # define some things
    input_path = "/root/datasets/NYU_Depth_V2"
    output_path = "/root/datasets/NYU_Depth_V2/dataset"
    num_data = 1449
    
    main(input_path, output_path, num_data)
