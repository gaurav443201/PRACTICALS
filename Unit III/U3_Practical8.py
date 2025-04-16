# 8. Program that uses split() to split a multiline string.

str1 = """Hello
World
Python
Java
C
C++"""

print("String before split: ", str1)

# Splitting the string using split() function.

str2 = str1.split("\n")

print("String after split: ", str2)

"""
Output :
(base) student@ioe-l1lab-14:~$ python3 U3_Practical8.py
String before split:  Hello
World
Python
Java
C
C++
String after split:  ['Hello', 'World', 'Python', 'Java', 'C', 'C++']
"""