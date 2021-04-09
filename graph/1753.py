import heapq
import sys

input=sys.stdin.readline

inf=100000000

V,E=map(int,input().split())
K=int(input())

d=[inf]*V
d[K-1]=0

g = [[] for _ in range(V)]


for i in range(E):
    u,v,w=map(int,input().split())
    g[u-1].append((w,v-1))

heap=list()

heapq.heappush(heap,(0,K-1))

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


for i in range(V):
    if d[i]==inf:
        print("INF")
    else:
        print(d[i])
