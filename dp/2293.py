n,k=map(int,input().split())

a=list()
for i in range(n):
    a.append(int(input()))

b=list()
b=[0]*(k+1)

b[0]=1

for i in range(n):
    for j in range(a[i],k+1):
        b[j]+=b[j-a[i]]

print(b[k])
