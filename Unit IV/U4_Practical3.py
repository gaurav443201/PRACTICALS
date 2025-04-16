# 3. Program to write a file using the writelines() method. 
# List of lines to write
lines = [
    "Hello, world!\n",
    "This is the second line.\n",
    "And here is the third one.\n"
]

# Open the file in write mode
with open('practical3.txt', 'w') as file:
    file.writelines(lines)

print("Lines written successfully to practical3.txt")


"""
Output :
(base) student@ioe-l1lab-14:~$ python3 U4_Practical3.py
Lines written successfully to practical3.txt
"""