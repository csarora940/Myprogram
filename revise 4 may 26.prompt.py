#WAP check character type (vowel/consonant)
"""
char=input("Enter char = ")
if len(char)!=1:
    print("only alphabet")
elif char.isalpha():
    if char in "aeiouAEIOU":
        print("vowel")
    else:
        print("consonat")
else:
    print("numeric")
                #OR
char=input("Enter char = ")
if char in"aeiouAEIOU":
    print("vowel")
else:
    print("Consonant")"""

#WAP ATM withdrawal, condition:(BAl check + withdrawl limit)
"""
PIN= int(input("enter pin ="))

if PIN==1234:
    print("pass")
else:
    print("wrong pass")     #Query - PIN should be input by user and get matched 
#condition 1. Bal check 2. Withdrawl limit
bal=17000
if bal>=17000:
    print("Available balance = ", bal)
else:
    print("No sufficient bal")

#2. Withdrawl limit
withdrwal_limit=int(input("enter amount = "))

if withdrwal_limit<=10000:
    remain_bal=bal-withdrwal_limit
    print("Withdrawl=",withdrwal_limit, "Remain balance =", remain_bal )
else:
    print("out of limit") 
"""
#12. count vowels in list
from itertools import count


txt= input("Enter string = ")
def vowels(txt):
    for i in range (len(txt)):
        if txt[i] in "aeiouAEIOU":
            print(i, "vowel")
        else:
            print("constant")