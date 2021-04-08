n=int(input())
p=n
a=[]
b=[]
c=[]
total=0

for i in range(n):
    a.append(list(map(int, input().split())))

a.sort()


for i in range(n):
    b.append(a[i][1])
   

for i in range(n):
    c.append(a[i][0])

m=max(b)
p=b.index(m)

top=0
topi=0

for i in range(p+1):
    if(b[i]>=top):
        total+=(c[i]-topi)*top
        top=b[i]
        topi=c[i]

total+=m

b.reverse()
c.reverse()

top=0
topi=0


for i in range(n-p):
    if(b[i]>=top):
        total+=(topi-c[i])*top
        top=b[i]
        topi=c[i]

print(total)
