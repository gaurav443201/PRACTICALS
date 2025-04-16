# 7. Program that tells and sets the position of the file pointer.

# Open the file in read mode
with open('practical7.txt', 'r') as file:
    # Tell the current position of the file pointer
    pos = file.tell()
    print("Initial file pointer position:", pos)

    # Read 10 characters
    content = file.read(10)
    print("Reading 10 characters:", content)

    # Tell the position again
    pos = file.tell()
    print("File pointer after reading 10 characters:", pos)

    # Move the file pointer back to the beginning
    file.seek(0)
    print("File pointer after using seek(0):", file.tell())

    # Read again from the beginning
    print("Reading from the beginning again:", file.read(10))

""" 
Output :
(base) student@ioe-l1lab-14:~$ python3 U4_Practical7.py
Initial file pointer position: 0
Reading 10 characters: hello btw 
File pointer after reading 10 characters: 10
File pointer after using seek(0): 0
Reading from the beginning again: hello btw
"""