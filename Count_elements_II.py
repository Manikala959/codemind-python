n,m=map(int,input().split())
l=list(map(int,input().split()))
l1=list(map(int,input().split()))
k=[]
d=[]
for i in l:
    for j in l1:
        if i==j:
            k.append(i)
for i in l:
    for j in l1:
        if i not in k:
            if i not in d:
                d.append(i)
        if j not in d:
            if j not in k:
                d.append(j)
print(len(d))
    
