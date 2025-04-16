# 6. Program to understand how characters in a string are accessed using negative indexes.

str1 = input("Enter the string: ")

index = int(input("Enter the index: "))

try :
    print("Character at index -1 is: ", str1[-index])
except Exception as e:
    print(e)

# Added Exception handling to handle the case when the index is out of range.

"""
Output :
(base) student@ioe-l1lab-14:~$ python3 U3_Practical6.py
Enter the string: Python
Character at index -1 is:  n
"""