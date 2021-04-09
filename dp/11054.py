N=int(input())

A=list(map(int, input().split()))
dp=[0]*N
dp2=[0]*N

for i in range(1,N):
    t=0
    for j in range(i):
        if A[i]>A[j]:
            t=dp[j]+1
        if t>dp[i]:
            dp[i]=t

A.reverse()
for i in range(1,N):
    t=0
    for j in range(i):
        if A[i]>A[j]:
            t=dp2[j]+1
        if t>dp2[i]:
            dp2[i]=t

dp2.reverse()

for i in range(N):
    dp[i]+=dp2[i]

print(max(dp)+1)
