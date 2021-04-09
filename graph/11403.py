N=int(input())

a=list()

for i in range(N):
    a.append(list(map(int,input().split())))

 
for i in range(N):

    que=list()

    for p in range(N):
        que.append([])
        for q in range(N):
            if a[p][q]==1:
                que[p].append(q)

    while(que[i]):
        x=que[i].pop()
        for j in que[x]:
            if a[i][j]==0:
                que[i].append(j)
                a[i][j]=1

for i in range(N):
    for j in range(N):
        print(a[i][j], end=" ")

    print()

