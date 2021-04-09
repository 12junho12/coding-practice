T=int(input())
pt=list()
for i in range(T):
    K=int(input())
    a=list(map(int,input().split()))

    sum=list()
    s=0
    dp=list()
    for i in range(K):
        s+=a[i]
        sum.append(s)
        dp.append([0]*K)

    for i in range(1,K):
        
        for j in range(i,K):
            p=1
            m=1000000000
            for z in range(i):
                if dp[i-z-1][j-z-1]+dp[z][j]<m:
                    m=dp[i-z-1][j-z-1]+dp[z][j]


            if j-i>0:
                dp[i][j]=sum[j]-sum[j-i-1]+m
            else:
                dp[i][j]=sum[j]+m


    pt.append(dp[K-1][K-1])

for i in range(T):
    print(pt[i])
    

   
