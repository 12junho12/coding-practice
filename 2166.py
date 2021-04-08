ord ={0:5, 1:3, 2:4, 3:1, 4:2, 5:0}

n=int(input())
a=[]

for i in range(n):
    a.append(list(map(int, input().split())))

bot=0
top=0

mx=0;

for j in range(6):
    total=0
    for i in range(n):
        b=[1,2,3,4,5,6]
        if i==0:
            bot=a[i][j]
            top=a[i][ord[j]]
            b.remove(bot)
            b.remove(top)
            total+=max(b)
        else:
            bot=top
            top=a[i][ord[a[i].index(bot)]]
            b.remove(bot)
            b.remove(top)
            total+=max(b)
    if mx<total:
        mx=total


print(mx)
