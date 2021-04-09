T=int(input())

def mm(a,b):
    if a>b:
        return a
    else:
        return b

for i in range(T):
    n=int(input())
    a=list()
    for i in range(2):
        a.append(list(map(int,input().split())))

    dp=list()
    dp.append([0,a[0][0],a[1][0]])
    
    for i in range(1,n):
        dp.append([max(dp[i-1]),mm(dp[i-1][2],dp[i-1][0])+a[0][i],mm(dp[i-1][1],dp[i-1][0])+a[1][i]])
   
    print(max(dp[n-1]))
