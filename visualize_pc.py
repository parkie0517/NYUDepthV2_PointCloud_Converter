import open3d as o3d


# Load the PCD file
pcd_path = 'output.pcd'
pcd = o3d.io.read_point_cloud(pcd_path)

# Visualize the point cloud
o3d.visualization.draw_geometries([pcd])