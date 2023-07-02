def prime(a):
    if a<2:
        return(False)
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return(False)
    return(True)
a=int(input())
b=int(input())
dc=0
for n in range(a,b+1):
    if prime(n):
        dc+=1
print(dc)
    