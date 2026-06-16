# wap create a calculator with Argumental parameters!!!
"""
def add(a, b):
    c=a+b
    print("sum = ", c)

def sub(a, b):
    c=a-b
    print("sub = ", c)
def multi(a, b):
    c=a*b
    print("multi = ", c)
def div(a, b):
    c=a/b
    print("div = ", c)
def modd(a, b):
    c=a%b
    print("modulas = ", c)

print("1.addition")
print("1.subtraction")
print("1.multiplication")
print("1.division")
print("1.modulas")
op= int(input("enter ur option = "))

match op:
    case 1:
        add(a, b)
    case 2:
        sub(a,b)
    case 3:
        multi(a,b)
    case 4:
        div(a,b)
    case 5:
        modd(a,b)
    case _:
        print("error")
        """
        
# wap create a calculator without Argumental parameters!!!
def add(): # no need to enter variable in conditiiion of inputin the values
# a=int(input("enter A = "))
    #b=int(input("enter B = "))
    c=a+b
    print("sum = ", c)

def sub():
    a=int(input("enter A = "))
    b=int(input("enter B = "))
    c=a-b
    print("sub = ", c)
def multi():
    a=int(input("enter A = "))
    b=int(input("enter B = "))
    c=a*b
    print("multi = ", c)
def div(a, b):
    a=int(input("enter A = "))
    b=int(input("enter B = "))
    c=a/b
    print("div = ", c)
def modd(a, b):
    a=int(input("enter A = "))
    b=int(input("enter B = "))
    c=a%b
    print("modulas = ", c)

print("1.addition")
print("1.subtraction")
print("1.multiplication")
print("1.division")
print("1.modulas")
op= int(input("enter ur option = "))

match op:
    case 1:
        a=int(input("enter A = "))
        b=int(input("enter B = "))
        add() # no need to enter variable in conditiiion of inputin the values
    case 2:
        a=int(input("enter A = "))
        b=int(input("enter B = "))
        sub()
    case 3:
        a=int(input("enter A = "))
        b=int(input("enter B = "))
        multi()
    case 4:
        a=int(input("enter A = "))
        b=int(input("enter B = "))
        div()
    case 5:
        a=int(input("enter A = "))
        b=int(input("enter B = "))
        modd()
    case _:
        print("error")


#Wap create a calculator using match case without argumental parameters and without taking input in the function.
"""
a=int(input("enter A = "))
b=int(input("enter B = "))
print("1.addition")
print("1.subtraction")
print("1.multiplication")
print("1.division")
print("1.modulas")
op= int(input("enter ur option = "))
match op:
    case 1:
        c=a+b
        print("sum = ", c)
    case 2:
        c=a-b
        print("sub = ", c)
    case 3:
        c=a*b
        print("multi = ", c)
    case 4:
        c=a/b
        print("div = ", c)
    case 5:
        c=a%b
        print("modulas = ", c)
    case _:
        print("error")
"""