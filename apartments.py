f=[[int(i) for i in input().split()] for j in range(3)]
n,m,k=f[0][0],f[0][1],f[0][2]
a=sorted(f[1])
b=sorted(f[2])
i,j,c=0,0,0
while i<n and j<m:
	if a[i]+k < b[j]:
		i+=1
	elif a[i]-k > b[j]:
		j+=1
	else:
		i+=1
		j+=1
		c+=1
print(c)







