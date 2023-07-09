n=int(input())
l=list(map(int,input().split()))
s=[]
f=0
for i in range(len(l)):
    if(l[i]==l.count(l[i])):
        s.append(l[i])
        f=1
q=set(s)
j=len(q)
if(f==1):
    r=sum(q)/j
    print("%.2f" %r)
else:
    print("-1")