from collections import deque
import sys

input=sys.stdin.readline

N=int(input())
a=list()
b=set()
visit=list()
visit2=list()
dx=[-1,1,0,0]
dy=[0,0,-1,1]
f=list()
for i in range(N):
    a.append(list(map(int,input().split())))
    b.update(a[i])
    visit2.append([0]*N)
f=sorted(list(b))
area=1


for i in range(len(f)):
    que=deque()
    for j in range(N):
        visit.append([0]*N)
        for k in range(N):
            if a[j][k]==f[i]:
                visit2[j][k]=1
    bk=0
    for j in range(N):
        for k in range(N):
            if visit2[j][k]==0:
                visit[j][k]=1
                que.append((j,k))
                bk=1
                break
        if bk==1:
            break
    cnt=0

    while(que):
        x,y=que.pop()
        for i in range(4):
            if 0<=x+dx[i]<N and 0<=y+dy[i]<N:
                if visit2[x+dx[i]][y+dy[i]]==0 and visit[x+dx[i]][y+dy[i]]==0:
                    visit[x+dx[i]][y+dy[i]]=1
                    que.append((x+dx[i],y+dy[i]))

        if not que:
            cnt+=1
            bk=0
            for j in range(N):
                for k in range(N):
                    if visit2[j][k]==0 and visit[j][k]==0:
                        visit[j][k]=1
                        que.append((j,k))
                        bk=1
                        break
                if bk==1:
                    break

    visit.clear()
    
    if area<cnt:
        area=cnt

print(area)
