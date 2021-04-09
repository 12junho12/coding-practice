N=int(input())

d={}
for i in range(1,N+1):
    d[i]=[]

a=list()
for i in range(N-1):
    a.append(list(map(int, input().split())))
    d[a[i][0]].append(a[i][1])
    d[a[i][1]].append(a[i][0])

c=[0]*N

que=list()
cnt=len(d[1])
c[0]=1
que.append(1)

while(que):
    x=que.pop(0)
    for i in d[x]:
        
        if c[i-1]==0:
            que.append(i)
            c[i-1]=x


c.pop(0)
for i in range(len(c)):
    print(c[i])
