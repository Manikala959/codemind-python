n=int(input())
l=list(map(int,input().split()))
s=[]
c=0
for i in range(len(l)):
    if(l[i]==l.count(l[i])):
        s.append(l[i])
m=[]
for i in s:
    if i not in m:
        m.append(i)
b=len(m)
print(b)
