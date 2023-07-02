a=int(input())
b=int(input())
for i in range(a,b+1):
    rev=0
    tem=i
    while(tem>0):
        r=tem%10
        rev=rev*10+r
        tem=tem//10
    if(rev==i):
        print(i,end=' ')