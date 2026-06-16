"""
age=int(input("Age = "))
if age<13:
    print("Child")
elif age<18:
    print("Teenage")
else:
    print("Adult")



day=3
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("friday")
    case 6:
        print("Saturday")
    case 7:
        print("sunday")
    case _:
        print("Other day")

i=0
while i<6:
    i+=1
    if i==3:
        continue
    print(i)
    """

"""fruits=["apple", "banana", "cherry"]
for i in (fruits):
    if i=="banana":
        break
    print (i)
    """
    
