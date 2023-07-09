n=int(input())
l=list(map(int,input().split()))
s=[]
for i in range(len(l)):
    if(l[i]%2==0):
        s.append(l[i])
        
k=set(s)
print(len(k))