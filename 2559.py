N,K=map(int, input().split())
a=list(map(int,input().split()))
max=0

for i in range(K):
    max+=a[i]

total=max

for i in range(N-K):
    
    total=total-a[i]+a[i+K]

    if total>max:
        max=total

print(max)
