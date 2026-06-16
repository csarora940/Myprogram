#1. Reverse number
'''
n=int(input("enter num:"))
s=str(n)
print(type(s))
for i in range(len(s)-1, -1, -1):
    print((s[i]), end="")'''
print("\n------------end 1. --------------")

#PRIME NO.
"""
n=int(input("enter num:"))
k=0
for i in range(2,n):
    if n%i==0:
        k=1
        break
if k==0:
    print("PRIME NUM")
else:
    print("NOT PRIME")
"""
print("\n------------end 2. --------------")
#3. fibonacci series
"""
prev=0 #previous number
curr=1 #current number
n=int(input("ending num of series: "))
def fibonacci(prev, curr):
    while prev<=n:  #loop will run untill prev is lesser than equal to ending num
        print(prev, end=",") 
        next=prev+curr # formula to get next num
        prev=curr # now prev is current
        curr=next # then curr will be next numb
fibonacci(prev,curr)
"""
print("\n------------end 3. --------------")

#4. perfect no.
"""
k=0
n= int(input("num : "))
for i in range (1,n):
    if n%i==0 and n%(i+i)==0:
        k=1
        break
if k==1:
    print("perfect no.:", n)
else:
    print("error",n)
"""
        #OR
"""
n=int(input("num : "))
divi=0
for i in range (1,n):
    if n%i==0:
        divi+=i
if divi==n:
    print("perfect no.:", n)
else:
    print("error",n)
"""

#5. Palindrom
"""

n=int(input("Enter num: "))
r=0
k=n
def palindrome(n,k,r):

while n>0:
    d=n%10
    r=r*10+r
    n=n//10

if k==r:
    print("palindrom", n)
else:
    print("no plaindrome")
"""

