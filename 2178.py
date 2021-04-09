dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n,m = map(int, input().split())
a=list()
for i in range(n):
    a.append(list(map(int, input())))

c=list()
d=list()

for i in range(n):
    c.append([False]*m)

for i in range(n):
    d.append([0]*m)

q=list()

q.append((0,0))
c[0][0]=True
d[0][0]=1

while q:
    x,y=q.pop(0)
    for i in range(4):
        if 0<=x+dx[i]<m and 0<=y+dy[i]<n :
            if a[y+dy[i]][x+dx[i]]==1 and c[y+dy[i]][x+dx[i]]==False:
                q.append((x+dx[i],y+dy[i]))
                c[y+dy[i]][x+dx[i]]=True
                d[y+dy[i]][x+dx[i]]=d[y][x]+1


print(d[n-1][m-1])
