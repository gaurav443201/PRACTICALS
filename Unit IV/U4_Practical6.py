'''6. Program to split the line into a series of words and use space to perform the split operation. 
Using Practical 5 file.'''

# Open the file in read mode
with open('practical6.txt', 'r') as file:
    print("Splitting lines into words:\n")
    for line in file:
        words = line.strip().split(' ')
        print(words)



"""
Output :
(base) student@ioe-l1lab-14:~$ python3 U4_Practical6.py
Splitting lines into words:

['hii', 'this', 'is', 'python']

"""