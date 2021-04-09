from collections import deque

R,C=map(int, input().split())

M=list()
for i in range(R):
    M.append(list(input()))

dx=[-1,1,0,0]
dy=[0,0,1,-1]

que=deque()
que2=deque()
visit=list()
visit2=list()

for i in range(R):
    visit.append([0]*C)
    visit2.append([0]*C)

for i in range(R):
    for j in range(C):
        if M[i][j]=="S":
            que.append((i,j))
            visit[i][j]=1
        if M[i][j]=="*":
            que2.append((i,j))
            visit2[i][j]=1

cnt2=len(que2)          
cnt=1
total=1
bk=0
while que:
    
    if cnt2>0 and que2:
        x,y=que2.popleft()
        for i in range(4):
            if x+dx[i]<R and x+dx[i]>=0 and y+dy[i]<C and y+dy[i]>=0:
                if visit2[x+dx[i]][y+dy[i]]==0 and (M[x+dx[i]][y+dy[i]]=="." or M[x+dx[i]][y+dy[i]]=="S"):
                    que2.append((x+dx[i],y+dy[i]))
                    visit2[x+dx[i]][y+dy[i]]=1
                    M[x+dx[i]][y+dy[i]]="*"
        cnt2-=1

    if cnt2==0:    
        x,y=que.popleft()
        cnt-=1
        for i in range(4):
            if x+dx[i]<R and x+dx[i]>=0 and y+dy[i]<C and y+dy[i]>=0:
                if visit[x+dx[i]][y+dy[i]]==0 and M[x+dx[i]][y+dy[i]]=="D":
                    que.append((x+dx[i],y+dy[i]))
                    visit[x+dx[i]][y+dy[i]]=1
                    bk=1
                    break
            
                if visit[x+dx[i]][y+dy[i]]==0 and M[x+dx[i]][y+dy[i]]==".":
                    que.append((x+dx[i],y+dy[i]))
                    visit[x+dx[i]][y+dy[i]]=1

        if cnt==0:
            if bk==1:
                break
            cnt=len(que)
            total+=1
            cnt2=len(que2)
       

if bk==0:
    print("KAKTUS")
else:
    print(total)
