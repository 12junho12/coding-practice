def dfs(graph, start_node):
    visit = list()
    stack = list()

    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])

    return visit

def bfs(graph, start_node):
    visit = list()
    que = list()

    que.append(start_node)

    while que:
        node = que.pop(0)
        if node not in visit:
            visit.append(node)
            que.extend(graph[node])

    return visit

N, M, V = map(int, input().split())
dic1={}
dic2={}
for i in range(1,N+1):
    dic1[i]=[]
    dic2[i]=[]

for i in range(M):
    a,b= map(int, input().split())
    
    dic1[a].append(b)
    dic1[b].append(a)
    dic1[a].sort(reverse=1)
    dic1[b].sort(reverse=1)
    dic2[a].append(b)
    dic2[b].append(a)
    dic2[a].sort()
    dic2[b].sort()
  

for i in dfs(dic1,V):
    print(i, end=" ")

print()
for i in bfs(dic2,V):
    print(i, end=" ")
