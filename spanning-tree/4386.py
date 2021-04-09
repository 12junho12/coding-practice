import copy

N=int(input())

a=list()

for i in range(N):
    x,y=map(float,input().split())
    a.append((x,y))

g=list()

for i in range(N):
    g.append([])
    for j in range(N):
        if i!=j:
            g[i].append((((a[i][0]-a[j][0])**2)+((a[i][1]-a[j][1])**2))**(1/2))

        else:
            g[i].append(0)



d=copy.deepcopy(g[0])

t=0

while(1):
    cnt=0
    m=10000000
    mi=0
    for j in range(N):
        if d[j]!=0:
            if d[j]<m:
                m=d[j]
                mi=j

    t+=d[mi]
    d[mi]=0
    for j in range(N):
        if g[mi][j]<d[j]:
            d[j]=g[mi][j]

    for j in range(N):
        if d[j]==0:
            cnt+=1

    if cnt==N:
        break


print('%.2f'%t)
