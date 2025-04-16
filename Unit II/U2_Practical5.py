# 5. Program to determine whether the character entered is a vowel or not. 

# Taking the character as input

char = input("Enter the character : ")

# making vowels list

vowels = ['a', 'e', 'i', 'o', 'u']

if char in vowels:
    print(char, "is a vowel")

else:
    print(char, "is not a vowel")


"""
Output:
(base) student@ioe-l1lab-14:~$ python3 U2_Practical5.py
Enter the character : a
a is a vowel
"""
