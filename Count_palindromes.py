def rev(n):
    sum=0
    temp=n
    while(n>0):
        d=n%10
        sum=sum*10+d
        n=n//10
    if sum==temp:
        return 1
    else:
        return 0
    
n=int(input())
l=list(map(int,input().split()))
count=0
for i in range(len(l)):
    if rev(l[i])==1:
        count+=1
print(count)
