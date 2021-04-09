c=list()

for i in range(4):
    c.append(list(map(int,input())))

K=int(input())

K_list=list()

for i in range(K):
    K_list.append(list(map(int,input().split())))

d=[-1,1]

que=list()
que.append((K_list[0][0]-1,K_list[0][1]))

def clock(a,b):
    if a==1:
        b.insert(0,b.pop())
    else:
        b.append(b.pop(0))

count=0
visit=[0,0,0,0]
while count<K:
    x,y=que.pop(0)
    visit[x]=1
    if x+1<4:
        if c[x][2]!=c[x+1][6] and visit[x+1]==0:
            que.append((x+1,-1*y))
            
    if x-1>=0:
        if c[x][6]!=c[x-1][2] and visit[x-1]==0:
            que.append((x-1,-1*y))
            
    clock(y,c[x])

    if not que:
        count+=1
        visit=[0,0,0,0]
        if count<K:
            que.append((K_list[count][0]-1,K_list[count][1]))

total=0
t=1

for i in range(4):
    total+=t*c[i][0]
    t*=2



print(total)
