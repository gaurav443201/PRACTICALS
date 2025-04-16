# 2. Program to access a file after it is closed 


# Open the file
file = open('practical2.txt', 'r')

# Close the file
file.close()

# Try accessing the file after closing it
try:
    content = file.read()
    print(content)
except ValueError as e:
    print("Error:", e)


"""
Output :
(base) student@ioe-l1lab-14:~$ python3 U4_Practical2.py
Error: I/O operation on closed file.

"""