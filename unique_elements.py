n=int(input())
l=list(map(int,input().split()))
p=[]
for i in range(len(l)):
    if l[i] not in p:
        p.append(l[i])
print(*p)
    