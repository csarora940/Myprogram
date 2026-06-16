income = int(input("Enter your Monthly income: "))
age = int(input("Your age: "))
cibil = int(input("CIBIL SCORE: "))
comp =input("Company name: ",)

if income > 25000:
    if age >= 18:   
        if cibil >= 675:
            if comp == "A+":
                print("Eligible")
            else:
                print("Not eligible - Company rating issue")
        else:
            print("Not eligible - Low CIBIL")
    else:
        print("Not eligible - Age criteria not met")

elif income == 25000:
    print("On hold for credit")

else:
    print("Not eligible")


#correct code***
# income = int(input("Enter your Monthly income: "))
#age = int(input("Your age: "))
#cibil = int(input("CIBIL SCORE: "))
#comp = input("Company name: ")

#if income > 25000 and age >= 18 and cibil >= 675 and comp == "A+":
#   print("Eligible")

#elif income == 25000:
#   print("On hold for credit")

#else:
#   print("Not eligible")