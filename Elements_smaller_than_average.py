n=int(input())
l=list(map(int,input().split()))
a=sum(l)//n
s=[]
for i in range(len(l)):
    if(l[i]<=a):
        s.append(l[i])
print(len(s))