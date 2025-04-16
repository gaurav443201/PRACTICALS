# 1. Program to open a file and print its attribute values. 



# Open the file in read mode
file = open('practical1.txt', 'r')

# Print file attributes
print("File Name:", file.name)
print("File Mode:", file.mode)
print("Is File Closed?", file.closed)

# Close the file
file.close()

# Print again to show it's closed now
print("Is File Closed After Closing?", file.closed)


""" 
Output :
(base) student@ioe-l1lab-14:~$ python3 U4_Practical1.py
File Name: example.txt
File Mode: r
Is File Closed? False
Is File Closed After Closing? True

"""