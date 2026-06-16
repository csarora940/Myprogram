"""
class calcu:
    
    def add (c,d):
        e=c+d
        print("Sum =", e)
    def sub (c,d):
        e= c-d
        print ("Sub=", e)
    def multi (c,d):
        e=c*d
        print ("multi =", e)

ob1=calcu#.add(20,30)
ob1=calcu#.sub(30,20)
ob1=calcu#.multi(10,20)

ob1.add(20,30)
ob1.sub(30,20)  # calling function from the values
ob1.multi(10,20)


    def add (a,b):
        return a+b
    def sub (a,b):
        return a-b
    def multi (a,b=10):
        return a*b

x=calcu.add(30,60)
y=calcu.sub(50,60)  #WARWR with arg with return
z=calcu.multi(30)

print("Sum =", x)
print("Sub=", y)
print("multi =", z)
"""
#WAP a class of bank customer including name, acc no.., balance, DR/Cr entry
class Bank:
    def __init__ (self, name, acc, amt):
        self.name = "Ashish"
        self.acc = 12345
        self.amt = 999
    def greet(self):
        print(f"Hello my name is {self.name}, My acc no is {self.acc}, Available balance is {self.amt}")

p1=Bank("Ashish", 12345, 999)
p1.greet()