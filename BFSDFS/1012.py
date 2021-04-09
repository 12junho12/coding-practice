from collections import deque
import sys
input = sys.stdin.readline

dx=[0,0,1,-1]
dy=[1,-1,0,0]

T=int(input())

for i in range(T):
    t=0
    M,N,K=map(int,input().split())
    a=list()
    visit=list()
    for j in range(N):
        a.append([0]*M)
        visit.append([0]*M)

    for j in range(K):
        X,Y=map(int,input().split())
        a[Y][X]=1

    que=deque()

    
    for j in range(N):
        for k in range(M):
            if a[j][k]==1 and visit[j][k]==0:
                que.append((j,k))
                visit[j][k]=1
                t+=1
            
                
            while(que):
                y,x=que.pop()

                for p in range(4):
                    if 0<=y+dy[p]<N and 0<=x+dx[p]<M:
                        if a[y+dy[p]][x+dx[p]]==1 and visit[y+dy[p]][x+dx[p]]==0:
                            visit[y+dy[p]][x+dx[p]]=1
                            que.append((y+dy[p],x+dx[p]))

         
   
    print(t)
