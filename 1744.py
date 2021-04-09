n=int(input())

a=list()
for i in range(n):
    a.append(int(input()))

a.sort(reverse=1)
s=list()
s2=list()
t=0
for i in range(n):
    if a[i]>1:
        s.append(a[i])
    elif a[i]==1:
        t+=a[i]
    else:
        s2.append(a[i])

    if len(s)==2:
        t+=s.pop()*s.pop()

while(s):
    t+=s.pop()

while(s2):
    if len(s2)>=2:
        t+=s2.pop()*s2.pop()
    else:
        if(s2):
            t+=s2.pop()
        break

print(t)
