# 9. Program that changes the current directory to our newly created directory.

import os

# Path to the new directory (you can modify the path as needed)
new_directory = "new_directory"  # or provide a full path like "C:/path/to/directory"

# Create the directory if it doesn't exist
if not os.path.exists(new_directory):
    os.makedirs(new_directory)
    print(f"Directory '{new_directory}' created.")

# Change the current working directory to the new directory
os.chdir(new_directory)

# Display the current working directory
print(f"Current directory is now: {os.getcwd()}")



""" 
Output :
(base) student@ioe-l1lab-14:~$ python3 U4_Practical9.py
Directory 'new_directory' created.
Current directory is now:/home/student/new_directory
"""
