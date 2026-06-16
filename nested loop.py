#WAP 
""" PIN=int(input("Enter a PIN: "))
for i in range(0,10):
    for j in range(0,10):
        for k in range(0,10):
            for l in range(0,10):
                if i+j+k+l==10:
                    print ("PIN","= ", i,j,k,l,"__end__")
"""
"""
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j==5:
            print (i,j, "__end__")
"""            
#WAP probability to get % of sum of i+j=5
"""
number = 0
for i in range(1,5):
    for j in range(1,5):
        if i+j==5:
            number= number+1
            print(i,j, "__end__")
    print(number/36*100)"""
"""
#WAP to get % of any number in rolling  two dices


number = 0
for n in range(1,16): #max number we can get
        for i in range(1,5):
            for j in range(1,5):
                for k in range(1,5):
                    if i+j==n:
                        number = number+1
            print(i,j,k, "__end__")

#wap create a clock using nested loop.

x=int(input("enter a time = "))
for i in range(0, 24):
    for j in range(0, 60):
        for k in range(0, 60):
            if i==x:
                print("Hours:", "=", i, "Minutes:", "=", j, "Seconds:", "=", k)
"""

correct_pin = 1234
for i in range(3):
    pin = int(input("Enter PIN: "))
    
    if pin == correct_pin:
        print("Access Granted ✅")
        break
    else:
        print("Wrong PIN ❌")
else:
    print("Card Blocked 🚫")