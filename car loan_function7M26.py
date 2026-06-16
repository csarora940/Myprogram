#WAP car loan eligibility check of CAR loan amount, income, age, EMI, Margin money.

def car_loan(income, age, ltv):
    if age>21 and income>25000 and ltv>=10:
        return "eligible"
    else:
        return "Not eligible"

age=float(input("Age="))
income=float(input("Monthly income="))
car=float(input("Car value="))
margin_money=float(input("Margin money="))
ltv=(car-margin_money)/car*100
principle=car-margin_money
result=car_loan(income, age, ltv)
def emi(p,r,t):
    rate=r/1200
    tenure=t*12
    emi=((p*r)*(1+r)**t)/((1+r)**t-1)
    return result

r=float(input("ROI="))
t=int(input("Tenure="))
p=principle#int(input("PRINCIPLE ="))#ltv*car/100
result=emi(p,r,t)
print("1. Loan amount=",p)
print("1. Congratulations", result)
print("3. Margin money =", margin_money)
print("4. Emi = ", result)