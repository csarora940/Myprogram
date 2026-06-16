#1. zip () & add()
"""
import numpy as np

x=[1,2,3,4]
y=[5,6,7,8]
z=[]
for i , j in zip(x,y):
    z.append(x+y)
print(z)
"""
 #add(), subtract(), multiply(), divide(), mod(),power(), remainder(), divmod()
"""
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

addition = np.add(arr1, arr2)
subtract = np.subtract(arr1, arr2)
multiply = np.multiply(arr1, arr2)
divide   = np.divide(arr1, arr2)
mod      = np.mod(arr1, arr2)
power    = np.power(arr1, arr2)
remainder = np.remainder(arr1, arr2)
divmod = np.divmod(arr1, arr2)

print(addition)
print ("1","---"*30)

print(subtract)
print ("2","---"*30)

print(multiply)
print ("3","---"*30)

print(divide)
print ("4","---"*30)

print(mod)

print ("5","---"*30)
print(power)

print ("6","---"*30)
print(remainder)

print ("7","---"*30)
print(divmod)
print ("8","---"*30)
"""

#2.  Truncations
import numpy as np
"""
arr1 = np.trunc([-3.1666, 3.0006]) #it will retrun nearest to nearest to zero
print("1.Trunc", arr1)
arr2=np.fix([-3.16667,3.0006]) #it will retrun nearest to increasing positive number
print("2.fix", arr2)
arr3=np.floor([-3.16667,3.0006]) #it will retrun nearest to increasing positive number
print("3.floor", arr3)
arr4=np.ceil([-3.16667,3.0006]) #it will retrun nearest to increasing positive number
print("4.ceil", arr4)
arr5=np.around([3.16667, 2]) # it will retrun 2 decimal space to (.)
print("5.around", arr5)
arr6=np.around([3.16667,1]) #it will retrun 1 decimal space to (.)
print("6.around", arr6)
arr7=np.around([3.16667,0]) #it will return decimal range of 0 after (.)
print("7.around", arr7)
arr8=np.around([13.16667,1]) #it will return in range of 10-20 nearest to its range
print("8.around", arr8)
arr9=np.around([183.16667,-2])#it will return in range of 100-200 nearest to its range
print("9.around", arr9)
"""

#3. summations axis 1 & axis 0
"""
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])
#summation axiis 1
z=np.sum([arr1, arr2], axis=1) #it will print output horizontaly
print(z)
print("-------- axis 1 --------")
#summation axiis 0
y=np.sum([arr1, arr2], axis=0) # it will print output of array in vertical
print(y)
print("-------- axis 0--------")
#cumsum
x=np.cumsum(arr1)
print(x) # it will print cumulatively sum of all digits (10+11, )
print("-------- cum sum--------")
#product ufunc
x1=np.prod([arr1, arr2])
print(x1) #it will print arr into multiplicatio itself within each digits
print("-------- product--------")
#cumproduct ufunc
x2=np.cumprod([arr1,arr2])
print(x2)
print("-------- cumproduct--------")
#Numpy difference
arr3 = np.array([10, 9, 12, 16, 14, 15])
x3=np.diff([arr3])
print(x3)
"""
print("-------- difference--------")
"""
x4=np.diff(arr3, n=2)
print(x4)
"""
print("-------- difference--------")

#Numpy LCM find lowest common multiple, 
"""
a=16
b=18
z=np.lcm(a,b) #it will multiple of common divisors 
print(z)
"""
print("-------- LOWEST COMMON MULTIPLE--------")

#Numpy LCM reduce()method will use the ufunc, function, on each element, and reduce the array by one dimension.
"""
y=np.lcm.reduce([10,20,30])
print(y)

#Numpy LCM reduce in range
arr=np.arange(1,5)
x=np.lcm.reduce(arr)
print(x)
"""

#Numpy GCD (greatest common divisor) or HCF(higher common factor)
"""
c=16
d=36
y=np.gcd(c,d)
print(y)
"""
print("-------- GREATEEST COMMON DIVISOR--------")

#Numpy gcd finder by reduce()
"""
arr3 = np.array([18, 9, 12, 48, 36, 24])
x=np.gcd.reduce(arr3)
print (x)
"""
print("-------- GCD find with reduce --------")

#find unique in array
"""
arr3 = np.array([18, 9, 12, 48, 36, 9, 48, 36, 24,18, 9, 12, 48, 24])
arr2 = np.array([18, 9, 12, 48, 36])
x=np.unique(arr3)
print(x) #it will merged the copied items in single element and print it
"""
print("--------unique --------")
#Finding Union To find the unique values of two arrays, use the union1d() method.
"""
arr3 = np.array([18, 9, 12, 48, 36, 9, 48, 36, 24,18, 9, 12, 48, 24])
arr2 = np.array([18, 9, 12, 48, 36])

y=np.union1d(arr3,arr2)
print(y)#it will merge two array into one.
"""
print("--------Union --------")

#Finding Intersection To find only the values that are present in both arrays, use the intersect1d() method.
"""
arr3 = np.array([18, 9, 12, 48, 36, 9, 48, 36, 24,18, 9, 12, 48, 24])
arr2 = np.array([18, 9, 12, 48, 36])
z=np.intersect1d(arr3,arr2) #it will create a list of similar array in one
print(z)
"""
print("--------intersection --------")

#Finding Difference To find only the values in the first set that is NOT present in the seconds set, use the setdiff1d() method.
"""
arr3 = np.array([18, 9, 12, 48, 36, 9, 48, 36, 24,18, 9, 12, 48, 24])
arr2 = np.array([18, 9, 12, 48, 36])
z=np.setdiff1d(arr3,arr2, assume_unique=True) #it will create a list of different array in one
z=np.setdiff1d(arr3,arr2)
print(z)
"""
print("--------set difference --------")

#Finding Symmetric Difference To find only the values that are NOT present in BOTH sets, use the setxor1d() method.

"""
arr3 = np.array([18, 9, 12, 48, 36, 24])
arr2 = np.array([ 12, 48, 36])
z=np.setxor1d(arr3,arr2, assume_unique=True) #it will create a list of different array in one

print(z)
"""
print("--------symmetrci difference --------")
"""
arr = np.array([1,2,3,4,5,6,7,8,9,10],dtype='f') #to convert in float
print(arr)
print(type(arr))
"""

from numpy import random

x = random.normal(size=1000, loc=50, scale=0.2)

print(x)


