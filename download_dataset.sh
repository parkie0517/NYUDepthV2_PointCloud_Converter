#!/bin/bash

# Declare an array of URLs
urls=(
    "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/basements.zip"
    "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/bathrooms_part1.zip"
    "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/bathrooms_part2.zip"
    "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/bathrooms_part3.zip"
    "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/bathrooms_part4.zip"
    "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/bedrooms_part1.zip"
    "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/bedrooms_part2.zip"
    "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/bedrooms_part3.zip"
    "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/bedrooms_part4.zip"
    "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/bedrooms_part5.zip"
    "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/bedrooms_part6.zip"
    "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/bedrooms_part7.zip"
    "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/bookstore_part1.zip"
    "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/bookstore_part2.zip"
    "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/bookstore_part3.zip"
    "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/cafe.zip"
    "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/living_rooms_part1.zip"
    "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/living_rooms_part2.zip"
    "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/living_rooms_part3.zip"
    "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/living_rooms_part4.zip"
    http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/dining_rooms_part1.zip
    http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/dining_rooms_part2.zip
    http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/furniture_stores.zip
    http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/home_offices.zip
    "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/kitchens_part1.zip"
    "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/kitchens_part2.zip"
    "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/kitchens_part3.zip"
    "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/libraries.zip"
    "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/studies.zip"
    "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/misc_part1.zip"
    "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/misc_part2.zip"
    "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/offices_part1.zip"
    "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/offices_part2.zip"
    "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/office_kitchens.zip"
    "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/playrooms.zip"
    "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/reception_rooms.zip"
    "http://horatio.cs.nyu.edu/mit/silberman/nyu_depth_v2/study_rooms.zip"
)

# Directory where files will be downloaded and extracted
download_directory="/root/datasets/NYU_Depth_V2"

# Loop over each URL
for url in "${urls[@]}"; do
    echo "Downloading $url..."
    wget -c --show-progress "$url"

    # Extract file name from URL
    file_name=$(basename "$url")

    echo "Unzipping $file_name..."
    unzip -o "$file_name"
done

echo "All files have been downloaded and extracted."