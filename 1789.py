import sys
input = sys.stdin.readline

N=int(input())

a=1
t=0

while t+a<=N:
    t+=a
    a+=1

print(a-1)
