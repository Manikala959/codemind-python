n=int(input())
l=list(map(int,input().split()))
s=[]
f=0
for i in range(len(l)):
    if(l[i]==l.count(l[i])):
        s.append(l[i])
a=[]
for i in s:
    if i not in a:
        a.append(i)
        f=1
if(f==1):
    print(*a)
else:
    print("-1")