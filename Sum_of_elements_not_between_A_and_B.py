n=int(input())
m=list(map(int,input().split()))
l=[]
k=[]
s=0
a,b=map(int,input().split())
for i in range(a,b+1):
    l.append(i)
for i in m:
    if i not in l:
        k.append(i)
        s=s+i
print(s)