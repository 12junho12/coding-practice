n=int(input())
m=int(input())

inf=100000000

g=list()

for i in range(n):
    g.append([inf]*n)
    g[i][i]=0

for i in range(m):
    a,b,c=map(int,input().split())
    if g[a-1][b-1]>c:
        g[a-1][b-1]=c

for i in range(n):
    for j in range(n):
        for k in range(n):
            if g[j][k]>g[j][i]+g[i][k]:
                g[j][k]=g[j][i]+g[i][k]

for i in range(n):
    for j in range(n):
        if g[i][j]==inf:
            print(0,end=" ")
        else:
            print(g[i][j], end=" ")
        
    print()
