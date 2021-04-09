N=int(input())

a=list()
b={}
for i in range(N):
    a.append(list(input().split()))
    b[a[i][0]]=list()

for i in range(N):
    b[a[i][0]]+=a[i][1:]

c=list()

def preorder(w):

    c.append(w)
    if b[w][0]!=".":
        preorder(b[w][0])
    if b[w][1]!=".":
        preorder(b[w][1])

def inorder(w):

    if b[w][0]!=".":
        inorder(b[w][0])
    c.append(w)
    if b[w][1]!=".":
        inorder(b[w][1])


def postorder(w):
    
    if b[w][0]!=".":
        postorder(b[w][0])
    if b[w][1]!=".":
        postorder(b[w][1])
    c.append(w)

preorder("A")
for i in range(N):
    print(c[i], end="")
c.clear()
print()
inorder("A")
for i in range(N):
    print(c[i], end="")
c.clear()
print()
postorder("A")
for i in range(N):
    print(c[i], end="")

