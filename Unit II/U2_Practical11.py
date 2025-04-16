# 11. Program to various patterns of * 
# Since question is not clear, I am assuming it will take a value from user and print the pattern of * upto that value.
# For example, if user enters 5, then it will print the following pattern:
# *
# **
# ***
# ****
# *****

number = int(input("Enter a number : "))

for i in range(1,number+1) :
    print("*"*i)
    continue

# A simpler version 

# for i in range(1,number+1) :
#     for j in range(i) :
#         print("*",end="")
#         continue
#     print()

"""
Output:
(base) student@ioe-l1lab-14:~$ python3 U2_Practical11.py
Enter a number : 3
*
**
***
"""