n=int(input())
l=list(map(int,input().split()))
s=[]

for i in range(len(l)):
    if(l[i]%2!=0):
        s.append(l[i])
p=set(s)
print(sum(p))