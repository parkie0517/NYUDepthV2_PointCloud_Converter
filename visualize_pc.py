import numpy as np
import open3d as o3d
import os
import sys

def visualize_point_cloud(file_name):
    # Load PCD file
    pcd = o3d.io.read_point_cloud(file_name)

    # Visualize the point cloud
    o3d.visualization.draw_geometries([pcd])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python visualize_pc.py <filename>")
    else:
        filename = sys.argv[1]
        visualize_point_cloud(filename)