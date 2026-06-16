#query
#1. running loop not giving particular denomination of notes
#2. amount asked 2 more times after asking WDL amount
#3. not stopping the syntax after wrong pin (5th attempt)


#1. PIN check & generation
saved_PIN= 1234
attempts=(5)
for i in range (attempts):
    user_pin=int(input("enter pin ="))
    if user_pin==saved_PIN:
        print("pass")
    else:
        print("wrong pin - Try again") #Query - PIN should be input by user and get matched 
        break
    
#2.balcheck
    Avail_bal=20000
    if  user_pin==saved_PIN:
        print("Available balance = ", Avail_bal)
    else:
        print("wrong pin")

#3. Withdrawl limit
    withdrwal_limit=11000
    amt = int(input("enter WDL AMT = "))
    if amt > withdrwal_limit:
        print("Withdrawl less than =",withdrwal_limit)
    elif amt > Avail_bal:
        print("insufficient balance")
    else:
        print("cash withdrawn = ", amt)

#4. denominations/ amount

    a=0
    if (amt%500==0):
        amt=amt-500
        five_notes=amt//500
        a=500
        two_notes=2
        one_notes=3

    else:
        five_notes=amt//500
        amt=amt%500
        two_notes=amt//200
        amt=amt%200
        one_notes=amt//100
    
    #6. Remain bal
    remain_bal=Avail_bal-amt
    print( "Remain balance =", remain_bal )

    
    print("500 * ", five_notes)
    print("200 * ", two_notes)
    print("100 * ", one_notes)
    break