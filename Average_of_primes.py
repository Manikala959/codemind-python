def prime(n):
    if n<2:
        return 0
    
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0
    return 1

n=int(input())
l=list(map(int,input().split()))
s=[]
for i in range(len(l)):
    if(prime(l[i])==1):
        s.append(l[i])
w=sum(s)
a=w/len(s)
print(format(a,".2f"))