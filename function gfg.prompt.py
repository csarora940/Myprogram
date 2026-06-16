#WAP to print a function.
"""
def greet():
    print("Hello, welcome to GeeksforGeeks!")
greet()
"""
#WAP to input message and  print it 5 times using function.
"""
def greet (message):
    for i in range(5):
        print(message)

msg = input("Enter message: ")
greet(msg)
"""
#WAP Global and local variable. scope of the function

#from threading import local

"""
n=int(input("Global variable = "))
def greet():
    n=int(input("Enter a number = "))    # Local variable
    print("Local variable = ", n)
    a=int(input("Enter a number = "))
    def inner(): # nested function ---- inner variable
        print("Inner variable = ", a)
    inner()
    b=int(input("Enter a number = "))
    def deep(): # nested function ---- deep variable 
        print("Deep variable = ", b)
        deep()
    inner()
greet()
print("Global variable = ", n)"""

#WAP to create a function of square and cube of list elements.
"""
list=[1, 2, 3, 4, 5]
def square(list):
    return[ i**2 for i in list]
def cube(list):
    return[i**3 for i in list]
print("square of list = ", square(list))
print("cube of list = ", cube(list))
print("-" *50)
def total(square, cube):
    return [square[i]+cube[i] for i in range(len(square))]
total(square(list), cube(list))
print("total of square and cube = ", total(square(list), cube(list)))
print("-" *50)
def multi(square, cube):
    return [square[i]*cube[i] for i in range(len(square))]
print("multi of square and cube =",  multi(square(list), (cube(list))))
print("-" *50)
"""
#wap to create a function of square and cube of list elements with input from user.
"""
list=[1,2,3,4,5]
def square(list):
    return[ i**2 for i in list]
def cube(list):
    return[i**3 for i in list]
def total(square, cube):
    return [square[i]+cube[i] for i in range(len(square))]
def multi(square, cube): 
    return [square[i]*cube[i] for i in range(len(square))]
def div(square, cube):
    return [square[i]/cube[i] for i in range(len(square))]
print("square of list = ", square(list))
print("-" *50)


print("cube of list = ", cube(list))
print("-" *50)


print("total of square and cube = ", total(square(list), cube(list)))
print("-" *50)


print("multi of square and cube =",  multi(square(list), (cube(list))))
print("-" *50)


print("div of square and cube =", div(square(list), cube(list)))
print("-" *50)
"""
# create a function
"""
b="shekhar"
def greet(b):
    a="Hello"
    print(a,b)
greet(b)
"""
#pass multiple function in it
"""
a=int(input("Numb A: "))
b=int(input("Numb B: "))
def add (a,b):
    c=a+b
    print("add:",c)
def subt (a,b):
    c=a-b
    print("subt:",c)
def guna (a,b):
    c=a*b
    print("guna:",c)
def bhag (a,b):
    c=a/b
    print("Bhag:",c)
def power (a,b):
    c=a**b
    print("power: ",c)
add(a,b)
subt (a,b)
guna(a,b)
bhag(a,b)
power(a,b)
"""

        # OR
#passing the parameters

"""
a=int(input("Numb A: "))
b=int(input("Numb B: "))
def arithmatic(a,b):
    return a+b, a-b, a*b, a//b

a=arithmatic(a,b)
print(a)
"""
#wap to create a function of square and cube of list elements with input from user.
"""
lst=[1,2,3,4,5]
def square(lst):
    return [i**2 for i in lst]
def cube(lst):
    return [i**3 for i in lst]
def total(square, cube):
    return [square[i]+cube[i] for i in range(len(square))]
def total_multi(square, cube):
    return [square[i]*cube[i] for i in range(len(square))]
def total_div(square, cube):
    return [square[i]/cube[i] for i in range(len(square))]
    



print("sq list :" , square(lst))
print("-" *50)
print("cu list :" , cube(lst))
print("-" *50)
print("Total of both :",total(square(lst), cube(lst)))
print("-" *50)
print("Total Multi of both :",total_multi(square(lst), cube(lst)))
print("-" *50) 
print("Total Deiv of both :",total_div(square(lst), cube(lst)))
"""

# WAP to create a function concatnate three list saluation, name and surname together
"""
list3=input("Saluation: ")          #["Mr"]
list1=input("Name: ")               #["Rakesh", "Ravi","Rajesh","Mukesh", "Suraj"]
list2=input("Surname: ")            #["Kumar", "Singh"]
def salu(list3):
    return [i for i in range (len(list3))]
def Name(list1):
    return [i for i in range (len(list1))]
def surname(list2):
    return [i for i in range (len(list2))]
def concat (salu, Name,surname):
    return [(salu)[i]+(Name)[i]+(surname)[i] for i in range (len(list3))]
print("Salu:", (list3))
print("-" *50)
print("Name:", (list1))
print("-" *50)
print("Surname:", (list2))
print("-" *50)
print("Full name :", concat(salu(list3),Name(list1), surname(list2)))
print("-" *50)
"""
# WAP to create a function concatnate three list saluation, name and surname together with input from user using function and for loop
"""
saluation=input("Saluation: ")          #["Mr"]
name=input("Name: ")                    #["ANY NAME"]
surname=input("Surname: ")              #["ANY SURNAME"]
def salu(saluation):
    return [i for i in range (len(saluation))]
def Name(name):
    return [i for i in range (len(name))]
def Surname(surname):
    return [i for i in range (len(surname))]
def concat (salu, Name,surname):
    return [(salu)[i]+(Name)[i]+(surname)[i] for i in range (len(saluation))]
print("Salu:", (saluation))
print("-" *50)
print("Name:", (name))
print("-" *50)
print("Surname:", (surname))
print("-" *50)1

print("Full name :", concat(salu(saluation)+Name(name)+Surname(surname)))
print("-" *50)
"""
#2nd option
"""
def fullname_lst(salu, name, surname):
    fullnames=[]
    for i in range (len(salu)):
        fullname=f"{salu[i]},{name[i]},{surname[i]}"
        fullnames.append(fullname)
    return (fullnames)
salu_lst=[]
name_lst=[]
surname_lst=[]

entries=int(input("num of entries: "))
print("\n enter details :-")
for i in range (entries):
    print(f"\nEntry #{i+1}:")
    salu=input("Enter Mr./Mrs./Miss.: ")
    name=input("Enter name: ")
    surname=input("Enter surname: ")
    salu_lst.append(salu)
    name_lst.append(name)
    surname_lst.append(surname)

print("Saluation list:- ", salu_lst)
print("Name list:- ", name_lst)
print("Surnam list:- ", surname_lst)
full_name=fullname_lst(salu_lst, name_lst, surname_lst)
print("\nfull NAME:-",full_name )
    """
# WAP fibonacci series using function
"""
n=int(input("enter ending no: "))
def fibonacci(n):
    a=0
    b=1
    fib_series=[]
    while a <= n:
        fib_series.append(a)
        a,b=b,a+b
    return fib_series
p1=fibonacci(n)
print("Fibonacci series: ", p1)
"""
n=int(input("enter ending no: "))
def fibonacci(n):
    prev=0
    curr= 1
    fib_series = []
    while prev <= n:
        fib_series.append(prev)
        prev=curr
        curr=prev+curr
    return fib_series
p1 = fibonacci(n)
print("Fibonacci series: ", p1)