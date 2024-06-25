# Write a program to generate the Fibonacci sequence up to a specified term.
def febonacci(no):
    a=0
    b=1
    for i in range(no):
        print(a, end=" ")  # a:0;    a:1;       a:2
        c = a + b  # c=0+1=1; c= 1+1=2;  c=1+2=3
        a = b  # a=1    ; a=1;       a=2
        b = c

febonacci(12)