# Create a function that takes a list of numbers and returns a new list containing only the even numbers.

lst = []


def initialization():
    no = int(input("Enter Size of List:"))
    for i in range(no):
        ele = int(input("Enter Element:"))
        lst.append(ele)
    print(lst)


def even():
    lst2 = [i for i in lst if i % 2 == 0]
    print(lst2)


initialization()
even()
