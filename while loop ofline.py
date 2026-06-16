"""
n=int(input("no. = "))#ending range
i=1 #initial variable
dif=1 # 
while i<n:
    print(i, end =" - ")
    print(dif)
    i+=1
    dif=(i*1)+2
"""
"""
n=int(input("no. = "))
i=1 # initial value
#prev=i+1 # series prev value
sum=1 # formula>> prev+current = sum value in 0,1,1,2,3,5,8,13..21
while (n>sum): # run until n is greater than sum
    print(i, end=" - ")
    print(sum)
    i+=1
    sum+=i # series prev value
else:
    print("ends here")
"""    
"""
#WAP input starting and ending num and print all even  b/w them.
n=int(input("enter no.= "))
for i in range(n, (n*10)+1,2):
    if n%2==0:
        print(i, end= " - ")
    else:
        print("odd no")
"""
month=int(input("month = "))
#leap=year/366
year= int(input("enter year = "))
match month :
    case 1  if year % 4 ==0:
        print("Leap year")
    case _ :
        print("NOt leap year")

