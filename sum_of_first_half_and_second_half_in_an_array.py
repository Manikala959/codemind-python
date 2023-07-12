n=int(input())
l=list(map(int,input().split()))
s1=0
s=0
for i in range(n//2):
    s=s+l[i]
for i in range(n//2,n):
    s1=s1+l[i]
print(s)
print(s1)