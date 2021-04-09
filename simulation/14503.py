N,M=map(int, input().split())
r,c,d=map(int,input().split())

a=list()
for i in range(N):
    a.append(list(map(int,input().split())))

dx=[0,1,0,-1]
dy=[-1,0,1,0]
visit=list()
for i in range(N):
    visit.append([0]*M)

while(1):
    visit[r][c]=1
    if (visit[r][c-1]==1 or a[r][c-1]==1) and (visit[r][c+1]==1 or a[r][c+1]==1) and (visit[r-1][c]==1 or a[r-1][c]==1) and (visit[r+1][c]==1 or a[r+1][c]==1):
        if a[r-dy[d]][c-dx[d]]==1:
            break
        else: 
            r-=dy[d]
            c-=dx[d]
    else:
        d-=1
        if d<0:
            d=3
        if visit[r+dy[d]][c+dx[d]]==0 and a[r+dy[d]][c+dx[d]]==0:
            r+=dy[d]
            c+=dx[d]


t=0
for i in range(N):
    for j in range(M):
        if visit[i][j]==1:
            t+=1

print(t)
