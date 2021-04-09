N,M=map(int,input().split())

a=list()

for i in range(N):
    a+=(list(map(int,input().split())))

m=0

for i in range(N*M-3):
    if i//M==(i+3)//M:
        if a[i]+a[i+1]+a[i+2]+a[i+3]>m:
            m=a[i]+a[i+1]+a[i+2]+a[i+3]
    if (i+3*M)//M<N:
        if a[i]+a[i+M]+a[i+2*M]+a[i+3*M]>m:
            m=a[i]+a[i+M]+a[i+2*M]+a[i+3*M]
    if (i+M)%M+1<M and (i+1+M)//M<N:
        if a[i]+a[i+1]+a[i+M]+a[i+M+1]>m:
            m=a[i]+a[i+1]+a[i+M]+a[i+M+1]
    if (i+2*M)%M+1<M and (i+1+2*M)//M<N:
        if a[i]+a[i+1]+a[i+2*M]+a[i+M]>m:
            m=a[i]+a[i+1]+a[i+2*M]+a[i+M]

        if a[i]+a[i+1+2*M]+a[i+2*M]+a[i+M]>m:
            m=a[i]+a[i+1+2*M]+a[i+2*M]+a[i+M]
        if a[i]+a[i+2*M+1]+a[i+M+1]+a[i+M]>m:
            m=a[i]+a[i+2*M+1]+a[i+M+1]+a[i+M]
        if a[i]+a[i+1+M]+a[i+2*M]+a[i+M]>m:
            m=a[i]+a[i+1+M]+a[i+2*M]+a[i+M]
        if a[i]+a[i+1+M]+a[i+2*M+1]+a[i+1]>m:
            m=a[i]+a[i+1+M]+a[i+2*M+1]+a[i+1]
    if (i+M)%M+2<M and (i+2+M)//M<N:
        if a[i]+a[i+1]+a[i+2]+a[i+M]>m:
            m=a[i]+a[i+1]+a[i+2]+a[i+M]
        if a[i]+a[i+1]+a[i+2]+a[i+M+2]>m:
            m=a[i]+a[i+1]+a[i+2]+a[i+M+2]
        if a[i]+a[i+1]+a[i+M+1]+a[i+M+2]>m:
            m=a[i]+a[i+1]+a[i+M+1]+a[i+M+2]
        
        if a[i]+a[i+1]+a[i+2]+a[i+M+1]>m:
            m=a[i]+a[i+1]+a[i+2]+a[i+M+1]
       
        if a[i]+a[i+M]+a[i+M+1]+a[i+M+2]>m:
            m=a[i]+a[i+M]+a[i+M+1]+a[i+M+2]
    if i%M>0 and (i-1+2*M)//M<N:
        
        if a[i]+a[i+M]+a[i+M-1]+a[i+2*M-1]>m:
            m=a[i]+a[i+M]+a[i+M-1]+a[i+2*M-1]
        
        if a[i]+a[i+M]+a[i+M-1]+a[i+2*M]>m:
            m=a[i]+a[i+M]+a[i+M-1]+a[i+2*M]
    if M-1>i%M>0 and (i+M)//M<N:
        
        if a[i]+a[i+M]+a[i+M-1]+a[i+1]>m:
            m=a[i]+a[i+M]+a[i+M-1]+a[i+1]
        
        if a[i]+a[i+M]+a[i+M-1]+a[i+M+1]>m:
            m=a[i]+a[i+M]+a[i+M-1]+a[i+M+1]
    if i%M>0 and (i+2*M)//M<N:
        
        if a[i]+a[i+M]+a[i+2*M]+a[i+2*M-1]>m:
            m=a[i]+a[i+M]+a[i+2*M]+a[i+2*M-1]
    if i%M>1 and (i+1*M)//M<N:
        
        if a[i]+a[i+M]+a[i+M-1]+a[i+M-2]>m:
            m=a[i]+a[i+M]+a[i+M-1]+a[i+M-2]


print(m)
    

