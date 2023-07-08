n=int(input())
a=list(map(int,input().split()))
c,m=0,0
for i in range(n-1,-1,-1):
    m=m+(a[i]*(2**c))
    c+=1
print(m)