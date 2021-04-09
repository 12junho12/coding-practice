M=int(input())

m1="Messi "
m2="Messi Gimossi "

messi=list()
messi.append((1,0))
messi.append((1,1))
ni=1
a=1
b=1

while M>a*6+b*8:
    a=messi[ni][0]+messi[ni-1][0]
    b=messi[ni][1]+messi[ni-1][1]
    messi.append((a,b))
    ni+=1


while ni>=2:
    a=messi[ni-1][0]
    b=messi[ni-1][1]

    if M>a*6+b*8:
        M-=(a*6+b*8)
        ni-=2
    else:
        
        ni-=1


if ni==0:
    if m1[M-1]==" ":
        print("Messi Messi Gimossi")
    else:
        print(m1[M-1])
else:
    if m2[M-1]==" ":
        print("Messi Messi Gimossi")
    else:
        print(m2[M-1])
