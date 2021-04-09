T=int(input())

a=list()
for i in range(T):
    a.append(int(input()))

g=[0]*max(a)
for i in range(2,int(max(a)**0.5+1)):
    for j in range(i*i,max(a)+1):
        if j%i==0:
            g[j-1]=1
            

for i in a:
    for j in range(int(i/2)):
        if g[int(i/2)-j-1]==0 and g[int(i/2)+j-1]==0:
            print(int(i/2)-j, end=' ')
            print(int(i/2)+j)
            break
