"""
import heapq
nums = [4, 1, 3]
heapq.heapify(nums)

print(nums[0])

print("ends")
heapq.heappush(nums)

print(nums[0])
"""


#collections module
from collections import Counter
list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10,1,2,3,5,6,4,7,5,8,1,2,3,4,5,6,7,8,9,10]
print(Counter(list))

#math module
import math
print(math.sqrt(16))
print(math.factorial(10))
print(math.gcd(12, 15))
print(math.sin(90))
print(math.cos(90))
print(math.tan(90))