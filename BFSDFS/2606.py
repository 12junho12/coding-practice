N=int(input())
C=int(input())

net=list()
for i in range(C):
    net.append(list(map(int, input().split())))

dic={}
for i in range(N):
    dic[i+1]=[]

for i in range(C):
    dic[net[i][0]].append(net[i][1])
    dic[net[i][1]].append(net[i][0])

visit=[0]*N
que=list()
que.append(1)
cnt=-1

while que:
    x=que.pop(0)
    visit[x-1]=1
    for i in dic[x]:
        if visit[i-1]==0 and i not in que:
            que.append(i)
    
    cnt+=1

print(cnt)
