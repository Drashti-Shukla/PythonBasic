# Implement a program that counts the occurrences of each character in a string.

name='Drashti Shukla'
s={x:name.count(x)  for x in set(name)}
print(s)