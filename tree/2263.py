from collections import deque

n=int(input())

visit=[0]*n
io=list(map(int,input().split()))
po=list(map(int,input().split()))
pro=list()
que=deque()
que.append((po[n-1],0,n-1,0,n-1))



while que:
    x,s1,e1,s2,e2=que.pop()
    pro.append(x)

    y=io.index(x)
    if y+1 <= e1 and s2+y-s1 <= e2-1:
        que.append((po[e2-1],y+1,e1,s2+y-s1,e2-1))
    if s1 <= y-1 and s2 <= s2+y-s1-1:
        que.append((po[s2+y-s1-1],s1,y-1,s2,s2+y-s1-1))
        

for i in range(n):
    print(pro[i], end=" ")
