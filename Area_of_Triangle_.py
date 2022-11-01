from math import*
a,b,c=map(int,input().split())
s=(a+b+c)/2
Area=sqrt(s*(s-a)*(s-b)*(s-c))
print('{:.2f}'.format(Area))