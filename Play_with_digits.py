
def dig(n):
    s=0
    while n>0:
        r=n%10
        s=s+r
        n=n//10
    return s


n=int(input())
l=list(map(int,input().split()))
sum=0
for i in range(len(l)):
    sum=sum+dig(l[i])
print(sum)