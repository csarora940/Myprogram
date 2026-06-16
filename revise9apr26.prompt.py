# String slicing 1. 1st and last 2. negative indexing 3. reverse string 4. 0 to last.5. last to 0. 6. step size.
n=input("Enter a string = ")
l=len(n)
print("string = ", n)
print("string in reverse order  negative = ", n[::-1])
print("2.string 0 to end = ", n[0::])
print("3.string in reverse order= ",n[::l]) # to print first and last character of string.
print("4. ",n[0:l:2]) # to print alternate characters of string.
print(n[-1:l:-1]) # to print string in reverse order.
print(n)