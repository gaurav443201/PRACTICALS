# 4. Program to append data to an already existing file. 

# Data to append
new_data = "This line is added to the existing file.\n"

# Open the file in append mode
with open('practical4.txt', 'a') as file:
    file.write(new_data)

print("Data appended successfully to practical4.txt")



"""
Output :
(base) student@ioe-l1lab-14:~$ python3 U4_Practical4.py
Data appended successfully to practical4.txt
"""