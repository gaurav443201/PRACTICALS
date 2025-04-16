# 5. Program to display the contents of a file. 

# Open the file in read mode
with open('practical5.txt', 'r') as file:
    content = file.read()

# Display the content
print("Contents of the file:")
print(content)


"""
Output :
(base) student@ioe-l1lab-14:~$ python3 U4_Practical5.py
Contents of the file:
hiii
this
is
gaurav
"""
