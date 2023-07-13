def dig(n):
    if(n==0):
        return 1
    if n<0:
        n=abs(n)
    c=0
    while n>0:
        r=n%10
        c+=1
        n=n//10
    return c
n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(n):
    if(dig(l[i])>c):
        c=dig(l[i])
for i in range(n):
    if(dig(l[i])==c):
        print(l[i],end=" ")