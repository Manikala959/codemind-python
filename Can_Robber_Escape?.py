n=int(input())
m=0
a=list(map(int,input().split()))
for i in range(n):
    if a[i]%2!=0:
        m+=1
if m<=2:
    print("YES")
else:
    print("NO")