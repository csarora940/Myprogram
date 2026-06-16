#wap Create a food ordering menu using match-case statement.
"""
order = int(input("Enter the food item you want to order: "))    
match order:
    case 1:
        print ("DAL+ROTI")
    case 2:
        print ("sabzi")
    case 3:
        print ("chowmien")
    case _:
        print ("NONE")
"""

#2.WAP Create a language translator (English → Hindi words)
"""
language= input("enter word = ")
match language:
    case "English":
        print("English")
    case "punjabi":
        print("punjabi")
    case "tamil":
        print("Tamil")
    case "HEllo":
        print ("namastey")
    case "evertything":
        print("sab kuch")
    case _:
        print("NONE")
"""

#3.WAP Make a movie ticket booking menu.
"""
slot= int(input("Enter movie slot = "))
day= input("Enter movie day = ")
match slot:
    case 1|3|4 if day=="Monday":
        print ("Spider man")
    case 2|4 if day=="Tuesday":
        print("iron man")
    case 1|3|5 if day=="Wednesday":
        print("Avengers")
    case _:
        print ("NONE")
"""

#4. WAP Build a mobile recharge system
"""
company= input("Enter comp= ")
plan=  int(input("Enter your plan ="))
match plan:
    case 599|799|1299 if company=="Vodafone":
        print ("Vodafone net plan ", plan)
    case 399|999|1099 if company=="Jio":
        print ("Jio net plan ", plan)
    case 799|999|1299 if company=="Airtel":
        print ("Airtel net plan ", plan)
    case 299|499|699 if company=="BSNL":
        printprint ("BSNL net plan ", plan)
    case _:
        print ("NO match")
"""

#5. WAP Create a robot direction controller (left/right/up/down)
"""
horizontal=int(input("press button= "))
vertical=int(input("press button = "))

match horizontal:
    case 8 if vertical==8:              #we can also put all this syntax in while loop if any user hold any side !!!
        print("move up ")
    case 2 if vertical==2:
        print("Move down ")
    case 4 if vertical==4:
        print("Move only left")
    case 6 if vertical==6:
        print ("Move only right")
    case 9 if vertical==9:
        print ("Move only upward right")
    case 3 if vertical==3:
        print ("Move only downward right")
    case 7 if vertical==7:
        print ("Move only upward left")
    case 1 if vertical==1:
        print ("Move only downward left")
    case _:
        print ("STAND BY")
"""

#6. WAP Make a season checker from month number
"""
month= int(input("Enter MOnth number ="))
match month:
    case 11|12|1 :
        print("Winters")
    case 2|3:
        print("Spring")
    case 4|5|6|7:
        print ("Summer")
    case 8|9:
        print("Monsoon")
    case 10:
        print("Autumn")
    case _:
        print("zindagi jhand")
"""
#using if elif else
"""
if month in [11, 12, 1]:
    print("It's Winter")
elif month in [2,3]:
    print("It's Spring")
elif month in [4,5,6, 7, 8]:
    print("It's Summer")
elif month in [8,9]:
    print ("it's Monsoon")
elif month in [10]:
    print("It's Fall")
else:
    print("Invalid month number")
    """

#7. WAP Create a bank transaction menu using match case statement: 1. Credit money 2.Debit money 3. Check balance 4. Mini statement 5.Exit
"""
balance= 5000
mini_statement=[]
while True:
    print ("\n Transaction menu:")
    print ("1. Credit amount")
    print ("2. Debit amount")
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

"""
#8. WAP Make a command-based chatbot using Match/switch case
"""
choice= input("Enter choice= ")
command=float(input("Enter numeric command="))
match command:
    case 1 if choice=="hello":
        print (" Hi , How can i help you")
    case 2 if choice=="Whats your name":
        print ("My name is chandu champion chatbot")
    case 3 if choice=="What you can help me ":
        print ("i can answer simple chat answers")
    case 4 if choice=="India's capital":
        print ("India's capital is'Delhi'")
    case _:
        print ("No keyword")
        """

# while loop
"""
while True:
    choice= input("Enter keyword / input=")
    match choice:
        case "hello":
            print (" Hi , How can i help you")
        case "Whats your name":
            print ("My name is chandu champion chatbot")
        case "What you can helpp me":
            print ("i can answer simple chat answers")
        case "India's capital":
            print ("India's capital is'Delhi'")
        case "Bye":
            print ("Bye, Have a nice day")
            break
   """     
#9. WAP Create a marksheet grading system

"""
Marks=int(input ("Student marks:(0-100) "))
match Marks:

    case Marks if Marks  >= 90:
        print("Grade 'A'")
    case Marks if Marks >= 75:
        print("Grade 'B'")
    case Marks if Marks >= 50:
        print("Grade 'C'")    case Marks if Marks >= 40:
        print("Grade 'D'")
    case Marks if Marks >= 33:
        print("Grade 'FAIL'")
    case _:
        print ("wrong ")
"""


#10. Make a railway reservation menu using match case including
#1. Journey from-to 2. DAte of journey 3. quota (Gen/spec abled / sen citi) 4. class - SL/AC/gen 5. Passenger details (Name:Age:gender)
#6. Birth - Lower/middle/ upper/ Side lower/ side upper


From=input("Station from: ")
To = input("Station to: ")
Date = input("Enter date of journey (DD/MM/YYYY): ")
Quota = input("Enter Quota (Gen/spec abled/ sen citi): ")
Class = input("Enter Class (Gen/AC/Sleeper): ")
Name = input("Enter Your name: ")
Age = int (input("Enter your age :"))
birth_type =  input("Enter Quota (L/M/U/SL/SU: ")

print("\nDear, Your Reservation Details below ")
print(f"Journey starts from '{From}' Journey ends to '{To}'")
print(f"Journey starting '{Date}'")
print(f"Quota selected '{Quota}'")
print(f"Class selected '{Class}'")
print(f"Passenger details Name:'{Name}', Age: '{Age}'")
print(f"Birth preference : '{birth_type}'")

#11. Group words by length using match case and print the grouped words. (list of words is the parameter)
marks={"math":80,"english": 55,"science": 70, "hindi": 45,
    "sanskrit": 70,"sst": 90, "punjabi": 85}
for k, v in marks.items():
    match len(k):
        case 7:
            print(f"{len(k)}:{k}", end=" , ")
        case 6:
            print(f"{len(k)}:{k}", end=" , ")
        case 5:
            print(f"{len(k)}:{k}", end=" , ")
        case 4:
            print(f"{len(k)}:{k}", end=" , ")
        case _:
            print(f"{len(k)}:{k}", end=" , ")