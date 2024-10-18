#!/bin/bash

# Repository URL
REPO_URL="https://github.com/clemsonciti/rcde_workshops.git"

# Folder you want to download
FOLDER="pytorch"

# Temporary directory name
TEMP_DIR="temp_repo"

# Clone the repository with minimum history
git clone --depth 1 --filter=blob:none --sparse $REPO_URL $TEMP_DIR

# Change to the temporary directory
cd $TEMP_DIR

# Set up sparse checkout
git sparse-checkout set $FOLDER

# Update the working directory
git checkout

# Move the folder to the parent directory
mv $FOLDER ..

# Change back to the parent directory
cd ..

# Remove the temporary directory
rm -rf $TEMP_DIR

echo "The $FOLDER workshop folder has been downloaded successfully."
