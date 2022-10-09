def adddigits(num):
    s=0
    while num:
        d=num%10
        num=num//10
        s=s+d
    return s
n=int(input())
while n>9:#11>9
    n=adddigits(n)#11
print(n)