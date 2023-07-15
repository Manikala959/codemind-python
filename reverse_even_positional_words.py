n=input().split()
for i in range(len(n)):
    if i%2==0:
        k=n[i]
        print(k[::-1],end=' ')
    else:
        print(n[i],end=' ')