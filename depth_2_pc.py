import numpy as np
import cv2
import open3d as o3d
import sys

# Depth camera's intrinsic parameters
fx_d = 5.8262448167737955e+02
fy_d = 5.8269103270988637e+02
cx_d = 3.1304475870804731e+02
cy_d = 2.3844389626620386e+02


# Assuming depth_image is a 2D NumPy array with shape (480, 640)
# and contains depth values in meters

depth_image_path = '10.png'
depth_image = cv2.imread(depth_image_path, cv2.IMREAD_UNCHANGED).astype(np.float32)
height, width = depth_image.shape

print(height, width)


# Create a meshgrid of pixel coordinates
x = np.linspace(0, width-1, width)
y = np.linspace(0, height-1, height)
x, y = np.meshgrid(x, y)

z = depth_image
x = (x - cx_d) * z / fx_d
y = (y - cy_d) * z / fy_d

# Filter out points where depth is 0
mask = depth_image > 0
x = x[mask]
y = y[mask]
z = z[mask]

# Stack to get a 3D point for each pixel
points = np.stack((x, y, z), axis=-1)

# Create Open3D point cloud
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points)

# Save the point cloud
output_path = 'output.pcd'
o3d.io.write_point_cloud(output_path, pcd)

print(f'Point cloud saved to {output_path}')