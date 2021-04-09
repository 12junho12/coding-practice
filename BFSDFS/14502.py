from collections import deque
import copy

N,M=map(int,input().split())

lab=list()

for i in range(N):
    lab.append(list(map(int,input().split())))

a=list()

for i in range(N*M-2):
    if lab[i//M][i%M]==0:
        for j in range(i+1,N*M-1):
            if lab[j//M][j%M]==0:
                for k in range(j+1,N*M):
                    if lab[k//M][k%M]==0:
                        a.append((i,j,k))

dx=[1,-1,0,0]
dy=[0,0,1,-1]
max=0
que=deque()
lab2=copy.deepcopy(lab)

for i in range(N):
    for j in range(M):
        if lab[i][j]==2:
            que.append((i,j))
 
que2=copy.deepcopy(que)

for t in range(len(a)):
    lab2[a[t][0]//M][a[t][0]%M]=1
    lab2[a[t][1]//M][a[t][1]%M]=1
    lab2[a[t][2]//M][a[t][2]%M]=1
    
    while que2:
        x,y=que2.pop()
        for i in range(4):
            if 0<=x+dx[i]<N and 0<=y+dy[i]<M:
                if lab2[x+dx[i]][y+dy[i]]==0:
                    que2.appendleft((x+dx[i],y+dy[i]))
                    lab2[x+dx[i]][y+dy[i]]=2
    

    total=0
    for i in range(N):
        for j in range(M):
            if lab2[i][j]==0:
                total+=1

    if total>max:
        max=total
        
    que2=copy.deepcopy(que)
    lab2=copy.deepcopy(lab)

print(max)
  
    
