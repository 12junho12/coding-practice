s=int(input())
b=list(map(int, input().split()))

n=int(input())

a=list()
for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(n):
    if a[i][0]==1:
        j=1
        while (a[i][1])*j<=s:
            b[(a[i][1])*j-1]+=1
            j+=1
    else:
        j=1
        b[a[i][1]-1]+=1
        while(a[i][1]-j>=1)and(a[i][1]+j<=s):
            if b[a[i][1]-1-j]%2==b[a[i][1]-1+j]%2:
                b[a[i][1]-1-j]+=1
                b[a[i][1]-1+j]+=1
                j+=1
            else:
                break

for p in range(s):
    if (b[p]%2)==0:
        b[p]=0
    else:
        b[p]=1


for p in range(s):
    if p%20==0:
        if p!=0:
            print('')
    print(b[p], end=" ")
