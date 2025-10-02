'''
os module – talking to your computer

os lets Python interact with your operating system. You can create folders, list files, check your current directory, and more


'''

# os module

import os

# Current working directory
print(os.getcwd())  # e.g., C:\Users\Mini\Projects

# List files and folders
print(os.listdir())  # shows files/folders in current directory

# Make a new folder
os.mkdir("my_folder")

# Remove a folder
os.rmdir("my_folder")

# Check if a file exists
print(os.path.exists("file.txt"))  # True/False


# sys

import sys
print(sys.version)
print(sys.platform)
