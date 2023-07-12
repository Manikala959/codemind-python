n=int(input())
l=list(map(int,input().split()))
s=0
k=0
for i in range(n):
    if i%2==0 or i==0:
        s=s+l[i]
    else:
        k=k+l[i]        
if(abs(s-k))==0:
    print("YES")
else:
    print("NO")