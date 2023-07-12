m=int(input())
n=int(input())
s=0
for i in range(0,m):
    a=list(map(int,input().split()))
    s=s+sum(a)
print(s)

