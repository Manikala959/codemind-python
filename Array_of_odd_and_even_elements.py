n=int(input())
l=list(map(int,input().split()))
k=[]
m=[]
for i in l:
    if i%2!=0:
        k.append(i)
    if i%2==0:
        m.append(i)
print(*(k+m))