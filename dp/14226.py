S=int(input())

dp=[(1,1)]

for i in range(1,S):
    t=0
    mx=1000
    my=0
    for j in range(i):
        x,y=dp[j]
        t=(i+1-x)//y
        if t*y==i+1-x and mx>x+(t*y):
            mx=x+(t*y)
            my=y

        a=1
        while a*(j+1)<i+1:
            a+=1
        t=a*(j+1)
        if mx>x+a+(t-i-1):
            mx=x+a+(t-1-i)
            my=j+1


    dp.append((mx,my))

print(dp[S-1][0])
    
