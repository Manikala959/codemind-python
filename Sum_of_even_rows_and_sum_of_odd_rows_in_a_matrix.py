n,m=map(int,input().split())
ev=0
odd=0
for j in range(n):
    m=list(map(int,input().split()))
    for i in m:
        if j%2:
            odd=odd+i
        else:
            ev=ev+i
print(ev,odd)