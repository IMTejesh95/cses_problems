
missing = 0
# Total number of integers
nums = int(input())
# Integers list 
integers = [ int(n) for n in input().split() ]

size = len(integers)
# Sum of (size+1) natural numbers
total = (size + 1)*(size + 2)//2

missing = total - sum(integers)
print(missing)

