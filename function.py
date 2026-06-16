# wap creat a function to create a list and print the elements of list.
"""
def list():
    list=["apple", "banana", "cherry", "dog", "elephant"]
    return list
x=list()
print(x[0])
print(x[1])
print(x[2])
print(x[3])
print(x[4])

#wap to create a function to print multiple functions with single value.
def multi(a,b):
    c=a*b
    e= a+b
    d=a-b
    f=a/b
    ll=[c,d,e,f]
    return ll

c3=multi(10, 20)
print("multi = ", c3[0])
print("sum = ", c3[2] )
print("sub = ", c3[1])
print("div = ", c3[3])

"""
#wap to create a function to take input from user and print the list."
"""
l=[]
n=int(input("enter number of elements in list = "))
for i in range (0, n, 1):
        a=int(input("enter element = "))
        l.append(a)
print("list = ", l)
"""
#wap input a number and print reverse of the number using function.

"""
def number():
    num=int(input("enter a number = "))
    l=len(str(num))
    return num,l
num, l = number()
print("reverse number = ", str(num)[::-1])

for i in range(0, l-1, -1):
    print("reverse num=", str(num)[::-1])             
    print("reverse num=", str(num)[i])
    print("reverse num = ", str(num)[-1:len(str(a))-1])
"""
#5. Factorial Function Using loop.
"""
def factorial(n):
    fact=1
    for i in range(1, n+1):
        fact=fact*i
    print("factorial = ",n,"*",n, "=",fact)
n=6 #int(input("enter a number = "))
factorial(n)
"""
#6.Prime Number Function Check if number is prime.
"""
n=int(input("enter a number = "))
def prime(n):
    if n>1:
        for i in range(2, n):
            if (n%i)==0:
                print(n, "is not a prime number")
                break
            else:
                print(n, "is a prime number")
    else:
        print(n, "is not a prime number"   
prime(n)
"""
