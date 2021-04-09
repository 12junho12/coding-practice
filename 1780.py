from collections import deque

N=int(input())

a=list()
for i in range(N):
    a.append(list(map(int,input().split())))
ans=[0,0,0]
que=deque()
que.append((0,0,N))

while que:
    x,y,n=que.pop()
    b=a[x][y]
   
    bk=0
    
    for i in range(x,x+n):
        for j in range(y,y+n):
            if a[i][j]!=b:
                
                bk=1
                break

        if bk==1:
            break
            

    if bk==0:
        ans[b+1]+=1

    else:
        for k in range(3):
            for p in range(3):
                que.append((int(x+(n/3)*k),int(y+(n/3)*p),int(n/3)))
                
for i in range(3):
    print(ans[i])
