# Create a function that returns the reverse of a list.
class lst:
    a = []

    def data(self):
        n = int(input("Enter size of list:"))
        for i in range(n):
            ele = input("Enter Element:")
            self.a.append(ele)

    def dis(self):
        print("Before :", self.a)
        b=(self.a[::-1])
        print("After :", b)


a = lst()
a.data()
a.dis()
