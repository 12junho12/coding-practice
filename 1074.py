N,r,c=map(int, input().split())

total=0

for i in range(N):
    if r<2**(N-i-1) and c<2**(N-i-1):
        total+=0

    elif r<2**(N-i-1) and c>=2**(N-i-1):
        total+=4**(N-i-1)
        c-=2**(N-i-1)
    elif r>=2**(N-i-1) and c<2**(N-i-1):
        total+=4**(N-i-1)*2
        r-=2**(N-i-1)
    else:
        total+=4**(N-i-1)*3
        c-=2**(N-i-1)
        r-=2**(N-i-1)

print(total)
