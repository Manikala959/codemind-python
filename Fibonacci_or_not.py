n=int(input())
a=0
b=1
s=0
for i in range(0,100):
    c=a+b
    a=b
    b=c
    if(c==n):
        print("True")
        break
    else:
        s+=1
if(s==100):
    print("False")