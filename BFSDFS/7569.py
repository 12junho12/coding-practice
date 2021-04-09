from collections import deque

M,N,H=map(int,input().split())

visit=list()
a=list()

dx=[1,-1,0,0,0,0]
dy=[0,0,1,-1,0,0]
dz=[0,0,0,0,1,-1]

for i in range(H):
    a.append([])
    visit.append([])
    for j in range(N):
        a[i].append(list(map(int,input().split())))
        visit[i].append([0]*M)

que=deque()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if a[i][j][k]==1:
                visit[i][j][k]=1
                que.append((i,j,k))


cnt=len(que)
day=-1

while(que):
    x,y,z=que.popleft()

    for i in range(6):
        if 0<=x+dx[i]<H and 0<=y+dy[i]<N and 0<=z+dz[i]<M:
            if visit[x+dx[i]][y+dy[i]][z+dz[i]]==0 and a[x+dx[i]][y+dy[i]][z+dz[i]]==0:
                visit[x+dx[i]][y+dy[i]][z+dz[i]]=1
                a[x+dx[i]][y+dy[i]][z+dz[i]]=1
                que.append((x+dx[i],y+dy[i],z+dz[i]))
    cnt-=1
    if cnt==0:
        day+=1
        cnt=len(que)

cnt2=0
for i in range(H):
    for j in range(N):
        for k in range(M):
            if a[i][j][k]==0:
                cnt2=1
                break
        if cnt2==1:
            break
    if cnt2==1:
        break

if cnt2==1:
    print(-1)

else:
    print(day)
