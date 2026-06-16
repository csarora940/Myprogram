#WAP Loan eligiblity check of CAR loan amount, income, age, and credit score.
def carloan(amount, income, age):
    if amount>=600000 and income>=25000 and age>=21 and age<=60:
        return "Eligible for CAR loan"
    
    else:
        return "Not eligible for CAR loan"

#Taking user input
amount = float(input("Enter the CAR loan amount: "))
income = float(input("Enter your monthly income: "))
age = int(input("Enter your age: "))
#Checking eligibility
result = carloan(amount, income, age)
print(result)

#WAP emi calculator for CAR loan amount, interest rate, and tenure.
def emicalculator(amount, interest_rate, tenure):
    monthly_interest_rate = interest_rate / (12 * 100)
    number_of_payments = tenure * 12
    emi = (amount * monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments) / ((1 + monthly_interest_rate) ** number_of_payments - 1)
    return emi
#Taking user input
amount = float(input("Enter the CAR loan amount: "))
interest_rate = float(input("Enter the annual interest rate (in %): "))
tenure = int(input("Enter the tenure of the loan (in years): "))
#Calculating EMI
emi = emicalculator(amount, interest_rate, tenure)
print(f"The monthly EMI for the CAR loan is: {emi:.2f}")
