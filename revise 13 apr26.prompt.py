#WAp find the runnerup score in a list.
"""
list=[10, 20, 30, 40, 50]
list.sort()
print("runnerup score = ", list[-2], "and highest score = ", list[-1])
"""

#Wap find the runnerup score in a list without using sort function.
"""
list=[10, 20, 30, 40, 50]
max1=0
max2=0
for i in list:
    if i>max1:
        max2=max1
        max1=i
print("runnerup score = ", max2, "and highest score = ", max1)
"""
#Wap find the runnerup score in a list with function.
"""
def runnerup(list):
    max1=0
    max2=0
    for i in list:
        if i>max1:
            max2=max1
            max1=i
    return max2, max1
    """
#Wap find the runnerup score in a list with function and input from user.
"""
list=[]
n=int(input("enter number of elements in list = "))
for i in range(0,50,5):
    a=int(input("enter element = "))
    list.append(a)
"""
