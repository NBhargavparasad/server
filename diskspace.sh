#!/bin/bash

# Function to check disk space and display usage
check_disk_space() {
    echo "Checking disk space usage..."
    df -h | awk 'NR==1 || $5+0 > 80 {print $0}'
}

# Run the disk space check
check_disk_space
