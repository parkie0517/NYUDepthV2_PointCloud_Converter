import numpy as np
import cv2
import open3d as o3d
import sys

def convert(filename):
    # Depth camera's intrinsic parameters
    fx_d = 5.8262448167737955e+02
    fy_d = 5.8269103270988637e+02
    cx_d = 3.1304475870804731e+02
    cy_d = 2.3844389626620386e+02


    depth_image = cv2.imread(filename, cv2.IMREAD_UNCHANGED).astype(np.float32)
    height, width = depth_image.shape

    print(height, width) # Print the size of the depth image


    # Create a meshgrid of pixel coordinates
    x = np.linspace(0, width-1, width)
    y = np.linspace(0, height-1, height)
    x, y = np.meshgrid(x, y)

    # Conversion
    Z = depth_image
    X = (x - cx_d) * Z / fx_d
    Y = (y - cy_d) * Z / fy_d

    # Filter out points where depth is 0
    mask = depth_image > 0
    X = X[mask]
    Y = Y[mask]
    Z = Z[mask]

    # Stack to get a 3D point for each pixel
    points = np.stack((X, Y, Z), axis=-1)

    # Create a point clou data
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)

    # Save the point cloud
    output_path = 'output.pcd'
    o3d.io.write_point_cloud(output_path, pcd)

    print(f'Point cloud saved to {output_path}')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python depth_2_pc.py NAME_OF_THE_DEPTH_IMAGE")
    else:
        filename = sys.argv[1]
        convert(filename)
