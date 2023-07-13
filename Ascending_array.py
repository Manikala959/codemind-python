n=int(input())
l=list(map(int,input().split()))
l1=sorted(l)
s=[]
for i in range(len(l)):
    for j in range(len(l1)):
        if l[i]==l1[j]:
            s.append(l[i])
        
if l1==s:
    print("yes")
else:
    print("no")