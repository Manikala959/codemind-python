n=int(input())
m=list(map(int,input().split()))
l=[]
k=[]
c=0

a,b=map(int,input().split())
for i in range(a,b+1):
    l.append(i)
for i in m:
    if i not in l:
        k.append(i)
        c+=1
if c>0:
    print(*k)
else:      
    print(-1)