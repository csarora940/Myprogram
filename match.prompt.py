#WAP leap year  or not.

"""
year = int(input("enter year = "))
month =3 #int(input("enter month = "))
v = year % 4==0 
match v:
    case 0:
        print("Leap year")
    case 1 :
        print("not Leap year")
"""
#WAP input month & year , nand print whether its leap along with num of day of with month name.
"""
year = int(input("Enter year = "))
month = int(input("Enter month = "))
leap = year % 4
if (year % 4 == 0, leap):
    print("leap year")
else:
    print ("not leap")
match month:
    case 1:
        print("January - 31 days")
    case 2:
        if leap==0:
            print("February - 29 days (Leap Year)")
        else:
            print("February - 28 days (Not Leap Year)")
    case 3:
        print("March - 31 days")
    case 4:
        print("April - 30 days")
    case 5:
        print("May - 31 days")
    case 6:
        print("June - 30 days")
    case 7:
        print("July - 31 days")
    case 8:
        print("August - 31 days")
    case 9:
        print("September - 30 days")
    case 10:
        print("October - 31 days")
    case 11:
        print("November - 30 days")
    case 12:
        print("December - 31 days")
    case _:
        print("Invalid month")
if leap==0:
    print("It is a Leap Year")
else:
    print("It is NOT a Leap Year")"""
    


month = int(input("enter month ="))
day = int(input("enter day ="))
match day:
    case 1 | 2 | 3 | 4 | 5 if month == 3:
        print ("A weekday in March")
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("A weekday in April")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("A weekday in May")
    case _:
        print("No match")
