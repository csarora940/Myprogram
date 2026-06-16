account = {"name":"Rahul","balance":5000,"acc no.":9901,"pin":1234}
s_pin=1234
attempts=(3)
k = 0
for i in range(attempts):
    u_pin=int(input("Enter PIN: " ))
    if u_pin==s_pin:
        print(f"Welcome Mr.{account['name']},with endingXXX{account['acc no.']}, Avail bal is {account['balance']}")
        k=1 #to run the transaction menu if pin is correct
        break
    else:
        print("Wrong PIN, Try again")
balance= 5000
mini_statement=[]
if k==1:
    while True:
        print ("\n Transaction menu:")
        print ("1. Debit amount")
        print ("2. Credit amount")
        print ("3. check balance")
        print ("4. Mini statement")
        print ("5. EXIT")
        choice= int(input("Enter num (1-5)="))
        match choice:
            case 1:
                amount= float(input("Enter debited amount ="))
                balance+=amount
                mini_statement.append(f"deposited {amount}")
                print ("Available Balance=", balance)
            case 2:
                amount= float(input("Enter dep amount ="))
                if amount > balance:
                    print("\nInsuficient funds, Bal Avail:", balance)
                else:
                    balance-=amount
                    mini_statement.append(f"withdrawal {amount}")
                    print ("Available Balance=", balance)
            
            case 3:
                print ("Available balance is =", balance)

            case 4 :
                for transaction in mini_statement:
                    print ("Recent 10 Transactions =", transaction)
            
            case 5:
                print ("Thanks for banking with us")
                break
            case _:
                print ("Error")
else:
    print("wrong PIN attempt, Try again")
    k=0