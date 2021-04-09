a=input()

s=list()
M=list()

for i in range(len(a)):
   
    if a[i]=="(":
        s.append((3,"("))
    elif a[i]==")":
        while(s):
            x,y=s.pop()
            if x==3:
                break
            else:
                M.append(y)
            
    elif a[i]=="*":
        if not s:
            s.append((2,"*"))
        else:
            while(s):
                if 3>s[len(s)-1][0]>=2:
                    M.append(s.pop()[1])
                else:
                    break
            s.append((2,"*"))
    elif a[i]=="/":
        if not s:
            s.append((2,"/"))
        else:
            while(s):
                if 3>s[len(s)-1][0]>=2:
                    M.append(s.pop()[1])
                else:
                    break
            s.append((2,"/"))
    elif a[i]=="+":
        if not s:
            s.append((1,"+"))
        else:
            while(s):
                if 3>s[len(s)-1][0]>=1:
                    M.append(s.pop()[1])
                else:
                    break
                
            s.append((1,"+"))
    elif a[i]=="-":
        if not s:
            s.append((1,"-"))
        else:
            while(s):
                if 3>s[len(s)-1][0]>=1:
                    M.append(s.pop()[1])
                else:
                    break
            s.append((1,"-"))
    else:
        M.append(a[i])

while(s):
   
    M.append(s.pop()[1])


for i in range(len(M)):
    print(M[i], end="")
