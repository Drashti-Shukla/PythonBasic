# Write a program to read a text file and count the number of words

with open('abc', 'r') as file:
    content = file.read()
    lst=content.split(' ')
    print(len(lst))