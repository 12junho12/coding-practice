dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n = int(input())
a=list()

for i in range(n):
    a.append(list(map(int, input())))


c=list()

for i in range(n):
    c.append([False]*n)


q=list()
k=list()

for i in range(n):
    bk=0
    for j in range(n):
        if a[i][j]==1:
            q.append((j,i))
            c[i][j]=True
            d=1
            bk=1
            break
    if bk==1:
        break

while q:
    x,y=q.pop(0)
    
    for i in range(4):
        if 0<=x+dx[i]<n and 0<=y+dy[i]<n :
            if a[y+dy[i]][x+dx[i]]==1 and c[y+dy[i]][x+dx[i]]==False:
                q.append((x+dx[i],y+dy[i]))
                c[y+dy[i]][x+dx[i]]=True
                d+=1
     
    if not q:
        for i in range(n):
            bk=0
            for j in range(n):
                if c[i][j]==False and a[i][j]==1:
                    k.append(d)
                    q.append((j,i))
                    c[i][j]=True
                    d=1
                    bk=1
                    break
            if bk==1:
                break
        

k.append(d)
k.sort()
print(len(k))
for i in range(len(k)):
    print(k[i])
