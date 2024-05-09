cd /root/datasets/NYU_Depth_V2/rgb/

for oldname in nyu_rgb_*.png; do
    # Extract the number part from the filename
    number=$(echo "$oldname" | grep -o '[0-9]\+')
    
    # Format the new filename with leading zeros
    newname=$(printf "%06d.png" "$number")
    
    # Rename the file
    mv "$oldname" "$newname"
done