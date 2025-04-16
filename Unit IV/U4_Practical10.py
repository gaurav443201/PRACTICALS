# 10. Program to print the absolute path of a file using os.path.join 

import os


directory = "Unit IV"
filename = "practical10.txt"

file_path = os.path.join(directory, filename)

absolute_path = os.path.abspath(file_path)

print("Absolute path of the file:", absolute_path)

""" 
Output :
(base) student@ioe-l1lab-14:~$ python3 U4_Practical10.py
Absolute path of the file: /home/student/Unit IV/practical10.txt
"""