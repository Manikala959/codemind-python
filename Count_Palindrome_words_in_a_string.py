n=input()
l=n.lower()
x=l.split()
c=0
for i in x:
    v=i[::-1]
    if(i==v):
        c+=1
print(c)