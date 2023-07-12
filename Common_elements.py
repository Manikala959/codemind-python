n,m=map(int,input().split())
n=list(map(int,input().split()))
m=list(map(int,input().split()))
s=[]
for i in range(len(n)):
    for j in range(len(m)):
        if(n[i]==m[j]):
            s.append(n[i])
x=[]
for i in s:
    if i not in x:
            x.append(i)
        
print(*x)
    
