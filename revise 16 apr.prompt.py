"""
list=[100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120]
def sum (list):
    return sum(list)
print("sum of list = ", sum(list))
def avg(list):
    return (sum(list)/len(list))
print("avg of list = ", avg(list))  
"""
#Wap input a list of numbers and print sum and  average of the list using function.
"""
list=[]
n=int(input("enter number of elements in list = "))
for i in range (0, n, 1):
    a=int(input("enter element = "))
def sum (list):
        return sum(list)
print("sum of list = ", sum(list))
def avg(list):
        return (sum(list)/len(list))
print("avg of list = ", avg(list))
"""

#Wap assign multiple value to a variable in single line.
"""
a,b,c,=10,20,30
print( a,b,c)
"""
#Wap assing multiple values in list
"""
list=["apple", 123,4.50, True]
print(list)
"""
#Wap to Unpack a Collection of list
"""
list=["apple", 123,4.50, True]
a,b,c,d=list
print(a)
print(b)
print(c)
print(d)
"""
#WAP to Unpack a Collection of list using *
"""
list=["apple", 123,4.50, True]
a,*b=list
print(a)
print(b)
"""
#WAP print global variables
"""
x=123
def globl():
    print("Python is", + x)
    def inner(y):
        print("i'm working with python", +y)
    inner(321)        
globl()
"""
#WAP to print global variable.
"""
def globl():
    global x
    x=123
    print("Python is", + x)
globl()
"""

#WAP Data type
"""
x=5
y=3.14
z="Hello"
print(type(x))
print(type(y))
print(type(z))
"""
#WAP Type conversion of data type into another data type.
"""
x=5
y=3.14
z="Hello"
a=float(x)
b=int(y)
print(float(x))
print(str(y))
print((z))
print(a)
print(b)
"""
#WAP variable casting
"""
x=(float(3))
y=(int(3.14))
z=str("abc")
print(x)
print(y)
print(z)
"""
#wap print function hello
"""
def hello():
    print("Hello")
hello()
"""
#WAP string slicing
a= "Hello, World"
print(a[0:5])
print(a[1])
print("----"*30)
for i in a:
    print (i,end="")