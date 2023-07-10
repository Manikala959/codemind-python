def rev(n):
    sum=0
    while(n>0):
        d=n%10
        sum=sum*10+d
        n=n//10
    return sum
    
n=int(input())
l=list(map(int,input().split()))
k=[]

for i in range(len(l)):
    v=rev(l[i])
    k.append(v)
print(*k)
    