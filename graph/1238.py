import heapq
import sys

input=sys.stdin.readline

inf=100000000

N,M,X=map(int,input().split())


d=[inf]*N
d[X-1]=0

g = [[] for _ in range(N)]


for i in range(M):
    u,v,w=map(int,input().split())
    g[u-1].append((w,v-1))

heap=list()

heapq.heappush(heap,(0,X-1))

while(heap):
    
    x,y=heapq.heappop(heap)
    
    if d[y]<x:
        continue

    for i in range(len(g[y])):
        nx=g[y][i][1]
        ny=g[y][i][0]
        if d[nx]>d[y]+ny:
            d[nx]=d[y]+ny
            heapq.heappush(heap,(d[nx],nx))

for i in range(N):
    d2=[inf]*N
    d2[i]=0

    heap=list()
    heapq.heappush(heap,(0,i))

    while(heap):
        x,y=heapq.heappop(heap)
        if d2[y]<x:
            continue

        for j in range(len(g[y])):
            nx=g[y][j][1]
            ny=g[y][j][0]
            if d2[nx]>d2[y]+ny:
                d2[nx]=d2[y]+ny
                heapq.heappush(heap,(d2[nx],nx))

    d[i]+=d2[X-1]

print(max(d))
