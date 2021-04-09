N,K=map(int,input().split())

dp=list()

for i in range(K):
    dp.append([1])

dp[0]=[1]*(N+1)


for i in range(1,K):
    for j in range(1,N+1):
        dp[i].append(dp[i-1][j]+dp[i][j-1])

print(dp[K-1][N]%1000000000)
