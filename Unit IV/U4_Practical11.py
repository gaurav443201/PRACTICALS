# 11. Program that counts the number of tabs, space and newline character in a file.

file_path = "practical11.txt"

with open(file_path, "r") as file:
    data = file.read()


tabs = data.count("\t")
spaces = data.count(" ")
newlines = data.count("\n")

print("Number of tabs in the file:", tabs)
print("Number of spaces in the file:", spaces)
print("Number of newlines in the file:", newlines)

""" 
Output :
(base) student@ioe-l1lab-14:~$ python3 U4_Practical11.py
Number of tabs in the file: 0
Number of spaces in the file: 27 
Number of newlines in the file: 5
"""