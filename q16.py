# Implement a program that finds the second largest element in a list.
lst=[4,8,5,2,5,7,4,3,2,5,6]
lst=list(set(lst))
lst.sort(reverse=True)
print(lst)
print(lst[1:2])


