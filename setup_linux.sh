#!/bin/bash

# Fetch the HTML content of the Zig download page
page_content=$(curl -s https://ziglang.org/download/)

# Extract the link for the latest Linux x86_64 release (excluding the master branch)
latest_link=$(echo "$page_content" | grep -oP '(?<=href=")[^"]*zig-linux-x86_64-[^"]*\.tar\.xz(?=")' | grep -v "master" | head -n 1)

# Check if latest_link is empty
if [ -z "$latest_link" ]; then
    echo "No latest Zig release found for Linux x86_64."
    exit 1
fi

# Prefix the extracted link with the base URL
base_url="https://ziglang.org"
full_link="${base_url}${latest_link}"

# Output the full download link
echo "Latest Zig release for Linux x86_64: $full_link"
