amt=int(input("Enter amount = " ))  #15900
a=0
if (amt%500==0):
    amt=amt-500         #10000/500 -500=9500
    five=amt//500           # 9500/500 = 19 OR if amount is 10200 -> 10000/500=200, 200*1 OR 
    a=500
    two=1                   #500%200 REMAINDER 100 *1                
    one=1

else:
    five=amt//500
    amt=amt%500
    two=amt//200
    amt=amt%200
    one=amt//100
print("500 * ", five)
print("200 * ", two)
print("100 * ", one)