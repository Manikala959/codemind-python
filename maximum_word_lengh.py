n=list(input().split())
m=[]
for i in range(len(n)):
    x=list(n[i])
    m.append(len(x))
print(max(m))