N=int(input())

p=list()
numbers=list()
isSelected=[False]*9

def perm(cnt):
    global p
    if cnt==3:
        p+=numbers
    
    else:
        for i in range(9):
            if isSelected[i]==True:
                continue
            numbers.append(i+1)
            isSelected[i]=True
            perm(cnt+1)
            isSelected[i]=False
    if numbers:
        numbers.pop()

perm(0)

for j in range(N):
    
    i=0
    a,s,b=map(int, input().split())
    x=a//100
    y=(a-(x*100))//10
    z=a%10
    cnt=int(len(p)/3)
    while cnt>0:
        t=0
        if x==p[3*i]:
            t+=10
            
        if x==p[3*i+1]:
            t+=1
            
        if x==p[3*i+2]:
            t+=1
            
        if y==p[3*i+1]:
            t+=10
            
        if y==p[3*i+2]:
            t+=1
            
        if y==p[3*i]:
            t+=1
            
        if z==p[3*i+2]:
            t+=10
            
        if z==p[3*i+1]:
            t+=1
            
        if z==p[3*i]:
            t+=1
            
        if t!=(10*s+b):
            del p[3*i]
            del p[3*i]
            del p[3*i]
        else:
            i+=1
           
     
        cnt-=1
               

print(int(len(p)/3))
