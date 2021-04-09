from collections import deque
import sys
input = sys.stdin.readline

N=int(input())
W=list()
que=deque()
for i in range(N):
    W.append(list(map(int,input().split())))

m=1e9

for i in range(N):
    que.append((i,0,0))
    a=list()
   
    while(que):
        x,y,z=que.pop()
        if y==N-1:
            if W[x][i]!=0 and m>z+W[x][i]:
                m=z+W[x][i]
            continue
                      

        while len(a)-1>=y:
            a.pop()

        a.append(x)
       
        for j in range(N):
            if j not in a:
                if W[x][j]!=0 and z+W[x][j]<m:
                    que.append((j,y+1,z+W[x][j]))
       
print(m)
        
