'''12. To copy contents of one file to another. While copying a) all full stops are to be replaced with 
commas b) lower case are to be replaced with upper case c) upper case are to be replaced with 
lower case.''' 


file_path = "practical12a.txt"
new_file_path = "practical12b.txt"

with open(file_path, "r") as file:
    data = file.read()

data = data.replace(".", ",")
data = data.swapcase()

with open(new_file_path, "w") as file:
    file.write(data)

print("File copied successfully! with changes")


""" 
Output :
(base) student@ioe-l1lab-14:~$ python3 U4_Practical12.py
File copied successfully! with changes
"""