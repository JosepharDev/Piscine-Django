#!/bin/bash

echo "=== PIP VERSION ==="
pip --version

echo "===================="

# Folder for the library
LIB_DIR="local_lib"
LOG_FILE="path_install.log"

# Remove old installation if exists
if [ -d "$LIB_DIR" ]; then
    echo "Removing old library..."
    rm -rf "$LIB_DIR"
fi

# Create folder
mkdir -p "$LIB_DIR"

echo "Installing path.py from GitHub..."

# Install path.py
pip install \
    git+https://github.com/jaraco/path.git \
    --target "$LIB_DIR" \
    --upgrade \
    > "$LOG_FILE" 2>&1

# Check if installation succeeded
if [ $? -eq 0 ]; then
    echo "Installation successful ✅"
    echo "Running Python program..."
    python3 my_program.py
else
    echo "Installation failed ❌"
    echo "Check $LOG_FILE"
fi
