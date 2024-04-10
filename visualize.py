from datasets import load_dataset
import numpy as np
import matplotlib.pyplot as plt


cmap = plt.cm.viridis

ds = load_dataset("sayakpaul/nyu_depth_v2")


def colored_depthmap(depth, d_min=None, d_max=None):
    if d_min is None:
        d_min = np.min(depth)
    if d_max is None:
        d_max = np.max(depth)
    depth_relative = (depth - d_min) / (d_max - d_min)
    return 255 * cmap(depth_relative)[:,:,:3] # H, W, C


def merge_into_row(input, depth_target):
    input = np.array(input)
    depth_target = np.squeeze(np.array(depth_target))

    d_min = np.min(depth_target)
    d_max = np.max(depth_target)
    depth_target_col = colored_depthmap(depth_target, d_min, d_max)
    img_merge = np.hstack([input, depth_target_col])
    
    return img_merge


random_indices = np.random.choice(len(ds["train"]), 9).tolist()
train_set = ds["train"]

plt.figure(figsize=(15, 6))

for i, idx in enumerate(random_indices):
    ax = plt.subplot(3, 3, i + 1)
    image_viz = merge_into_row(
        train_set[idx]["image"], train_set[idx]["depth_map"]
    )
    plt.imshow(image_viz.astype("uint8"))
    plt.axis("off")