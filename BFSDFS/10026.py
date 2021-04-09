dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n = int(input())
a=list()

for i in range(n):
    a.append(list(input()))


c=list()

for i in range(n):
    c.append([False]*n)


q=list()

q.append((0,0))
c[0][0]=True
d=1

while q:
    x,y=q.pop(0)
    rgb=a[y][x]
    for i in range(4):
        if 0<=x+dx[i]<n and 0<=y+dy[i]<n :
            if a[y+dy[i]][x+dx[i]]==rgb and c[y+dy[i]][x+dx[i]]==False:
                q.append((x+dx[i],y+dy[i]))
                c[y+dy[i]][x+dx[i]]=True
     
    if not q:
        for i in range(n):
            bk=0
            for j in range(n):
                if c[j][i]==False:
                    q.append((i,j))
                    c[j][i]=True
                    d+=1
                    bk=1
                    break
            if bk==1:
                break

for i in range(n):
    for j in range(n):
        if a[i][j]=='R':
            a[i][j]='G'

del c[:]

for i in range(n):
    c.append([False]*n)

q.append((0,0))
c[0][0]=True
d2=1

while q:
    x,y=q.pop(0)
    rgb=a[y][x]
    for i in range(4):
        if 0<=x+dx[i]<n and 0<=y+dy[i]<n :
            if a[y+dy[i]][x+dx[i]]==rgb and c[y+dy[i]][x+dx[i]]==False:
                q.append((x+dx[i],y+dy[i]))
                c[y+dy[i]][x+dx[i]]=True
                
    
    if not q:
        for i in range(n):
            bk=0
            for j in range(n):
                if c[j][i]==False:
                    q.append((i,j))
                    c[j][i]=True
                    d2+=1
                    bk=1
                    break
            if bk==1:
                break

print(d,d2)
