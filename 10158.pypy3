xy=list(map(int,input().split()))
ab=list(map(int,input().split()))
t=int(input())
k=[]

if ((ab[0]+t)//xy[0])%2==0:
    k.append((ab[0]+t)%xy[0])
else:
    k.append(xy[0]-(ab[0]+t)%xy[0])
    
if ((ab[1]+t)//xy[1])%2==0:
    k.append((ab[1]+t)%xy[1])
else:
    k.append(xy[1]-(ab[1]+t)%xy[1])

print(k[0], k[1])
