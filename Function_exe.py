"""
def reverse():
    n=int(input("enter a number = "))
    rev=0
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev
print("reverse number = ", reverse())
"""

#1.Creating a function
"""
def greet(): #step 1 defining the function
    print("Hello, welcome to tutorial GFG") #printing statement

greet() #calling function for output of statement
"""
print("--------- end of 1 ---------")
"""
#2. using for loop to calling same function multiple times
for i in range(6):
    greet()
"""
print("--------- end of 2 ---------")

#3. Arithmatic Function with Global variable
"""
a=20
b=10  
def sum():
    c=a+b
    print("sum:   ",c)
def sub():
    c=a-b
    print("sub:   ",c)
def multi ():
    c=a*b
    print("multi: ",c)
def div ():
    c=a/b
    print("div:   ",c)
sum()
sub()
multi()
div()
"""
print("--------- end of 3 ---------")

#4. concatenation with global variable
"""
nmea=input("enter your name: ")                #global variable
def greet(name):                               #defining function
    print(f"Hello",name,"\nGo to kitchen",name)   # callling statement
greet(name)                                    #called function for stetement output
"""
print("--------- end of 4 ---------")


#5.a. wap convert ferenhiet into celcuis b. calculate temp in cesius & ferenhiet
"""
ferenhiet=int(input("Temp in ferenheit is : "))
celsius = ((ferenhiet-32)*5)/9
def temp(ferenhiet):
    print("Temp in Celsius is : ", celsius)
    
temp(celsius)
"""
print("--------- end of 5 ---------")

#6.Even or Odd Function checks whether number is even or odd.
"""
a=int(input("Enter num: "))
def Even(a):
    print("Even" if a%2==0 else"Odd")
    if a%2==0:
        print("Even num")
    else:
        print("odd num")
Even(a)
"""
print("--------- end of 6 ---------")

#7. Maximum of 3 Numbers Find largest number using function.
"""
a=int(input("A: "))
b=int(input("B: "))
c=int(input("C: "))
def maximum(a,b,c):
        if a > b and c:
            print("A greater")
        elif b > c and a:
            print("B greater")
        elif c > b and a:
            print("C greater")
        else:
            print("equal")
maximum(a,b,c)
"""
print("--------- end of 6 ---------")

#8. 5. Factorial Function - Using loop.
"""
n=int(input("factorial of : "))
def factorial (n):
        fact=1
        for  i in range(1, n+1):
                fact=fact*i
        print("factorial: ", n, "-", fact)
factorial(n)
"""


#9. Prime Number Function Check if number is prime.
"""
n=int(input("enter num: "))
def prime(n):
        if n>1:
                for i in range(2,n):
                        if n%2==0:
                                print(n, "is not prime num")
                                break
                        else:
                                print(n, "PRIME NO")
        else:
                print("IS NOT PRIME NO. ", n)
prime(n)
"""
#10. Fibonacci Series Return first n Fibonacci numbers.
"""
n=int(input("enter ending no: "))
def fibonacci(n):
    prev=0
    curr=1
    nxt=prev+curr
    n=int(input("enter ending no: "))
    fibonachi=[]
    while nxt>n:
        print("fabonacci", fibonachi)
fibonacci(n)
"""
#11. Reverse number using loop.
"""
n=int(input("enter num:"))
s=str(n)
print(type(s))
for i in range(len(s)-1, -1, -1):
    print((s[i]), end="")
"""

#12. count vowels in list

"""
txt= input("enter word: ")

def vowel(txt):
    if len(txt)!=1:
        print( "only alphabet")
    elif txt.isalpha():
        if txt in "aeiouAEIOU":
            print(txt,"=", " is a vowel")
        else:
            print(txt,"=", " is a consonant")
    else:
        print(txt,"=", " is a numeric")
vowel(txt)
"""
#13. count vowels in list
"""txt=("something is cooking in the kitchen and it smell good")
def count_vowel(txt):
    vowel_lst=[]
    for x in txt:
        if x in "aeiou":
            vowel_lst.append(x)
    print("list:", vowel_lst)
    print("count: ", len(vowel_lst))
#txt=input("char: ")
#p1=count_vowel(txt)
#print("list: ", p1)
count_vowel(txt)
"""

#14 palindrome number checker
n=int(input("Number: "))
