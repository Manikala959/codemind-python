n=int(input())
a=list(map(int,input().split()))
e=o=0
for i in range(n):
    if i%2==0:
        e+=a[i]
    else:
        o+=a[i]
k=abs(e-o)
if(k%4)==0:
    print("X")
else:
    print("Y")




'''
for i in a:
    if a.count(i)==1:
        b.append(i)
if(len(b)==0):
    print("-1")
else:        
    print(max(b))'''