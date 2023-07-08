a,b,c=list(map(int,input().split()))
d=2*a*b*c*512
e=d//1024
print(e,end='KB')