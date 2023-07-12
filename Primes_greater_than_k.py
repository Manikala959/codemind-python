n=int(input())
a=list(map(int,input().split()))
k=int(input())
c=0
for i in a:
    if(i>=k):
        for j in range(2,i//2+1):
            if(i%j==0):
                break
        else:
            c+=1
print(c)