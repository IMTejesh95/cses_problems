
n = int(input())
elements = [ int(i) for i in input().split() ]

nturns = 0
for i in range(n-1):
	diff = 0
	if elements[i+1] < elements[i]:
		diff = elements[i] - elements[i+1]
		elements[i+1] = elements[i]
		nturns += diff

print(nturns)



