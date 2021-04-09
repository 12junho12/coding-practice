n=int(input())

a=list()
for i in range(n):
    a.append(input())

b=list()
for i in range(n):
    for j in range(len(a[i])):
        if a[i][j] not in b:
            b.append(a[i][j])

c=[0]*len(b)
d=1
for i in range(10):
    for j in range(n):
        if len(a[j])-1>=i:
            c[b.index(a[j][len(a[j])-i-1])]+=d

    d*=10

c.sort(reverse=1)
t=0
for i in range(len(c)):
    t+=(9-i)*c[i]

print(t)
