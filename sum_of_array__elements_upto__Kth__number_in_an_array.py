n=int(input())
l=list(map(int,input().split()))
k=int(input())
s=0
c=0
for i in range(k):
    s=s+l[i]
    c=1
print(s)