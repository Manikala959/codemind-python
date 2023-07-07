n=int(input())
a=list(map(int,input().split()))
s=0
for i in a:
    s=s+i
   
    m=s//n
if(m in a):
    print("True")
else:
    print("False")