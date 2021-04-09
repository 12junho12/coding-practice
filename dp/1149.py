N=int(input())

H=list()
for i in range(N):
    H.append(list(map(int, input().split())))

d=list()
a=[[0,0,0]]
a+=H

for i in range(N+1):
	d.append([])

d[0].extend([0,0,0])

def mm(a,b):
	if a>b:
		return b
	else:
		return a


for i in range(1,N+1):
			
	d[i].append(mm(d[i-1][1], d[i-1][2]) + a[i][0])
	d[i].append(mm(d[i-1][0], d[i-1][2]) + a[i][1])
	d[i].append(mm(d[i-1][0], d[i-1][1]) + a[i][2])
				

	
print(mm(mm(d[N][0],d[N][1]),d[N][2]))
